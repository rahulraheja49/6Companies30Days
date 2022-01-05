#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        stack = []
        num = 1
        res = ''
        
        for i in S:
            if i=="D":
                stack.append(num)
                num+=1
            else:
                stack.append(num)
                num+=1
                while len(stack) > 0:
                    res += str(stack.pop())
        stack.append(num)
        while len(stack) > 0:
            res += str(stack.pop())
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends