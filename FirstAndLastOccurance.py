#User function Template for python3


def find(arr,n,x):
    # code here
   min=n-1
   max=0
   for i in range(len(arr)):
       if arr[i]==x and i<min:
           min=i
       if arr[n-i-1]==x and (n-i-1)>max:
           max=n-i-1
   if max<min or min>max:
       return -1,-1
   return min,max


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends