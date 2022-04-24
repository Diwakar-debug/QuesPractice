

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
	   temp = sorted(nums)
       mapp = {}
       swaps = 0
       num_len = len(nums)
       for i in range(num_len):
           mapp[nums[i]] = i
           
       for i in range(num_len):
           if nums[i] == temp[i]: # element already in their place
               continue
           else:
               init = nums[i] 
               #swapping the elements of input array to their correct pos
               
               nums[i], nums[mapp[temp[i]]] = nums[mapp[temp[i]]], nums[i]
               swaps += 1
               # updating map values after swapping
               mapp[init] = mapp[temp[i]]
               mapp[temp[i]] = i
       return swaps
  
#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends