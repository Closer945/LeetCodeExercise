class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            x = target - nums[i]
            for j in range(1, lens-i):
                if nums[j+i]==x:
                    return [i, j+i]
        return
