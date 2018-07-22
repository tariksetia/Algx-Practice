from queue import Queue 

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)
    
    def __bool__(self):
        return True if self.data is not None else False
    
    @property
    def leaf(self):
        return False if (self.right and self.left) else True

