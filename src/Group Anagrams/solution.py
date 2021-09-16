from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #code here
        

        group = defaultdict(list)

        for word in words:
            group["".join(sorted(word))].append(word)

        result = []

        for key in group.keys():
            result.append(group[key])
        
        return result
