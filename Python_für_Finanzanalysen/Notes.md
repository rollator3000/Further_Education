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
- Printing & formatting `"Der Durchschnitt der {0} ist {1} Kilometer.".format('Erde', 12345)`    
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

### 2.4 Part Four
- Small functions can be mapped into `lambda()`  
```
def mal2(var):
	return(var * 2)

l_mal2 = lambda var: var * 2

l_mal2(2) --> 4
mal2(2)   --> 4
```
- `map` maps a function to a list of sequence - to see the result we need to convert the result to a list   
```
lst = [1,2,3] = [1, 2, 3, 4]
list(map(lambda var: var * 2, seq)) --> [2, 4, 6, 8]
```
- `filter` can be used to filter a list - to see the result we need to convert the result to a list   
```
list(filter(lambda x: x % 2 == 0), seq) --> [2, 46
```
- Methods are class specific operations *(e.g. for strings, lists, integers, ...)* - example for strings, dictionaries & lists  
- To get the availabe methods of a element, type '.' and 'tab'  
```
st = "Hallo mein Name ist Sam"
st.lower()                       --> 'hallo mein name ist sam'
st.upper()                       --> 'HALLO MEIN NAME IST SAM'
st.split()                       --> ['Hallo', 'mein', 'Name', 'ist', 'Sam']
'Los Sports! #Sports'.split("#") --> ['Los Sports! ', 'Sports']
```
```
d = {'key1': 'item1', 'key2': 'item2'}
d.keys()  --> dict_keys(['key1', 'key2'])
d.items() --> dict_items([('key1', 'item1'), ('key2', 'item2')])
```
```
lst = [1,2,3]
lst.pop()            --> removes the last element (3)
'x' in [1,2,3]       --> False
'x' in ['x','y','z'] --> True
```

### 1. Exercise - Python Basics  
- Corresponding JupyterNotebook with own solutions: 'Python_für_Finanzanalysen/code/01-Python_Crashkurs/2-Python_Crashkurs_Uebung-Aufgabe.ipynb'     
- Solutions from the course in: 'Python_für_Finanzanalysen/code/01-Python_Crashkurs/3-Python_Crashkurs_Uebung-Loesung.ipynb'     

<br/>
<br/>

# (4) NumPy
Library for linear algebra, data science, etc. in Python - fast as it builds up on 'C'.   
- In this course mainly used for NumPy-Vectors & -Matrixs  
 

