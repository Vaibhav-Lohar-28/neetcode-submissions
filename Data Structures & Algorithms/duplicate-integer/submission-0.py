class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        duplicate = set()

        for i in nums:
            if i in hashmap:
                duplicate.add(i)
            else:
                hashmap.add(i)
        if duplicate:
            return True
        else:
            return False
        