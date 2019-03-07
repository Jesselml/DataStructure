from bstmap import BSTMap
class Map:
    def __init__(self):
        self.bst_map = BSTMap()
    
    def add(self,key,val):
        self.bst_map.add(key,val)

    def remove(self,key):
        self.bst_map.remove(key)
    
    def get_size(self):
        return self.bst_map.get_size()
    
    def contains(self,key):
        return self.bst_map.contains(key)
    
    def is_empty(self):
        return self.bst_map.is_empty()

    def get_val(self,key):
        return self.bst_map.get_val(key)
    
    def set_val(self,key,val):
        self.bst_map.set_val(key,val)

    

