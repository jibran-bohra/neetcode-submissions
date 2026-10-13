class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{":"}","(":")","[":"]"}

        stack = []

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            
            else:
                if not stack:
                    return False

                top = stack.pop()

                if char != pairs[top]:
                    return False
        
        if len(stack) > 0:
            return False
            
        return True