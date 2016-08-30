class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first = 0
        second = 0
        xor = reduce(lambda x, y: x ^ y, nums)
        
        print xor
        xor &= -xor
        print -xor
        for num in nums:
            if num & xor == 0:
                first ^= num
            else:
                second ^= num
        
        return [first, second]
