from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack=deque()

        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            else:
                if (stack[-1]=="(" and s[i]==")") or (stack[-1]=="[" and s[i]=="]") or (stack[-1]=="{" and s[i]=="}"):
                    stack.pop()
                else:
                    stack.append(s[i])
            print(stack)
        
        if not stack:
            return True
        else:
            return False