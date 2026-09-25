class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        duplicat = nums.copy()
        return nums + duplicat
        