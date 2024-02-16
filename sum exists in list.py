# sum exists in list

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return None
        dct = dict()
        for i,c in enumerate(nums):
            new = target - c
            if new in dct:
                return (dct[new], i)
            dct[c] = i
        return []


