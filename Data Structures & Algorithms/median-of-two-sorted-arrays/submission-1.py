class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        s_nums = sorted(nums)

        low = 0
        high = len(s_nums) - 1

        mid =  low + (high - low) // 2

        if (high + 1) % 2 != 0:
            return s_nums[mid]
        else:
            return(s_nums[mid] + (s_nums[mid+1])) / 2
