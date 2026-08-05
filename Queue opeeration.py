from collections import deque

class Solution:

    def insert(self, q, k):
        q.append(k)

    def findFrequency(self, q, k):
        count = q.count(k)
        if count == 0:
            return -1
        return count


# Driver Code
q = deque()
sol = Solution()

# Input
n = int(input())

# Insert elements
arr = list(map(int, input().split()))
for i in arr:
    sol.insert(q, i)

# Number of queries
m = int(input())

# Elements to find frequency
find = list(map(int, input().split()))

for x in find:
    print(sol.findFrequency(q, x))