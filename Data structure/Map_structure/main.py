from map import Map

bst_map = Map()

words = ''
with open('shakespeare.txt', 'r') as f:
    words = f.read()
words = words.split()

from time import time
start_time = time()

for word in words:
    if bst_map.contains(word):
        bst_map.set_val(word,bst_map.get_val(word)+1)
    else:
        bst_map.add(word,0)

print('Total words: ', len(words))
print('Unique words: ', bst_map.get_size())
print('Contains word "they": ', bst_map.contains('they'))
print('Total time: {} seconds'.format(time() - start_time))

# rt = {}
# for word in words:
#     if word in rt:
#         rt[word] = rt[word] + 1
#     else:
#         rt[word] = 1

# print('Total words: ', len(words))
# print('Unique words: ', len(rt))
# print('Total time: {} seconds'.format(time() - start_time))

# m = {}
# for i in rt:
#     if 100 < rt[i]:
#         m[i] =  rt[i]
# print (m)

