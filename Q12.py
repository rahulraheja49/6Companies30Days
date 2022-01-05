#User function Template for python3

class Solution:
    def squaresInChessBoard(self, N):
         # code here
         res = 0
         for i in range(1, N+1):
             res += i**2
         return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))
# } Driver Code Ends