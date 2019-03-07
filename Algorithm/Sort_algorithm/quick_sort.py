def quick_sort(nums):
    if len(nums)<=0:
        return nums
    p = partition(nums)
    nums[:p] = quick_sort(nums[:p])
    nums[p+1:] = quick_sort(nums[p+1:])
    return nums

def partition(nums):
    v = nums[0]
    j = 0
    for i in range(1,len(nums)):
        if nums[i] < v:
            empty = nums[i]
            nums[i] = nums[j+1]
            nums[j+1] = empty
            j+=1
    empty = nums[j]
    nums[j] = nums[0]
    nums[0] = empty
    return j

def quick_sort2(nums):
    if len(nums)<=0:
        return nums
    p = partition2(nums)
    nums[:p] = quick_sort(nums[:p])
    nums[p+1:] = quick_sort(nums[p+1:])
    return nums

def partition2(nums):
    v = nums[0]
    i = 1
    j = len(nums)-1
    while True:
        while nums[i] < v and i <= len(nums)-1: i+=1
        while nums[j] > v and j >= 0: j-=1
        if i > j: break
        empty = nums[i]
        nums[i] = nums[j]
        nums[j] = empty
    return j
            
        

