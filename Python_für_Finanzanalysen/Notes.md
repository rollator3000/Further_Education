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

Code to this chapters can be found in 'Python_für_Finanzanalysen/code/02-Numpy/'  

### 2.1 Arrays
- `np.array([1, 2, 3])` creates an numpy array  
- `np.array([1, 2, 3], [4, 5, 6])` creates an numpy martix    
- `np.arange(1, 10)` numpy array from 1 - 9  
- `np.zeros(3)` // `np.ones(3)` creates an array with 3 0 / 1 values  
- `np.zeros((3, 3))` // `np.ones((3, 3))` creates an 3x3 matrix with only 0 / 1  
- `np.linspace(0, 10, x)` x uniformly distributed values between 0 & 10  
- `np.exe(3)` Unit matrix  
- `np.random.rand(2)` array with two random values between 0 & 1  
- `np.random.randint(1, 100, x)` a x integer value(s) between 1 & 99   
- `array.reshape(5, 5)` convert 'array' into a 5x5 matrix  
- `.max()`// `.min()` returns the max/ min value of an array  
- `argmax()`// `argmin()` returns the index of the max/ min value  
- `.shape` returns the dimensions of a np array / matrix  
- `.dtype` returns the data type objects in an array  

### 2.2 Indexing  
Access values in a numpy array/ matrix: `arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  // `arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))`    

- `arr[8]` --> 8  
- `arr[1:5]` --> array([1, 2, 3, 4])    
- `.copy()` to copy an array properly, else we might change the values of the orgininal array, when changing the non legit copy *(Broadcasting)*    
- `arr_2d[1]` returns the second row --> array([20, 25, 30])  
- `arr_2d[1][0]` // `arr_2d[1,0]` both return 20 - with matrix always [ROW, COLUMN]   
- `arr_2d[:2,1:]` returns the first 2 rows and skip the first colulm --> array([[10, 15], [25, 30]])   
- `arr[arr > 5]` --> array([5, 7, 8, 9, 10])   

### 2.3 Operations