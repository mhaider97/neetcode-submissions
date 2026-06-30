class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newCapacity = 2 * len(nums)
        ansArr = [0] * newCapacity

        for i in range(len(nums)):
            ansArr[i], ansArr[i+len(nums)] = nums[i], nums[i]
        
        return ansArr
        