class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = []
        for i in sentence:
            l.append(i)
        l = list(set(l))
        if(len(l) == 26):
            return True
        else:
            return False
