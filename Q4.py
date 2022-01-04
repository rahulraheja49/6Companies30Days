#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    output = ''
    i, j = 0, 0
    while i < len(arr):
        item = arr[i]
        j = i+1
        while j<len(arr) and arr[j] == arr[i]:
            j+=1
        string = ''+item+''+str(j-i)
        output+= string
        i=j
    return output

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends