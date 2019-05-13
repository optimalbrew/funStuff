"""
Find indices of pairs of elements in a list that sum to a given target
"""

def twoSum(nums, target):
    sol=[]
    i,j=0,1
    while i < len(nums)-1:
        j=i+1                
        while j < len(nums):
            if nums[i]+nums[j]==target:
                #print(i,j)
                sol.append((i,j))
            j+=1
        i+=1        
    return sol

#simple test
nums = [1,2,3,4,2]
target = 5

twoSum(nums,target) 

"""
This approach is O(n^2). Can speed it up by using hash tables to keep track of where elements are (indices)
"""


"""
This approach does not find all, but is faster, uses a dict
"""
def twoSum(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i