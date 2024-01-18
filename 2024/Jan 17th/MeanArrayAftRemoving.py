# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)    
        if len(arr) > 0:
            x = int((5/100)*len(arr))
            arr = arr[x:-x]
        return mean(arr)