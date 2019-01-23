class BSTMap():
    class __Node():
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
    
    def __init__(self):
        self.__root = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def add(self,key,val):
        self.__root = self.__add(self.__root,key,val)
        
    #插入递归 返回以node为根的添加好元素的BST的根节点
    def __add(self,node,key,val):
        if node == None:
            node = self.__Node(key,val)
            self.__size +=1
            return node
        else:
            if key == node.key:
                return node
            elif key < node.key:
                node.left = self.__add(node.left,key,val)
                return node
            else:
                node.right = self.__add(node.right,key,val)
                return node

    def contains(self,key):
        return self.__contains(self.__root,key)
        
    #查询递归 在以node为根节点的的BST中查找是否存在元素e
    def __contains(self,node,key):
        if node == None:
            return False
        else:
            if node.key == key:
                return True
            elif node.key > key:
                return self.__contains(node.left,key)
            else:
                return self.__contains(node.right,key)
    
    def get_val(self,key):
        return self.__get_val(self.__root,key)
        
    def __get_val(self,node,key):
        if node == None:
            return
        else:
            if node.key == key:
                return node.val
            elif node.key > key:
                return self.__get_val(node.left,key)
            else:
                return self.__get_val(node.right,key)

    def set_val(self,key,val):
        self.__set_val(self.__root,key,val)
        
    def __set_val(self,node,key,val):
        if node:
            if node.key == key:
                node.val = val
            elif node.key > key:
                self.__set_val(node.left,key,val)
            else:
                self.__set_val(node.right,key,val)
    
    def remove_min(self):
        minimum = self.minimum()
        self.__root = self.__remove_min(self.__root)

        return minimum

    #删除最小值 递归 删除以Node为根的BST的最小值
    def __remove_min(self,node):
        if node == None:
            return node
        else:
            #如果已经最左了，就是删除这个点
            if node.left == None:
                if node.right == None:
                    node = None
                    self.__size -=1
                    return node
                else:
                    right_node = node.right
                    node.right = None
                    self.__size -=1
                    return right_node
            else:
                node.left = self.__remove_min(node.left)
                return node
        
    def minimum(self):
        if self.__size != 0:
            minimum = self.__minimum(self.__root)
        return minimum
    
    def __minimum(self,node):
        if node.left == None:
            return node
        return self.__minimum(node.left)

    def remove(self,key):
        self.__root = self.__remove(self.__root,key)

    #递归返回删除了以Node为根节点的BST中的元素e
    def __remove(self,node,key):
        if node == None:
            return 
        if key < node.key:
            node.left = self.__remove(node.left,key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right,key)
            return node
        #找到了要删除的元素
        else:
            if node.left == None:
                right_node = node.right
                node.right = None
                self.__size -=1
                return right_node
            if node.right == None:
                left_node = node.left
                node.left = None
                self.__size -=1
                return left_node
            
            successor = self.__minimum(node.right)
            successor.right = self.__remove_min(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor
   