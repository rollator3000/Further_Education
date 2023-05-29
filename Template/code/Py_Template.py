#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
What is this script doing?! 
What is the overall goal?!

(1) Chapter1 Topic
    - Detail 1
    - Detail 2
    - ...
(2) Chapter2 Topic
    - Detail 1
    - Detail 2
"""
#%% [0] Load packages, check WD, define fix variables & functions
# 0-1 Load packages
import os

# 0-2 Check WD
if "repository name" not in os.getcwd():
    raise ValueError("Working Directory not correct!")

# 0-3 Fix variables 
variables_must_be_all_lower_seperated_by_underscore = "Example"

# 0-4 Functions
def example_function(path, nec_cols):
    """
    What does this function?
    
    Args:
        > path      (str): BlaBlaBla
        > nec_cols (list): BluBluBlu
    
    Return:
        > DF...
    """
    # [0] Check Inputs
    # 0-1 'path' has to be a string of type '.ods' or '.csv' 
    if not isinstance(path, str): raise ValueError("'path' must be a str")
    if not '.csv' in path and not '.ods' in path: 
        raise ValueError("'path' must be of type '.csv' or 'ods'")

    # 0-2 'nec_cols' has to be a list with strings
    if not isinstance(nec_cols, list): raise ValueError("'nec_cols' must be a list")
    if not all(map(lambda x: isinstance(x, str), nec_cols)): 
        raise ValueError("'nec_cols' must only contain str")
        
    # [1] Do something
    # 1-1 
    # 1-2
    # 1-2-1
    # 1-2-2

#%% [1] Chapter Topic 1
# 1-1 SubChapter1
# 1-1-1 SubSubChapter1
# 1-1-1-1 SubSubSubChapter1
list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))

#%% [2] Chapter Topic 2
# 2-1 SubChapter2
# 2-1-1 SubSubChapter2
# 2-1-1-1 SubSubSubChapter2