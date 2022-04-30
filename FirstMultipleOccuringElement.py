#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
       mdict ={}
       for num in arr:
           if num in mdict:
               mdict[num] += 1
           else:
               mdict[num] = 1
       for idx,num in enumerate(arr):
           if mdict[num] > 1:
               return idx +1
       
       return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends