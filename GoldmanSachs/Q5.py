#User function Template for python3
class Solution:
    def getNthUglyNo(self,n):
        # code here
        i2, i3, i5 = 0, 0, 0
        ugly = [0]*(n+1)
        ugly[0] = 1
        next_ugly = 1
        num2, num3, num5 = 2, 3, 5
        for i in range(1, n):
            next_ugly = min(num2, num3, num5)
            ugly[i] = next_ugly
            if next_ugly == num2:
                i2+=1
                num2 = ugly[i2]*2
            if next_ugly == num3:
                i3+=1
                num3 = ugly[i3]*3
            if next_ugly == num5:
                i5+=1
                num5 = ugly[i5]*5
        return next_ugly
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends