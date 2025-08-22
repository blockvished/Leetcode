class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s<=e:
            m = (s+e)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                e = m - 1
            else:
                s = m + 1
        return - 1

# made a mistake of not adding `=` in while loop makeing `[5]` testcase to fail
