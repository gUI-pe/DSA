class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numberSet = set()

        for n in nums:
            if n in numberSet:
                return True
            numberSet.add(n)
        return False
        