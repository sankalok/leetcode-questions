class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
        # code here 
    	
    	for i in range(0, n):
    	    if(matrix[i][0] <= x and matrix[i][m-1] >= x):
    	        for j in range(0, m):
    	            if(matrix[i][j] > x):
    	                break
    	            if(matrix[i][j] == x):
    	                return 1
    	return 0
