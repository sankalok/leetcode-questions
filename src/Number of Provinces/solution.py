class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = dict()
        if(isConnected[0].count(1) == len(isConnected)):
            return 1
        for i in range(len(isConnected)):
            emptyList = []
            for j in range(len(isConnected)):
                if(isConnected[i][j] == 1):
                    emptyList.append(j+1)
            cities[i+1] = emptyList
        
        count = 1
        while(count < len(isConnected)):
            temp = dict(cities)
            for i in range(1, len(isConnected)+1):
                for j in range(1, len(isConnected)+1):
                    if(i in cities[j]):
                        cities[i].extend(cities[j])
                        cities[i] = list(set(cities[i]))
                        cities[i].sort()
                if(len(cities[i]) == len(isConnected)):
                    return 1
            count += 1
            if(cities == temp):
                break
        cityLists = []
        for i in range(1, len(isConnected)+1):
            cityLists.append(cities[i])
        uniqueCityLists = [cityLists[0]]
        for i in range(1, len(cityLists)):
            if cityLists[i] not in uniqueCityLists:
                uniqueCityLists.append(cityLists[i])
        return(len(uniqueCityLists))
        
                        
                
