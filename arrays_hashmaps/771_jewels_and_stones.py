class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel_list = set(jewels)
        for i in stones:
            if i in jewel_list:
                count += 1

        return count

