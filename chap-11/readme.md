## Practice Questions
### 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
```python
assert spam>=10
```
### 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
```python
assert eggs.lower() != bacon.lower()
```
### 3. Write an assert statement that always triggers an AssertionError.
```python
assert False
```
### 4. What are the two lines that your program must have in order to be able to call logging.debug()?
```python
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s- %(levelname)s - %(message)s')
```
### 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
```python
import logging
logging.basicConfig(filename='programLog.txt',level=logging.DEBUG,format='%(asctime)s- %(levelname)s- %(messages)s')
```
### 6. What are the five logging levels?
```
info
debug
warning
error
critical
```
### 7. What line of code can you add to disable all logging messages in your program?
```python
logging.disable(logging.CRITICAL)
```
### 8. Why is using logging messages better than using print() to display the same message?
```
Removing all the print() would be time consuming sometimes we may accidentally delete the no logging print statement.
```
### 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
```
Step In: will move the debugger to function call
Step Over: will execute the function call without stepping
Step Out: executes the rest of the code until it steps out of the function.
```
### 10. After you click Continue, when will the debugger stop?
```
When it reaches the end of the program or at a breakpoint.
```
### 11. What is a breakpoint?
```
Breakpoint is a setting on a line of code that pauses the debugger when the execution reaches the line.
```
### 12. How do you set a breakpoint on a line of code in Mu?
```
Click the line number to make a red dot appear next to it.
```