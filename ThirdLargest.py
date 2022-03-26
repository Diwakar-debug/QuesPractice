class Solution:
    def thirdLargest(self,a, n):
        # code here
       if n == 1 or n == 2 :
           return -1
       for i in range(2):
           max = a[0]
           for j in a:
               if j > max:
                   max = j
           a.remove(max)
       max = a[0]
       for i in range(0,len(a)):
           if a[i] > max:
               max = a[i]
               
       return max

#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends