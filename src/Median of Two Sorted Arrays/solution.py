class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        mid = len(nums1)/2
        if(len(nums1) % 2 == 1):
            return (float(nums1[mid]))
        else:
            return (float(nums1[mid-1]) + float(nums1[mid]))/2
