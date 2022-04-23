class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
           a.sort()
           b.sort()
           suma = sum(a)
           sumb = sum(b)
           i=0
           j=0
           while (i<n and j<m):
               p = suma - a[i] + b[j]
               q = sumb - b[j] + a[i]
               if (p == q):
                   return 1
               if (p > q):
                   i+=1
               else:
                   j+=1
           return -1        

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends