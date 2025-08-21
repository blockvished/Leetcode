class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        map = {}
        result = 0

        for num in nums:
            map[num] = 1 + map.get(num, 0)

            if map[num] > max_count:
                result = num
                max_count = map[num]
        
        return 
        

# alt solution
# increments the count and decrement if different number but if the count gets to 0 then new number has broken equilibrium and should be the appearing more times so that is result

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count +=1
            else:
                count -=1
        return result