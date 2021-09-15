class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        
        counter = 1
        counterMax = max(groupSizes)
        while(counter <= counterMax):
            indexes = []
            for i in range(0, len(groupSizes)):
                if(groupSizes[i] == counter):
                    indexes.append(i)
            groups.append(indexes)
            counter += 1 
        
        subgroups = []
        for i in range(0, len(groups)):
            size = i + 1
            noGroups = len(groups[i]) // size
            count = 0
            while(count < len(groups[i])):
                subgroups.append(groups[i][count:count+size])
                count = count + size
                
        return subgroups
