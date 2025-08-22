class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num):
            if i*i == num:
                return True
            if i*i > num:
                return False

# failed 1 edge case when num = 1, the loop runs only once
# so solves it^
```
for i in range(num+1):
```
