class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        l = 0
        r = len(nums) -1
        p = len(nums) -1


        while l <= r:
            if nums[l]**2>nums[r]**2:
                result[p] = nums[l]**2
                l += 1
            else: 
                result[p] = nums[r]**2
                r -= 1
            p -= 1
        
        return result


