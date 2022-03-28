#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
       array.sort()
       total=1
       for i in array:
           if(total>=i):
               total+=i
       return total

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends