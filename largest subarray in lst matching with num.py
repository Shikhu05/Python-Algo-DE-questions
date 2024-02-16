# def maxSubArray( nums: list[int]) -> int:

#     max_sum = nums[0]
#     x = nums[0]

#     for i in range (1, len(nums)):
#         x = max(nums[i], x+nums[i])
#         max_sum = max(x, max_sum)
    
#     return max_sum    

# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  



# Write a python function to find largest subarray of sum for a specific target sum as input.

def largest_subarray_sum(lst,n):
    sum1 = 0

    for i in range(len(lst)):
        sum1 = lst[i]
        if sum1 == n:
            return (lst[i])
        else:
            for j in range(i+1, len(lst)):
                sum1 += lst[j]
                if sum1 == n:
                    return (lst[i:j+1])
    return -1


lst = [1, 2, 3, 4, 5]
n = 9
print (largest_subarray_sum(lst,n))