"""905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition."""
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        start=0

        for i in range(n):
            if nums[i]%2==0:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1

        return nums
