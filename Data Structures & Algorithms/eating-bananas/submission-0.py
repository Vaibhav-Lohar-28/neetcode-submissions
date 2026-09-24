class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHours(piles,hours):
            total_h = 0
            for i in piles:
                total_h += math.ceil(i / hours)
            return total_h

        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            total_h = totalHours(piles,mid)
            
            if total_h <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        