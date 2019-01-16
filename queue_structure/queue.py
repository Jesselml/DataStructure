class Queue():
    def __init__(self):
        self.__queue = []
    
    def enqueue(self,e):
        self.__queue.append(e)

    def dequeue(self):
        return self.__queue.pop(0)

    def getFront(self):
        return self.__queue[0]

    def getSize(self):
        return len(self.__queue)

    def isEmpty(self):
        return self.__queue==[]
    
    def showQueue(self):
        return "Queue: ",self.__queue

    
