class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            for letter in set(s):
                count  = s.count(letter) - t.count(letter)

                if count !=0:
                    return False
            
            return True
        
        return False