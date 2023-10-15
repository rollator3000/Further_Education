#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coiding Exercises in Python
"""

# %% (1) Sum Of Numbers 
"""
- This problem was recently asked by Google.
- Given a list of numbers and a number k, return whether any of the two numbers
  from the list add up to k.
- For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
# 1-1 Write function:
def check_two_sum(numbers, k):
    
    # 1) Empty set to safe the unique differences between 'k' & 'numbers'
    comps = set()
    
    # 2) Loop over each element in 'numbers' to check if 2 elements can sum up 
    #    to 'k'
    for number in numbers:
        
        # Check if 'number' is part of 'comps' already 
        # (this means that the current number adds up to 'k' with a previous 
        #  number from 'numbers') 
        if number in comps:
            return True
        
        # Else get the difference between number and 'k' and add it to comps
        # (if any number from 'numbers' matches with this, it adds up to 'k')
        else: 
            comps.add(k - number)
        
    # 3) Return False, in case the loop in 2) didn't return true yet ;-)
    return False

# 1-2 Check it:
check_two_sum(numbers = [2, 7, 5, 11, -7, 6, -131], k = 1)    # Should be FALSE
check_two_sum(numbers = [2, 7, 5, 11, -7, 6, -131], k = -129) # Should be TRUE

# %% (2) 
"""
- This problem was asked by Uber
- Given an array of integers, return a new array such that each element at 
  index i of the new array is the product of all the numbers in the original
  array except the one at i.
- For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
 [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
 be [2, 3, 6].
"""
# 2-1 Write a function
def list_product(int_list):
    
    # 1) Empty list to fill products of all list elements except 'i' 
    return_list = []
    
    # 2) Loop over indeces in int_list
    for curr_ind in range(0, len(int_list)):
        
        # 2-1 Take all elements from 'int_list' except the one on 'curr_ind'
        elements_except_curr_ind = int_list[:curr_ind] + int_list[curr_ind+1:]
        
        # 2-2 Get the product of all elements in elements_except_curr_ind
        curr_result = 1
        for x in elements_except_curr_ind:
            curr_result = curr_result * x
         
        return_list.append(curr_result)
        
    # 3) Return the new list 
    return return_list
        
# 2-2 Check it:
list_product(int_list = [1, 2, 3, 4, 5])  # Should be: [120, 60, 40, 30, 24]
list_product(int_list = [3, 2, 7, 2, -2]) # Should be: [-56, -84, -24, -84, 84]

# %%  (3) 
"""
- This problem was asked by Stripe.
- Given an array of integers, find the first missing positive integer in linear
  time and constant space. In other words, find the lowest positive integer that 
  does not exist in the array.
- For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
- You can modify the input array in-place.
"""
# 3-1 Define Function
def find_missing_int(int_list):
    
    # 1) Order int_list and remove duplicates
    int_list_unique_ordered = set(int_list)
    
    # 2) Loop from 1 to the length of 'int_list_unique_ordered' & check if 
    #    the numbers are part of it already
    for curr_int in range(1, len(int_list) + 1):
        if curr_int not in int_list_unique_ordered:
            return(curr_int)
        
    return len(int_list_unique_ordered) + 1
     
# 3-2 Check it:
find_missing_int([-1, 0, 1, 2, 3, 4, 5, 7, 8])
find_missing_int([-1, 1212, 1, 2, 3, 4, 5, 7, 8])
find_missing_int([-1, 0, 1, 2, 3, 4, 5, 7, 6, 8])