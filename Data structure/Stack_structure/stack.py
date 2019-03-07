class Stack():
    def __init__(self):
        self.__stack = []
        self.__size = 0
    
    def push(self,e):
        self.__stack.append(e)
        self.__size+=1

    def pop(self):
        
        return self.__stack.pop()
        

    def peek(self):
        return self.__stack[-1]

    def getSize(self):
        return len(self.__stack)

    def isEmpty(self):
        return self.__stack==[]
    
    def showStack(self):
        return "Stack: ",self.__stack

    
