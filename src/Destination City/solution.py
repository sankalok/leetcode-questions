class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        if(len(paths) == 1):
            return paths[0][1]
        
        origin = paths[0][1]
        count = 1
        while(count < len(paths)):
            for i in range(1, len(paths)):
                if(origin == paths[i][0]):
                    origin = paths[i][1]
                    break
            count += 1
            
        destination = origin
        return destination
                    
