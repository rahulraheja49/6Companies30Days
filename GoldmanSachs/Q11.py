#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        num = [0]*(n+1)
        num[0] = 1
        for i in arr:
            num[i]+=1
        repeated = num.index(2)
        missing = num.index(0)
        return repeated, missing

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends