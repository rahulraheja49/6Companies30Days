#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        word_dictionary = dict()
        for i in words:
            word = ''.join(sorted(i))
            if word_dictionary.get(word, 0) == 0:
                word_dictionary[word] = [i]
            else:
                word_dictionary[word].append(i)
        result = []
        for i in word_dictionary:
            result.append(word_dictionary[i])
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends