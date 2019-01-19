from bst import BST

bst = BST()
nums = [5, 3, 6, 8, 4, 2, 2]
for num in nums:
    bst.add2(num)

bst.pre_order()

print (bst.get_size())