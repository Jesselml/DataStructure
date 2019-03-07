from bst import BST
class Set:
    def __init__(self):
        self.bst_set = BST()
    
    def add(self,e):
        self.bst_set.add2(e)

    def remove(self,e):
        self.bst_set.remove(e)
    
    def get_size(self):
        return self.bst_set.get_size()
    
    def contains(self,e):
        return self.bst_set.contains(e)
    
    def is_empty(self):
        return self.bst_set.is_empty()
    

