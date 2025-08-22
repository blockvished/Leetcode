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

# wasnt sure if it could be solved with bs but figured after looking at editorial title
# so solving without looking at solution of code

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 0
        e = num

        while s <= e:
            m = (s+e)//2

            if m*m == num:
                return True
            elif m*m > num:
                e = m-1
            else:
                s = m+1
        return False
