class Linkedlist():
    class __Node():
        def __init__(self,val,node):
            self.data = val
            self.next = node

    def __init__(self):
        self.__dummyHead = self.__Node(None,None)
        self.__size = 0
    
    def isEmpty(self):
        return self.__size == 0
    
    def getSize(self):
        return self.__size

    def remove(self,index):
        if index<0 and index>self.__size-1:
            return ("Failed")

        prev = self.__dummyHead
        for i in range(index):
            prev = prev.next
        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None

        self.__size -=1

    def removeFirst(self):
        self.remove(0)

    def removeLast(self):
        self.remove(self.__size)

    def add(self,index,val):
        if index<0 and index>self.__size-1:
            return ("Failed")

        prev = self.__dummyHead
        for i in range(index):
            prev = prev.next        
        # node_insert = self.__Node(val,None)
        # node_insert.next = prev.next
        # prev.next = node_insert
        prev.next = self.__Node(val,prev.next)
        self.__size +=1
    
    def addFirst(self,val):
        self.add(0,val)

    def addLast(self,val):
        self.add(self.__size,val)

    def showLinkedlist(self):
        l = []
        cur = self.__dummyHead.next
        while cur != None:
            l.append(str(cur.data))
            cur = cur.next
        return "Linkedlist:Head-"+",".join(l)+"-Tail"
    
    def getVal(self,index):
        if index<0 and index>self.__size-1:
            return ("Failed")

        cur = self.__dummyHead
        for i in range(0,index+1):
            cur = cur.next
        
        return cur.data
    
    def setVal(self,index,val):
        if index<0 and index>self.__size-1:
            return ("Failed")

        cur = self.__dummyHead
        for i in range(0,index+1):
            cur = cur.next
        cur.data = val


    
        

            




