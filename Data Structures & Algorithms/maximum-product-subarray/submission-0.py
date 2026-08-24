class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMax = 1
        curMin = 1
        res = nums[0]

        for i in nums:
            temp = curMax * i
            curMax = max(i*curMax,i*curMin, i)
            curMin = min(temp, i*curMin, i)
            res = max(res, curMax)

        return res
        