def has_33(nums):
    has33 = False
    for i in range(1, len(nums)): 
        if nums[i] == 3 and nums[i - 1] == 3:
            has33 = True
    return has33
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))