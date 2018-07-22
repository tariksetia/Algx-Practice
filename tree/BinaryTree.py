from queue import Queue
from collections import defaultdict as dd
from node import Node

class BinaryTree:
    
    def __init__(self, data=None):
        if len(data)<1:
            raise ValueError('Empty List Provided')

        self.root = Node(data=data[0])
        data = data[1:]

        for i in data:
            self.insert(i)
    
    def insert(self,data):
        buff = Queue()
        buff.put(self.root)

        while not buff.empty():
            node = buff.get()

            if not node.left:
                node.left = Node(data)
                return
            if not node.right:
                node.right = Node(data)
                return
            
            if node.left: buff.put(node.left)
            if node.right: buff.put(node.right)
    
    def max_node(self):
        max_data = float('-inf')
        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            max_data = max(max_data,node.data)

            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        
        return max_data
    
    def size_recursive(self,root=None):
        if root == None:
            return 0
        
        return 1 + self.size_recursive(root.left) + self.size_recursive(root.right)
        
    def size(self):
        count = 0
        q = Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            count += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return count
    
    def find_recursive(self, data, root=None):
        if root == None:
            return False
        if root.data == data:
            return root

        node = self.find_recursive(data,root.left)
        if node:
            return node
        else:
            return self.find_recursive(data, root.right)
    
    def find(self, data):
        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            if node.data == data: return node
            
            if node.left: q.put(node.left)
            if node.rihgt: q.put(node.right)
    


    def print_level_order_reverse(self):
        q = Queue()
        stack = []
        q.put(self.root)

        while not q.empty():
            node = q.get()
            stack.append(node)
            if node.left: q.put(node.left)
            if node.right: q.put(node.right)
        
        return stack
    
    
    def depth_recursive(self, root): # or height
        if not root: return 0
        return 1 + max(self.depth_recursive(root.left) , self.depth_recursive(root.right))
    
    def height(self):
        q = Queue()
        depth = 1
        q.put((self.root,1))
        while not q.empty():
            node, temp = q.get()
            depth = max(depth,temp)

            if node.left:
                q.put((node.left, depth+1))
            if node.right:
                q.put((node.right, depth+1))
        
        return depth
            
    def deepest_node(self,root=None):
        if root == None:
            root = self.root
        q = Queue()
        node = None
        q.put(root)

        while not q.empty():
            node = q.get()
            if node.left: q.put(node.left)
            if node.right: q.put(node.right)
        return node

    def find_parent(self,child):
        q = Queue()
        q.put(self.root)
        node = None
        while not q.empty():
            node = q.get()

            if node.left == child or node.right == child:
                return node
            
            if node.left: q.put(node.left)
            if node.right: q.put(node.right)
        
        return None


    def delete_node(self,data):
        node = self.find(data)
        deepest_node = self.deepest_node(node)
        pass
    
    @property
    def node_count(self):
        q = Queue()
        q.put(self.root)
        leaves = 0
        full_nodes = 0
        half_nodes = 0
        while not q.empty():
            node = q.get()
            if not node.left and not node.right:
                leaves +=1
            
            if node.left and node.right:
                full_nodes += 1

            if not node.left and node.right:
                half_nodes +=1
            
            if not node.right and node.left:
                half_nodes += 1

            if node.left: q.put(node.left)
            if node.right: q.put(node.right)
        
        return (full_nodes,half_nodes,leaves)
    
    def isIdenticalWith(self,tree):
        pass

    @property
    def level_with_max_sum(self):
        levels = dd(list)
        q = Queue()
        q.put((self.root,0))
        level = 0
        while not q.empty():
            node,level = q.get()
            levels[level].append(node.data)

            if node.right:
                q.put((node.right,1+level))
            if node.left:
                q.put((node.left,1+level))        

        levels = {sum(v):k for k,v in levels.items()}
        return levels[max(levels.keys())]
    
    def path_appender(self, node, path, paths):
        if not node: 
            return

        path.append(node)

        if not (node.left and node.right):
            print(path)
        else:
            self.path_appender(node.left, path,paths)
            self.path_appender(node.right,path,paths)

    def root_to_leaf_paths(self):
        paths = []
        self.path_appender(self.root,[],paths)
        [print(path) for path in paths]

    def _sum_nodes(self,root):
        return self._sum_nodes(root.left) + self._sum_nodes(root.right) if root is not None else 0
        
    @property
    def sum_nodes(self):
        self._sum_nodes(self.root)

    
        

if __name__ == '__main__':
    
    tree = BinaryTree([4,3,5,6,7,8,9,10])
    root = tree.root
    print('Max Node = {}'.format(tree.max_node()))
    print('Tree Size Recursive = {}'.format(tree.size_recursive(tree.root)))
    print('Tree Size = {}'.format(tree.size()))
    print('Find Recursive = {}'.format(tree.find_recursive(27,root)))
    print('Level Order = {}'.format(tree.print_level_order_reverse()))
    print('Height = {}'.format(tree.height()))
    print('Height Recursive = {}'.format(tree.depth_recursive(root)))
    
    full,half,leaves = tree.node_count
    print('Full nodes = {}'.format(full))
    print('Half nodes = {}'.format(half))
    print('Lead nodes = {}'.format(leaves))
    print('Level with max sum = {}'.format(tree.level_with_max_sum))






    
            

            