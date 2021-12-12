# Practice Questions

### 1. What are the two values of the Boolean data type? How do you write them?

- &ensp; **True** &ensp;-> &ensp; Starts with a capital T with the rest of the word in lowercase with no single or double quotes.
- &ensp; **False** -> &ensp; Starts with a capital T with the rest of the word in lowercase with no single or double quotes.
### 2. What are the three Boolean operators?
- and
- or
- not
### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
<!-- #### and
Expression|Result
---------------|---------------
True and True|True
True and False|False
False and True|False
False and False|False
#### or
Expression|Result
---------------|---------------
True or True|True
True or False|True
False or True|True
False or False|False
#### not
Expression|Result
---------------|---------------
not True|False
not False|True -->
<table>
<tr><th>and </th><th>or</th><th>not</th></tr>
<tr><td>

|Expression| Result|
|--|--|
True and True|True|
True and False|False|
False and True|False|
False and False|False|

</td><td>

|Expression| Result|
|--|--|
True or True|True|
True or False|True|
False or True|True|
False or False|False|

</td><td>

|Expression| Result|
|--|--|
not True|False|
not False|True|
</td></tr> </table>

### 4. What do the following expressions evaluate to?
```python
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

```
#### Ans
```python
>>> (5 > 4) and (3 == 5)
False
>>> not (5 > 4)
False
>>> (5 > 4) or (3 == 5)
True
>>> not ((5 > 4) or (3 == 5))
False
>>> (True and True) and (True == False)
False
>>> (not False) or (not True)
True

```
### 5. What are the six comparison operators?
Operators|Meaning
---------------|---------------
|==|Equal to
|!=|Not equal to
|<|Less than
|>|Greater than
|<=|Less than or equal to
|>=|Greater than or equal to


### 6. What is the difference between the equal to operator and the assignment operator?
- The `=` operator is an assignment operator and assigns the value on the into the variable on the left
- The `==` operator is a comparison operator and ask whether the two values on the left and right equal to each other
### 7. Explain what a condition is and where you would use one.
Boolean expressions which evaluate down to a boolean value are known as conditions. These are generally put after the `if` statement.
### 8. Identify the three blocks in this code:
```python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```
#### Ans
```python
spam = 0
if spam == 10:
  ❶ print('eggs')
    if spam > 5:
      ❷ print('bacon')
    else:
      ❸ print('ham')
    print('spam')
print('spam')
```
### 9. Write code that prints `Hello` if `1` is stored in `spam`, prints `Howdy` if `2` is stored in `spam`, and prints `Greetings!` if anything else is stored in `spam`.
```python
spam=int(input()) #enter spam value
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')
```

### 10. What keys can you press if your program is stuck in an infinite loop?
Ctrl + C


### 11. What is the difference between `break` and `continue`?
- `break`:used for immediate termination of loop. Skips the execution of the remaining statements of loop.
-  `continue`:terminates the current iteration and resumes the control to the next iteration of the loop.

### 12. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a for `loop`?

### 13. Write a short program that prints the numbers `1` to `10` using a `for` loop. Then write an equivalent program that prints the numbers `1` to `10` using a `while` loop.

### 14. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?

