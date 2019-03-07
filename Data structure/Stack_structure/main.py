from stack import Stack

stack = Stack()
#检测是否为空
print (stack.isEmpty())

#添加元素
for i in range(10):
    stack.push(str(i))
print (stack.showStack())

#删除栈顶元素
stack.pop()
print (stack.showStack())

#检测是否为空
print (stack.isEmpty())

#反馈栈的大小
print (stack.getSize())