## Practice Questions
### 1. Does PyInputPlus come with the Python Standard Library?
```
No, it's a third party module.
```
### 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
```
To make the code shorter, readable and understandable.
```
```python
pyip.inputStr(): shorter, readable and understandable.
pyinputplus.inputStr(): lengthy and less readable.  
```
### 3. What is the difference between inputInt() and inputFloat()?
```
inputInt() :   Accepts an integer value
inputFloat() : Accepts a floating-point numeric value.
```
### 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
```python
pyip.inputint(min=0,max=99)
```
### 5. What is passed to the allowRegexes and blockRegexes keyword arguments?
```
List(s) of strings that is/are either allowed or denied.
```
### 6. What does inputStr(limit=3) do if blank input is entered three times?
```python
"RetryLimitException" raised.
```
### 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
```
It takes 'hello' as input.
```