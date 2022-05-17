#faster than 60% in python, for what it is worth
#problem:
#unsorted array, find smallest positive number NOT in it
# try to save in O(n)
# note: O(2n)= O(n) 

from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums):
        
        a = {}
        x = len(nums)
        for i in range(0,x):
            if nums[i]>0:
                a[nums[i]]=False
            #nums[:]= nums[1:]

        for j in range (1,x+1):
            if a.get(j) == None:
                return j
        return x+1
