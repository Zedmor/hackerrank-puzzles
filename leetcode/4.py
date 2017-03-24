"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Subscribe to see which companies asked this question.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        hyp1 = len(nums1) // 2
        hyp2 = len(nums2) // 2
        print(nums1[hyp1], nums2[hyp2])
        if nums1[hyp1] < nums2[hyp2]:
            if nums1[hyp1] > nums2[hyp2-1]:
                return (nums1[hyp1] + nums2[hyp2]) /2



nums1 = [1, 2, 9]
nums2 = [4, 6, 8, 10,13]

print(Solution().findMedianSortedArrays(nums1, nums2))
