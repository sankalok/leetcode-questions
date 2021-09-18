class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = [False]*len(l)
        
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            diff = []
            for j in range(1, len(arr)):
                diff.append(arr[j] - arr[j-1])
            if(diff.count(diff[0]) == len(diff)):
                result[i] = True
                
        return result
