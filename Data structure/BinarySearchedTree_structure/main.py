from bst import BST
bst_tree = BST()
nums = [5, 3, 5,11,6, 100, 2000,4, 2, 2]
for num in nums:
    bst_tree.add1(num)
print ("新生成的BST如下")
bst_tree.in_order()
print ("元素个数为",bst_tree.get_size())
print (bst_tree.contains(9))

minimum = bst_tree.remove_min()
print ("要删除的最小值元素为:",minimum.val)
print ("删除最小值的BST如下")
bst_tree.in_order()
print ("元素个数为",bst_tree.get_size())

maximum = bst_tree.remove_max()
print ("要删除的最大值元素为:",maximum.val)
print ("删除最大值的BST如下")
bst_tree.in_order()
print ("元素个数为",bst_tree.get_size())

print ("删除元素6")
bst_tree.remove(6)
print ("删除元素6后的BST如下")
bst_tree.in_order()

