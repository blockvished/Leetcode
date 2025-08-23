class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        k_sum = 0

        for i in range(k):
            k_sum += nums[i]
        max_avg = k_sum/k

        for i in range(k,len(nums)):
            k_sum += nums[i]
            k_sum -= nums[i-k]
            max_avg = max(max_avg,k_sum/k)


        return max_avg

# got an intuition but was wrong so had to watch the video for intuition, then stuck and solved by semi cheating