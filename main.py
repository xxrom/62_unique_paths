class Solution:

  def uniquePaths(self, m: int, n: int) -> int:
    arr = []

    # fill left side with 1 - only one possible way here
    for i in range(m):
      arr.append([1])

    # fill top side with 1 - only one possible way here
    for j in range(n):
      arr[0].append(1)

    # print(arr)

    for i in range(1, m):
      for j in range(1, n):
        arr[i].append(arr[i - 1][j] + arr[i][j - 1])

    # print(arr)

    return arr[m - 1][n - 1]


my = Solution()
m = 7
n = 3
ans = my.uniquePaths(m, n)
goal_ans = 28
print("ans: is correct ? - %s /" % str(ans == goal_ans), ans)
'''
top and left fill with 1
from 1,1 go and sum left and top numbers

0 1 1 1
1 2 3 4
1 3 6 10
'''

# Runtime: 32 ms, faster than 50.44% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.1 MB, less than 5.77% of Python3 online submissions for Unique Paths.
# Runtime: 28 ms, faster than 77.97% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 5.77% of Python3 online submissions for Unique Paths.
# Runtime: 24 ms, faster than 93.24% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.6 MB, less than 5.77% of Python3 online submissions for Unique Paths.