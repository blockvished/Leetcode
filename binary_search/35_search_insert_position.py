class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (s+e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = s+1
            else:
                e = m-1
        return e+1


# took tinkering for multiple tries but ez as before
# just figured that we can return start as well since in the end the start and end pointers will be adjacent but end will be before start
# e, s -> instead of adding 1 to e, we can directly return s
