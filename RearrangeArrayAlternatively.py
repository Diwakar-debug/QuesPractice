#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        a=[]
        b=1
        for i in range(0,(n//2)+1):
            if b<=n:
                a.append(arr[n-i-1])
                b+=1
            if b<=n:
                a.append(arr[i])
                b+=1
        arr.clear()
        for j in a:
            arr.append(j)
        return arr
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends