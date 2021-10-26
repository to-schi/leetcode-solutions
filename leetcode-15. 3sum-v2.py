def threeSum(self, nums):
    out = []
    nums.sort()
    for i in range(0, len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]: # duplicate skipped!
            continue
        # value of a is negative value at index i, because requirement -nums[i] == nums[j] + nums[k]
        a = -nums[i]    
        j = i + 1   # left-pointer "j" must me 1 higher than i
        k = len(nums)    # right pointer starts at last index-position

        while j < k:    # left pointer not higher than right pointer
            if nums[j]+nums[k] < a: # as long as requirement is not met, increase left pointer
                j += 1
            elif nums[j]+nums[k] > a:  # as long as requirement is not met, decrease right pointer
                k -= 1
    # if requirement is met: -nums[i] == nums[j] + nums[k], append and continue with increase left and decrease right
            else:   
                if [-a, nums[j], nums[k]] not in out:
                    out.append([-a, nums[j], nums[k]])
                j += 1
                k -= 1
    return out
print(threeSum(1, [-1, 0, 1, 2, -1, -4]))


