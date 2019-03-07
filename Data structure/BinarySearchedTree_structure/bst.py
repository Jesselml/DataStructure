class BST():
    class __Node():
        def __init__(self,val):
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

    def add1(self,e):
        if self.__root == None:
            self.__root = self.__Node(e)
            self.__size+=1
        else:
            self.__add1(self.__root,e)
        
        #以下这么写，通过在递归函数里判断node是否为空的写法是不对的，因为如果为空，赋值给Node的时候，Node会直接指向空内存，从而失去和树的连接
        #所以如果这么写，必须采用方式二的方法，直接将改变的地址接住，然后返回
        # self.__add1(self.__root,e)

    #插入递归 方式一: 向以node为根节点的的BST插入元素
    def __add1(self,node,e):
        if e == node.val:
            return
        #e < node.val
        elif e < node.val:
            if node.left == None:
                node.left = self.__Node(e)
                self.__size +=1
                return 
            else:
                self.__add1(node.left,e)
        #e > node.val
        else:
            if node.right == None:
                node.right = self.__Node(e)
                self.__size +=1
                return 
            else:
                self.__add1(node.right,e)

    def add2(self,e):
        self.__root = self.__add2(self.__root,e)
        
    #插入递归 方式二: 返回以node为根的添加好元素的BST的根节点
    def __add2(self,node,e):
        if node == None:
            node = self.__Node(e)
            self.__size +=1
            return node
        else:
            if e == node.val:
                return node
            #e < node.val
            elif e < node.val:
                node.left = self.__add2(node.left,e)
                return node
            #e > node.val
            else:
                node.right = self.__add2(node.right,e)
                return node

    def contains(self,e):
        return self.__contains(self.__root,e)
        
    #查询递归 在以node为根节点的的BST中查找是否存在元素e
    def __contains(self,node,e):
        if node == None:
            return False
        else:
            if node.val == e:
                return True
            elif node.val > e:
                return self.__contains(node.left,e)
            else:
                return self.__contains(node.right,e)

    def pre_order(self):
        self.__pre_order(self.__root)
        
    #前序遍历递归 在以node为根节点的的BST中前序遍历
    def __pre_order(self,node):
        if node == None:
            return
        else:
            print (node.val)
            self.__pre_order(node.left)
            self.__pre_order(node.right)

    def in_order(self):
        self.__in_order(self.__root)

    #中序遍历递归 在以node为根节点的的BST中中序遍历
    def __in_order(self,node):
        if node == None:
            return
        else:
            self.__in_order(node.left)
            print (node.val)
            self.__in_order(node.right)
            
    def post_order(self):
        self.__post_order(self.__root)

    #后序遍历递归 在以node为根节点的的BST中后序遍历
    def __post_order(self,node):
        if node == None:
            return
        else:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print (node.val)
    
    #层级遍历/广度优先遍历 非递归
    def level_order(self):
        queue = []
        if self.__root == None:
            return 
        else:
            queue.append(self.__root)
            while len(queue) != 0:
                #出队 - 遍历 - 俩孩子入队
                cur = queue.pop(0)
                print (cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
    
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

    def remove_max(self):
        maximum = self.maximum()
        self.__root = self.__remove_max(self.__root)
        return maximum

    #删除最大值 递归 删除以Node为根的BST的最大值
    def __remove_max(self,node):
        if node == None:
            return node
        else:
            #如果已经最右了，就是删除这个点
            if node.right == None:
                if node.left == None:
                    node = None
                    self.__size -=1
                    return node
                else:
                    left_node = node.left
                    node.left = None
                    self.__size -=1
                    return left_node
            else:
                node.right = self.__remove_max(node.right)
                return node
        
    def minimum(self):
        if self.__size != 0:
            minimum = self.__minimum(self.__root)
        return minimum
    
    def __minimum(self,node):
        if node.left == None:
            return node
        return self.__minimum(node.left)

    def maximum(self):
        if self.__size != 0:
            maximum = self.__maximum(self.__root)
        return maximum
    
    def __maximum(self,node):
        if node.right == None:
            return node
        return self.__maximum(node.right)

    def remove(self,e):
        self.__root = self.__remove(self.__root,e)

    #递归返回删除了以Node为根节点的BST中的元素e
    def __remove(self,node,e):
        if node == None:
            return 
        if e < node.val:
            node.left = self.__remove(node.left,e)
            return node
        elif e > node.val:
            node.right = self.__remove(node.right,e)
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
   