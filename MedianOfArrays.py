#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
           array1.extend(array2)
           array1.sort()
           if len(array1)%2==0:
               k=len(array1)//2
               
               if (array1[k]+array1[k-1])%2!=0:
                   return (array1[k]+array1[k-1])/2
               else:
                   return (array1[k]+array1[k-1])//2
           else:
               k=(len(array1)-1)//2
               return array1[k]

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends