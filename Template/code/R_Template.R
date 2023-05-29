## General:
#  (1) Tools > Global Options > Code > Display > MarginColumn = 100
#  (2) Tools > Global Options > Apperance > Cobalt
"
What is this script doing?! 
What is the overall goal?!

(1) Chapter1 Topic
    - Detail 1
    - Detail 2
    - ...
(2) Chapter2 Topic
    - Detail 1
    - Detail 2
"
# [0] Set WD, load packages, define variables & functions                                       ----
# 0-1 WD
setwd('Path/to/repository')

# 0-2 Packages
library(checkmate)

# 0-3 Variables
variables_must_be_all_lower_seperated_by_underscore <- "Example"

# 0-4 Functions
example_function <- function(x, y = "lol") {
    "What happens in this function? 

     Args:
        x (int): BlaBlaBla
        y (str): BluBluBlu

    Return:
        List of ...
    "
    # [0] Check Inputs
    # 0-1 'x' must be dataframe w/o missing values
    assert_data_frame(x, any.missing = FALSE)

    # 0-2
    # 0-2-1 

    # [1] Do something
    # 1-1 
    # 1-2
    # 1-2-1
    # 1-2-2 
}

# [1] Chapter1                                                                                  ----
# 1-1 SubChapter1
# 1-1-1 SubSubChapter1
# 1-1-1-1 SubSubSubChapter1
sapply(cars$speed, function(x) {
  # --1 First step in the loop/ apply/ ...
  
  # --2 Second step in the loop/ apply/ ...
})

# [2] Chapter2                                                                                  ----
# 2-1 SubChapter1
# 2-1-1 SubSubChapter1
# 2-1-1-1 SubSubSubChapter1