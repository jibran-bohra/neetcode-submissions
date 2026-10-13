from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_key(s):
            count = [0]*26 #letters of the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            return tuple(count)
        
        groups = defaultdict(list)

        for s in strs:
            key = get_key(s)
            groups[key].append(s)
        
        return list(groups.values())