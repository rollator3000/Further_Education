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
# 1-1 Define the list & k
k       = 17
numbers = [10, 15, 3, 7] 

# 1-2 Write function:
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


# 1-3 Check it:
check_two_sum(numbers = [2, 7, 5, 11, -7, 6, -131], k = 1)    # Should be FALSE
check_two_sum(numbers = [2, 7, 5, 11, -7, 6, -131], k = -129) # Should be TRUE