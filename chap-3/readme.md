## Practice Questions
### 1. Why are functions advantageous to have in your programs?
```
The major purpose of functions is to group code that gets executed multiple times. 
They make programs shorter, easier to read, and easier to update.
```
### 2. When does the code in a function execute: when the function is defined or when the function is called?
   ```
   When the function is called.
   ```
### 3. What statement creates a function?
```
def statement
```

### 4. What is the difference between a function and a function call?
```
A function is like a miniprogram within a program. It is a set of instructions grouped together to achieve a 
particular result. A function call is sending the execution to the top of the function’s code and using this 
function to achieve the result.
```

### 5. How many global scopes are there in a Python program? How many local scopes?
```
There is only one global scope. The local scope can be as many as desired.
```
### 6. What happens to variables in a local scope when the function call returns?
```
There is no change.
```

### 7. What is a return value? Can a return value be part of an expression?
```
The value that a function call evaluates to is called the return value of the function. The return value can 
be part of an expression.
Example: return 3+1

```

### 8. If a function does not have a return statement, what is the return value of a call to that function?
```
None is returned if a function doesn't have a return statement.
```
### 9. How can you force a variable in a function to refer to the global variable?

```
Achieved by using global statement alongwith variable name before defining the function.
```
```python
global variablename
```

### 10. What is the data type of None?
```python
NoneType
```

### 11. What does the import areallyourpetsnamederic statement do?
```
It imports a module named areallyourpetsnamederic.
```

### 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
```python
spam.bacon()
```
### 13. How can you prevent a program from crashing when it gets an error?
```
By using try and except clauses.
```
### 14. What goes in the try clause? What goes in the except clause?
```
The code which may have an error is put in a try clause and the except clause contains code to handle what happens 
when error occurs.
```
