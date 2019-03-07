from insert_sort import insert_sort
from merge_sort import merge_sort
# from quick_sort import quick_sort
from select_sort import select_sort


nums = [1,24,6,2000,8,33,90,35,75,19,3,66,2,300,41,78]
print ("乱序元素：",nums)
nums1 = insert_sort(nums)
print ("插入排序：",nums1)
print ("--------------------------------------------------------------------------------")
nums = [1,24,6,2000,8,33,90,35,75,19,3,66,2,300,41,78]
print ("乱序元素：",nums)
nums2 = select_sort(nums)
print ("选择排序：",nums2)
print ("--------------------------------------------------------------------------------")
nums = [1,24,6,2000,8,33,90,35,75,19,3,66,2,300,41,78]
print ("乱序元素：",nums)
nums3 = merge_sort(nums)
print ("归并排序：",nums3)
print ("--------------------------------------------------------------------------------")
nums = [1,24,6,2000,8,33,90,35,75,19,3,66,2,300,41,78]
print ("乱序元素：",nums)
# nums4 = quick_sort(nums)
# print ("快速排序：",nums4)