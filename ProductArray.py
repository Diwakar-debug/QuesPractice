#User function Template for python3
import numpy as np
class Solution:
    def productExceptSelf(self, nums, n):
        #code here
       prod=np.prod(nums)
       product_arr=[]
       if 0 not in nums:
           for i in nums:
               product_arr.append(prod//i)
       else:
          product_arr=[0]*n
          ind=nums.index(0)
          nums.pop(ind)
          product_arr[ind]=np.prod(nums)
       return product_arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends