# Practice Questions

### 1. Which of the following are operators, and which are values?
1. &ensp; &#8727; &emsp;&emsp;-> &emsp;Operator
2. &ensp; 'hello' &emsp;&emsp;-> &emsp;Value 
3. &ensp; -88.8 &emsp;&emsp;-> &emsp;Value
4. &ensp; &#8722; &emsp;&emsp;-> &emsp;Operator
5. &ensp; / &emsp;&emsp;-> &emsp;Operator
6. &ensp; &#43; &emsp;&emsp;-> &emsp;Operator
7. &ensp; 5 &emsp;&emsp;-> &emsp;Value

### 2. Which of the following is a variable, and which is a string?
1. &ensp; spam &emsp;&emsp;-> &emsp;Variable
2. &ensp; 'spam' &emsp;&emsp;-> &emsp;String

### 3. Name three data types.
- Integer
- Float
- String
### 4. What is an expression made up of? What do all expressions do?
Expressions consist of values and operators. All expressions can always evaluate down to a single value. 
### 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
A statement represents an action or command to be performed whereas an expression consists of values and operattors which evaluate down to a single value.
### 6. What does the variable bacon contain after the following code runs?
```python
bacon = 20
bacon + 1
```
Answer --> **21**
### 7. What should the following two expressions evaluate to?
```python
'spam' + 'spamspam'
'spam' * 3
```
Answer
```python
'spamspamspam'
'spamspamspam'
```
### 8. Why is ``eggs`` a valid variable name while ``100`` is invalid?
Because `100` starts with a number.
### 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
```python
- int()   -> integer 
- float() -> floating-point number
- str()   -> string
```
### 10. Why does this expression cause an error? How can you fix it?
```python
'I have eaten ' + 99 + ' burritos.'
```
It gives an error because a string datatype can't be concatenated with an integer datatype.
We can fix this by type-casting the integer datatype to string datatype.
```python
'I have eaten ' + '99' + ' burritos.'
```
