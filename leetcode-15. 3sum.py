def threeSum(self, nums):
    out = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            print(i) 
            print(a)
            continue
        l, r = i + 1, len(nums)-1
        while l<r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                out.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return out
print(threeSum(1, [-1, 0, 1, 2, -1, -4]))

    
    

    
    # out = [] 
    # for i in range(0, len(nums)):
    #     for j in range(1, len(nums)):
    #         for k in range(2, len(nums)):
    #             if nums[i] + nums[j] + nums[k] == 0 and nums[i] != nums[j] != nums[k]:
    #                 out.append([nums[i], nums[j], nums[k]])
    # for x in range(0, len(out)):
    #     out[x]
    # return out



# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
