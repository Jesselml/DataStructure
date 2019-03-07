from queue import Queue

queue = Queue()
#检测是否为空
print (queue.isEmpty())

#添加元素
for i in range(10):
    queue.enqueue(str(i**2))
print (queue.showQueue())

#返回队首元素
print (queue.getFront())

#删除队首元素
queue.dequeue()
print (queue.showQueue())

#检测是否为空
print (queue.isEmpty())

#反馈栈的大小
print (queue.getSize())