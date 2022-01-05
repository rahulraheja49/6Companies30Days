def lastPosition(n, m, k):
    if (m <= n - k + 1):
       return m + k - 1
 
    m = m - (n - k + 1)
 
    if(m % n == 0):
        return n
    else:
        return m % n
 
# Driver code
n = 5
m = 8
k = 2
print(lastPosition(n, m, k))
