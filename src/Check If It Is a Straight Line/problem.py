class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        c = 0
        for i in range(1, l):
            if(coordinates[i][0] == coordinates[i-1][0]):
                c += 1
        if(c == l - 1):
            return True
        l = len(coordinates)
        c = 0
        for i in range(1, l):
            if(coordinates[i][1] == coordinates[i-1][1]):
                c += 1
        if(c == l - 1):
            return True
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        if(x2-x1 == 0 or y2-y1 == 0):
            return False
        m = (y2 - y1)/(x2 - x1)
        c = y1 - (m * x1)
        for i in coordinates:
            x = i[0]
            y = i[1]
            if(y != (m*x + c)):
                return False
        return True
