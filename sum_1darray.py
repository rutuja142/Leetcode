"""1480. Running Sum of 1d Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums."""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        n=len(nums)
        ans=[]
        ans.append(nums[0])

        for i in range(1,n):
            x=ans[i-1]+nums[i]
            ans.append(x)

        return ans
        