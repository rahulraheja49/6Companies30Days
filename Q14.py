class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                res = min(res, i+1-left)
                curr_sum -= nums[left]
                left+=1
        return res if res != float('inf') else 0