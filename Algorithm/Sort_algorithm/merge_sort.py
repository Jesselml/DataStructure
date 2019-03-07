def merge_sort(nums):
    #第一步 分
    if len(nums) == 1:
        return nums
    mid = (len(nums))//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left,right)

def merge(left,right):
    #第二部 合并
    empty_nums = left+right
    i = j = 0
    for index in range(len(empty_nums)):
        if i == len(left):
            empty_nums[index] = right[j]
            j+=1
        elif j == len(right):
            empty_nums[index] = left[i]
            i+=1
        elif left[i] < right[j]:
            empty_nums[index] = left[i]
            i+=1
        elif left[i] > right[j]:
            empty_nums[index] = right[j]
            j+=1
    return empty_nums