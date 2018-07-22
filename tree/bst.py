from node import Node

class BST:
    def __init__(self, data=None):
        if not data:
            raise Exception("Please Provide Data")
        self.root = None
        for i in data:
            self.insert(self.root, i)
    
    def insert(self, root, data):
        if not root:
            self.root = Node(data)
        else:
            if data <= root.data:
                if not root.left:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)
            else:
                if not root.right:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)

    def _inorder(self,res,root=None):
        if not root : return
        self._inorder(res, root.left)
        res.append(root)
        self._inorder(res, root.right)
    
    @property
    def inorder(self):
        result = []
        self._inorder(result, self.root)
        return result

    def max(self, root):
        if not root: return
        prev = root
        start = root.right
        while start is not None:
            temp = start
            try:
                start = start.right
            except Exception as e:
                break
            prev = temp
        return prev
    
    def min(self, root):
        if not root: return
        prev = root
        start = root.left
        while start:
            temp = start
            try:
                start = start.left
            except Exception as e:
                break
            prev = temp
        return prev
    
    def _find(self,root,data):
        if root is None : return None
        if root.data == data:
            return root
        elif data < root.data:
            return self._find(root.left, data)
        else:
            return self._find(root.right, data)
    
    def __contains__(self, item):
        if type(item) != int: raise KeyError()
        
        return False if self._find(self.root, item) is None else True
        
    def lca(self,root,a,b):
        while root:
            if a <= root.data and b > root.data or a > root.data and b <= root.data:
                return root
            if a <= root.data:
               root = root.left
            else:
                root = root.right
            
        
        
    

if __name__ == '__main__':
    tree = BST([234,2,564,34,234,578,13132,12,32,545])
    root = tree.root
    print('Inorder = {}'.format(tree.inorder))
    print('Max = {}'.format(tree.max(root)))
    print('Min = {}'.format(tree.min(root)))
    res = 32 in tree
    print('32 in Tree = {}'.format(32 in tree))
    print('47 in Tree = {}'.format(47 in tree))
    print('Least Common Ancestor for 12,234 = {}'.format(tree.lca(root,12,234)))

    

