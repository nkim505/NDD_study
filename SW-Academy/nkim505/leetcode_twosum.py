class Solution(object):
    from copy import deepcopy
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            y = target - nums[i]
            new_list = deepcopy(nums)
            new_list.pop(i)
            if y in new_list:
                output += [i]
                output += [new_list.index(y)+1]
                return output
            else:
                pass
            
