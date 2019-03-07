from heap import Heap
n = 1000000
from time import time

start_time1 = time()
heap = Heap()
from random import randint
for i in range(n):
    heap.add(randint(0, 1000))
print('heap add: ', time() - start_time1)