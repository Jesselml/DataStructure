from node import Node
class SparseGraph:
    def __init__(self,directed=False):
        #key是node的id，value是Node  
        self.node_dict = {}
        self.node_num = 0
        self.driected = directed
        #连通分量
        self.connected_count = 0
    
    def get_node(self):
        rt = []
        for i in self.node_dict:
            rt.append(i)
        return (rt)

    def add_node(self,id,new_node):
        self.node_num+=1
        self.node_dict[id] = new_node

    def add_edge(self,id1,id2):
        if id1 not in self.node_dict:
            node1 = Node(id1)
            self.add_node(id1,node1)
        if id2 not in self.node_dict:
            node2 = Node(id2)
            self.add_node(id2,node2)
        self.node_dict[id1].add_connection(self.node_dict[id2])
        #如果是自环边则不需要第二次添加，如果是有向图也不需要继续添加
        if id1 == id2 or self.driected:
            return
        self.node_dict[id2].add_connection(self.node_dict[id1])
    
    #深度优先遍历 - 设置是否遍历过和前驱节点两个参数
    def dfs(self,node):
        for next_node in node.get_connection():
            if not next_node.get_visited():
                next_node.set_visited(True)
                next_node.set_pre(node)
                self.dfs(next_node)

    ##深度优先1计算连通分量
    def cal_cc(self):
        for id in self.node_dict:
            self.node_dict[id].set_visited(False)
            self.node_dict[id].set_pre(None)
        for id in self.node_dict:
            node = self.node_dict[id]
            if not node.get_visited():
                node.set_visited(True)
                self.dfs(node)
                self.connected_count+=1
    
    def get_cc(self):
        return self.connected_count
    
    #深度优先2判断两个点是否相连
    def is_connected(self,id1,id2):
        for id in self.node_dict:
            self.node_dict[id].set_visited(False)
            self.node_dict[id].set_pre(None)
        self.node_dict[id1].set_visited(True)
        self.dfs(self.node_dict[id1])
        if self.node_dict[id2].get_visited():
            return True
        return False
    
    #深度优先3寻找两个点之间的路径
    def get_path(self,id1,id2):
        if not self.is_connected(id1,id2):
            return "There is no path between",id1,"and",id2
        for id in self.node_dict:
            self.node_dict[id].set_visited(False)
            self.node_dict[id].set_pre(None)
        self.node_dict[id1].set_visited(True)
        self.dfs(self.node_dict[id1])
        #从后到前依次查找
        rt = []
        current_node = self.node_dict[id2]
        while current_node != self.node_dict[id1]:
            rt.append(current_node.get_id())
            current_node = current_node.get_pre()
        rt.append(self.node_dict[id1].get_id())
        return rt[::-1]
    
    #广度优先遍历 - 队列实现，对每个节点设置距离来寻找最短路径
    def bfs(self,node):
        queue = []
        queue.append(node)
        node.set_distance(0)
        while queue:
            current_node = queue.pop(0)
            for next_node in current_node.get_connection():
                if not next_node.get_visited():
                    next_node.set_visited(True)
                    next_node.set_pre(current_node)
                    next_node.set_distance(current_node.get_distance()+1)
                    queue.append(next_node)

    def get_shortest_path(self,id1,id2):
        if not self.is_connected(id1,id2):
            return "There is no path between",id1,"and",id2
        for id in self.node_dict:
            self.node_dict[id].set_visited(False)
            self.node_dict[id].set_pre(None)
            self.node_dict[id].set_distance(0)
        self.node_dict[id1].set_visited(True)
        self.bfs(self.node_dict[id1])
        #从后到前依次查找
        rt = []
        current_node = self.node_dict[id2]
        while current_node != self.node_dict[id1]:
            rt.append(current_node.get_id())
            current_node = current_node.get_pre()
        rt.append(self.node_dict[id1].get_id())
        return rt[::-1]

    def show(self):
        rt = {}
        for i in self.node_dict:
            rt[i] = []
            for j in self.node_dict[i].get_connection():
                rt[i].append(j.get_id())
        return rt

