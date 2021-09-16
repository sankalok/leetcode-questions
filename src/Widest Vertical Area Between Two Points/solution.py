class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = []
        
        for i in range(0, len(points)):
                x_points.append(points[i][0])
        x_points.sort()
        
        if(len(x_points) == 1):
            return 0
        
        width = 0

        for i in range(1, len(x_points)):
            if((x_points[i] - x_points[i-1]) > width):
                width = x_points[i] - x_points[i-1]
            
        return width
