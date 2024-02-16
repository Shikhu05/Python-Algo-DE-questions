# 1.
# Can you do the following without using subquery?: 
# # {1,None,1,2,None} --> [1,1,1,2,2] Ensure you take care of case input[None] which means None object
# lst = [1,None,1,2,None]

# for i in range(len(lst)):
# 	if lst[i] == None:
# 		lst[i] = 1
# print (lst)


## 2.
## Write a function in Python to check duplicate letters. 
## It must accept a string, i.e., a sentence.
## The function should return True 
## if the sentence has any word with duplicate letters, else return False. 


# s = "this is a sunny sentence"

# def find_udp(s):
# 	chck = set()
# 	for w in s.split(' '):
# 		new_word = ''
# 		for c in w:
# 			if c not in new_word:
# 				new_word += c
# 			else:
# 				return True
# 	return False

# print( find_udp(s))



##3.
# Write a function to detect 13th Friday. 
# The function can accept two parameters, and both will be numbers.
# The first parameter will be number indicating  month, and the second will be the year in four digits.
#  Your function should parse the parameters, 
# and it must return True when the month contains a Friday with the 13th, else return False. 

# m = 12
# y = 2022

# import datetime
# from datetime import date 

# def test(m,y):
# 	is_13_friday = date(y,m,13).strftime("%A") 
# 	if is_13_friday.upper() == 'FRIDAY' :
# 		return True
# 	else:
# 		return False

# print( test(m,y) )



##4. Validate ip address

# ip= '12.a.11.121'
# # ip = '127.0.0.1'

# def ip_chck(ip):
# 	if ip in (["127.0.0.1", "0.0.0.0", "255.255.255.255"]):
# 		return False

# 	a = ip.split('.')

# 	if len(a) != 4:
# 		return False
# 	elif a[0] == 0  :
# 		return False
# 	else:
# 		for i in a:
# 			if i.isnumeric() :
# 				continue
# 			else:
# 				return False
# 			i = int(i)
# 			if i < 0 or i > 255:
# 				return False
# 		return True

# print (ip_chck(ip))


##5
## Write a function in Python to parse a string such that it accepts a parameter- an encoded string. 
## This encoded string will contain a first name, last name, and an id. 
## You can separate the values in the string by any number of zeros. The id will not contain any zeros. 
## The function should return a Python dictionary with the first name, last name, and id values. 
## For example, if the input would be "John000Doe000123". 
## Then the function should return: { "first_name": "John", "last_name": "Doe", "id": "123" }

# a= 'John000Doe000123'

# def parse(a):
# 	a = [ c for c in a.split('0') if c != '']
# 	keys = ['first_name', 'last_name', 'id']
# 	dct = {k:v for k,v in zip(keys,a)}
# 	return dct
# print(parse(a))



## 6
## Find the second largest number in the integer array.

# arr = [3,6,50,23,11,19,23]

# def print2largest(self,arr):
# 	# code here
#     max = arr[0]
#     n_max = float('-inf') 

#     for i in arr:
#     	if i > max :
#     		n_max = max 
#     		max = i 
#     	elif i > n_max and max > i :
#     		n_max = i 
#     	else:
#     		continue
    		
# 	if n_max == float('-inf') :
# 	    return -1
# 	else:    
#         return n_max

# def secondlargest(arr):
# 	arr = sorted(set(arr), reverse = True)
	
# 	if len(arr) < 2:
# 		return -1
# 	else:
# 		return arr[1]

# print (secondlargest(arr))



## 7.
## sort function in python

# quick sort


# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quicksort(left) + middle + quicksort(right)

# # Example usage:
# my_list = [3, 1, 4, 4, 5, 6]
# sorted_result = quicksort(my_list)
# print(sorted_result)



## 8. Largest prime of a given number

# def largestPrimeFactor (N):
#     primes = []
#     n = int (N ** 0.5) 


#     for i in range( 2, n+1) :
#         while N % i == 0:
#             N //= i
#             primes.append(i)

#     return (N if N != 1 else primes[-1])

# print(largestPrimeFactor (24))


##9
# Palindrome true or false

# a = 'abdsba'
# def p(a):
# 	# if a == a[::-1]:
# 	# 	return True
# 	# else:
# 	# 	return False

# 	for i in range(len(a)):
# 		# for j in range(len(a),i)
# 		if a[i - 1] != a[-i]:
# 			# print(i, a[i] , a[-i])
# 			return False
# 		else:
# 			continue

# 	return True

# print(p(a))


##10
# not none values

# a = [1,2,None, 3, None]

# def nonnone(a):
# 	v = 0
# 	for i,c in enumerate(a):
# 		if c == None:
# 			a[i] = v 
# 		else:
# 			v = c 
# 	return a
	
# print(nonnone(a))














