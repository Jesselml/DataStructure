class Heap:
    def  __init__(self):
       self.__data = [0]
       self.__size = 0
    
    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size==0

    def __get_parent(self,index):
        return index//2
    
    def __get_left(self,index):
        return 2*index

    def __get_right(self,index):
        return 2*index+1
    
    def add(self,val):
        self.__data.append(val)
        self.__size +=1
        self.__sift_up(self.__size)
    
    def __sift_up(self,index):
        #如果父节点存在  且  父节点大于添加的节点  
        while self.__get_parent(index)>=1 and self.__data[self.__get_parent(index)] < self.__data[index]:
            empty = 0
            empty = self.__data[self.__get_parent(index)]
            self.__data[self.__get_parent(index)] = self.__data[index]
            self.__data[index] = empty
            index = self.__get_parent(index)
    
    def __find_max(self):
        return self.__data[1]
    
    def extract_max(self):
        max_val = self.__find_max()
        self.__data[1] = self.__data[self.__size]
        self.__data.pop()
        self.__sift_down(1)
        self.__size -=1
        return max_val
    
    def __sift_down(self,index):
        #首先找左右孩子的最大值，
        #如果有左孩子
        while self.__get_left(index) <= self.__size:
            j = self.__get_left(index)
            if self.__get_right(index) <= self.__size and self.__data[self.__get_left(index)] <= self.__data[self.__get_right(index)]:
                j = self.__get_right(index)
            #左右子的最大值小于当前节点
            if self.__data[j] < self.__data[index]:
                break
            empty = 0
            empty = self.__data[j]
            self.__data[j] = self.__data[index]
            self.__data[index] = empty
            index = j


            
            
            


        

        

    



