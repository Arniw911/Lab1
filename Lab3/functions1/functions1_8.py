def spy_game(nums):
    has007 = False
    for i in range(2, len(nums)): 
        if nums[i] == 7 and nums[i - 1] == 0 and nums[i - 2] == 0:
            has007 = True
    return has007
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))