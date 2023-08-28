class Solution(object):
    def isValid(self, s):
        if(len(s)==1):
            return False
        open = ['(','{','[']
        close = [')','}',']']
        stack=[]
        j=0
        check = False
        for i in s:
            j+=1
            if i in close:
                if stack==[]:
                    return False
                elif open[close.index(i)] == stack[-1]:
                    stack.pop()
                    check = True
                else:
                    return False
            else:
                check=False
                stack.append(i)
            if(j == len(s)):
                if(stack!=[]):
                    check = False
                return check