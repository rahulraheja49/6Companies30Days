#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        if n==1:
            if a[0]<k:
                return 1
            else:
                return 0
        
        product = 1
        i, j, count = 0, 0, 0
        while j<n:
            product *= a[j]
            while product>=k and i<=j:
                product/=a[i]
                i+=1
            count+=(j-i+1)
            j+=1
        return count
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends