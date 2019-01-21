from set import Set

bst_set = Set()

words = ''
with open('shakespeare.txt', 'r') as f:
    words = f.read()
words = words.split()

from time import time
start_time = time()

for word in words:
        bst_set.add(word)

print('Total words: ', len(words))
print('Unique words: ', bst_set.get_size())
print('Contains word "they": ', bst_set.contains('big'))
print('Total time: {} seconds'.format(time() - start_time))