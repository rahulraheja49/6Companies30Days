#User function Template for python3

class Solution:
    def canPair(self, nuns, k):
        # Code here
        arr = [0]*k
        for i in nuns:
            arr[i%k]+=1
        if arr[0]%2 != 0:
            return False
        for i in range(1, len(arr)):
            if arr[i] != arr[k-i]:
                return False
        return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends