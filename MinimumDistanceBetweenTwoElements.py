

class Solution:
    def minDist(self, arr, n, x, y):
       if int(x) not in arr:return -1
       if int(y) not in arr: return -1
       else:
           b=[i for i in range(len(arr)) if arr[i]==x]
           c=[i for i in range(len(arr)) if arr[i]==y]
           f=[]
           for i in c:
               for j in b:
                   f.append(abs(i-j))
           return min(f)        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends