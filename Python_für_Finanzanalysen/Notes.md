# Python for financial analysis and algorithmic trading

Notes to the Online-Course 'Python für Finanzanalysen und algorithmisches Trading' - https://www.udemy.com/course/python-fur-finanzanalysen-und-algorithmisches-trading/  

## Overview

1. Jupyter Notebook SetUp
2. Python Crashkurs
	- 
	- 

<br/> 

# (1) Jupyter Notebook SetUp
- Install Anaconda
- Open it > 'Jupyter Lab'
- Navigate to the folder of this course
- '00-Installation-Finanz-Packete/00-PythonFinance-PipInstallation-Abhaengigkeiten.ipynb'
- Run it to install all packages needed for this course

# (2) Python Crashkurs
- Corresponding JupyterNotebook: 'Python_für_Finanzanalysen/code/01-Python_Crashkurs/1-Python_Crashkurs_Teil_1-4.ipynb'  

### 2.1 Part One
- Mathematical operations *(multiplication, addition, division, power off, modulo, ...)*  
- Variable assigments  
- Strings  
- Printing & formatting  
- Lists *(append, indexing, list in lists)*  

### 2.2 Part Two
- Dictionaries *(key-item pairs, item could also be a list/ dictionary/ ...)*  
```
d = {'key1':'item1','key2':'item2'} 
d['key1']                           # Access item of 'key1' 
```
- Booleans *(True & False)*  
- Tupel *(can not be changed subsequently)*  
```
t = (1, 2, 3) 
```
- Sets *(like lists, but will only contain unique values)*  
```
s = {1, 2, 3, 4} 
s.add(12)        # Add an element
```
- Comparison operators `<, >, <= , >=, ==`
- Logical operators `and, or` to combine comparisons    
- If, elif & else
```
if 1 == 2:
    print('Zuerst')
elif 3 == 3:
    print('In der Mitte')
else:
    print('Zuletzt')
``` 

### 2.3 Part Three
- For loops  
- While loops  
- range *(range(from [incl.], to [excl.]))*  
- List comprehension *(smaller for loops)* 
```
y = []
for item in x:
	y.append(x ** 2)

[item ** 2 for item in x] # Same result as for loop above
```  
- Functions  
```
def meine_funk(param1='standard'):
    """
    Funktionsbeschreibung steht hier.
    """
    print(param1)

meine_funk(param1 = "Deine Mutter")
```