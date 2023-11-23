# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s = set(arr)
        m = -1
        if len(s) == 1 and arr[0] in s and arr[0] == len(arr):
            return arr[0]
        for i in range(1, len(s)+1):
            if i == arr.count(i):
                m = i
        return m
    
# Optimized but long run time

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = -1
        for i in range(1, len(arr)+1):
            j = arr.count(i)
            if j == i:
                m = i
        return m
    
# Optimized using dictionary

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        m = -1
        for n, c in d.items():
            if n == c:
                m = max(m, n)
        return m       