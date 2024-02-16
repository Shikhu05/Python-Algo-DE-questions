# multiply array or product array puzzle

#User function Template for python3

# if array has more than 1 zero result is 0 for len of n 
# if array has 1 zero than result is for all elements expect the 0 element is 0 
									# and 0 will get all other multiplication
# else multiply all except the num u r at index


class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        res = []
        temp = 1
        count_zero = 0
        
        for i in nums:
            if i == 0:
               count_zero += 1
               
            if i != 0 and count_zero <= 1:
                temp *= i
            elif count_zero > 1:
                temp = 0
        temp_prod = temp
        # print(temp)
            
        
        if 0 in nums and count_zero == 1:
            for i in range(n):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(temp)
                temp_prod = temp
        else:    
            for i in range(n):
                if temp_prod != 0:
                    temp_prod = int(temp_prod/nums[i])
                
                res.append(temp_prod)
                temp_prod = temp
            # print(res)
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends

