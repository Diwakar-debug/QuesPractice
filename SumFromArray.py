#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
   #Write your code here
       sumval=0
       i=0
       while(i<n):
           sumval=arr[i]
           j=i+1
           while(j<=n):
               if sumval<s:
                   if j==n:
                       break
                   sumval+=arr[j]
                   j+=1
               
               elif sumval>s:
                   sumval-=arr[i]
                   i+=1
                   continue
               
               else:
                   return [i+1,j]
           i+=1
               
               
       return [-1]