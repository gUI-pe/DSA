class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(n) time, O(n) space using a hash set.
        
        Key insight: Only start counting from the BEGINNING of a sequence.
        A number is the start of a sequence if (num - 1) is NOT in the set.
        Then expand forward while (num + 1) exists.
        """
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1
                
                # Expand forward
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest