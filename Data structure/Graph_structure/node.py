class Node:
    def __init__(self,id):
        self.id = id
        self.is_visited = False
        self.pre_node = None
        self.connected_to = []
        self.distance = 0

    def get_id(self):
        return self.id

    def get_visited(self):
        return self.is_visited

    def set_visited(self,visited):
        self.is_visited = visited
    
    def get_pre(self):
        return self.pre_node
    
    def set_pre(self,node):
        self.pre_node = node
    
    def get_distance(self):
        return self.distance
    
    def set_distance(self,distance):
        self.distance = distance

    def get_connection(self):
        return self.connected_to

    def add_connection(self,node):
        self.connected_to.append(node)