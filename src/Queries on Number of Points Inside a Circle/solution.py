class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        qP = []
        for q in queries:
            count = 0
            for p in points:
                if(sqrt(pow(q[0] - p[0],2) + pow(q[1] - p[1], 2)) <= float(q[2])):
                    count += 1
            qP.append(count)
        return qP
