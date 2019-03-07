from heap import Heap

class PriorityQueue:
    def __init__(self):
        self.__heap = Heap()
    
    def enqueue(self,val):
        self.__heap.add(val)
    
    def dequeue(self):
        return self.__heap.extract_max()
    
    def get_front(self):
        return self.__heap.find_max()
    
    def get_size(self):
        return self.__heap.get_size()

    def is_empty(self):
        return self.__heap.is_empty()