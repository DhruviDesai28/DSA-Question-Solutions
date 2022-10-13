#User function Template for python3

class Solution:
	def singleNumber(self, a):
		d = {}
		for i in a:
		    if i in d:
		        d[i]+=1
		    else:
		        d[i] = 1
		c = []
		for i in d.items():
		    if i[1] == 1:
		        c.append(i[0])
		c.sort()
		return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends