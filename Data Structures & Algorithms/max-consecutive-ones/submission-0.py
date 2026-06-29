class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOnes = 0
        maxOnes = 0
        for num in nums:
            if num == 1:
                countOnes += 1
            else:
                countOnes = 0
            
            if countOnes > maxOnes:
                maxOnes = countOnes
        
        return maxOnes
