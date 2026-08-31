class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token=="+" or token=="-" or token=="*" or token=="/":
                first_num=stack.pop()
                second_num=stack.pop()
                if token=="+":
                    stack.append(int(second_num + first_num))
                else:
                    if token=="-":
                        stack.append(int(second_num - first_num))
                    else:
                        if token=="*":
                            stack.append(int(second_num * first_num))
                        else:
                            stack.append(int(second_num / first_num))
            else:
                stack.append(int(token))
        
        return stack[-1]