#User function Template for python3

class Solution:
    def decodedString(self, s):
        stack1 = []
        stack2 = []
        temp = ""
        res = ""
        i = 0
        while i < len(s):
            count = 0
            if (s[i]>='0' and s[i]<='9'):
                while (s[i]>='0' and s[i]<='9'):
                    count = count * 10 + ord(s[i]) - ord('0')
                    i+=1
                i-=1
                stack1.append(count)
            elif (s[i] == ']'):
                temp = ""
                count = 0
                if (len(stack1) != 0):
                    count = stack1[-1]
                    stack1.pop()
                while (len(stack2) != 0 and stack2[-1] !='[' ):
                    temp = stack2[-1] + temp
                    stack2.pop()
                if (len(stack2) != 0 and stack2[-1] == '['):
                    stack2.pop()
                for j in range(count):
                    res = res + temp
                for j in range(len(res)):
                    stack2.append(res[j])
                res = ""
            elif (s[i] == '['):
                if (s[i-1]>='0' and s[i-1]<='9'):
                    stack2.append(s[i])
                else:
                    stack2.append(s[i])
                    stack1.append(1)
            else:
                stack2.append(s[i])
             
            i += 1
        while len(stack2) != 0:
            res = stack2[-1] + res
            stack2.pop()
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends