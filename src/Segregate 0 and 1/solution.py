class Solution:
    def segregate0and1(self, arr, n):
        # code here
        no0 = arr.count(0)
        no1 = arr.count(1)
        arr[:] = [0]*no0 + [1]*no1
