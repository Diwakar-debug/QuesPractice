#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        freq={}
        count=0
        for i in arr:
           diff=k-i
           if diff in freq:
               count=count+freq[diff]
           if i in freq:
               freq[i]=freq[i]+1
           else:
               freq[i]=1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends