def insert_sort(nums):
    for i in range(len(nums)):
        current_num = nums[i]
        for j in range(i,0,-1):
            if current_num < nums[j-1]:
                nums[j] = nums[j-1]
            else:
                nums[j] = current_num
                break
    return nums