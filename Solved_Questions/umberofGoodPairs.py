# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.



class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
