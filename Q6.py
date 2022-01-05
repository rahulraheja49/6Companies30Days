class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pre = []
        s = ''
        for i in range(0,len(str1)):
            s += str1[i] # everytime increasing s by 1 letter
            if s*(len(str1)//len(s)) == str1 and  s*(len(str2)//len(s)) == str2:
                pre.append(s)
        if len(pre) == 0:
            return ""
        return pre[-1]