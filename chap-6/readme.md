## Practice Questions
### 1. What are escape characters?
```
Escape characters represent characters in string values that would otherwise be difficult or impossible to type 
into code.
```
### 2. What do the `\n` and `\t` escape characters represent?
```
\n: newline
\t: tab
```
### 3. How can you put a `\` backslash character in a string?
```
By using \\
```

### 4. The string value `"Howl's Moving Castle"` is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
```
Because double quotes are used to mark the beginning and end of the string.
```
### 5. If you don’t want to put `\n` in your string, how can you write a string with newlines in it?
```
Multiline strings.
```
### 6. What do the following expressions evaluate to?
```python
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
```python
'e'
'Hello'
'Hello'
'lo, world!'
```
### 7. What do the following expressions evaluate to?
```python
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
```python
'HELLO'
True
'hello'
```
### 8. What do the following expressions evaluate to?
```python
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```
```python
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
'There-can-be-only-one.'
```
### 9. What string methods can you use to right-justify, left-justify, and center a string?
```
right-justify:  rjust()
left-justify:   ljust()
center:         center()
```
### 10. How can you trim whitespace characters from the beginning or end of a string?
```
left: lstrip()
right rstrip()
```
