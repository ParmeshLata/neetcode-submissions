#from collections import queue
class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        for char in s:
            if len(stack)==0:
                stack.append(char)
            else:
                if (stack[-1]=="(" and char==")") or (stack[-1]=="[" and char=="]") or (stack[-1]=="{" and char=="}"):
                    stack.pop()
                else:
                    stack.append(char)
        
        if not stack:
            return True
        else:
            return False