class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElem = max(arr[1:], default=-1)
        for i in range(len(arr)):
            if arr[i] == maxElem:
                maxElem = max(arr[i+1:], default=0)
                arr[i] = maxElem
            elif arr[i] != maxElem:
                arr[i] = maxElem
        
        arr[-1] = -1
        
        return arr
            
