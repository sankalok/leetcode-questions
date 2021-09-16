class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k != 0 and len(nums) >= 2):
            if(k > len(nums)):
                k = k % len(nums)
            result = [0]*len(nums)
            if(len(nums) > 1 or k > 0):
                count = 0
                for i in range(0, len(nums)):
                    position = i + k
                    if(position > len(nums) - 1):
                        position = i + k - len(nums)
                        result[position] = nums[i]
                    else:
                        result[position] = nums[i]     
            nums[:] = result[:]
            
