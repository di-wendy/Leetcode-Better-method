class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if (count == 0):
                result = nums[i]
                count = 1
            else:
                if (nums[i]==result):
                    count = count +1
                else:
                    count = count -1
        return result
