class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        seen = {}

        for index,num in enumerate(nums):
            remainder = target - num 
    
            if remainder in seen:
                ans = [seen[remainder], index]
                break
    
            seen[num] = index
        return ans