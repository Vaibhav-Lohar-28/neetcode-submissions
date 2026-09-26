class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkLimit(weights, cap):
            days_used = 1
            load = 0

            for weight in weights:

                if load + weight > cap:
                    days_used += 1
                    load = weight
                else:
                    load += weight

            return days_used

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = low + (high - low) // 2

            res = checkLimit(weights, mid)

            if res <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low