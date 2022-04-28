#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
       dic = defaultdict(int)
       s, res = 0, 0 
       dic[0] += 1
       
       for a in arr:
           s += a
           res += dic[s]
           dic[s] += 1
       return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends