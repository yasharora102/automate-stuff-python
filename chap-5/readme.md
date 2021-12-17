## Practice Questions
### 1. What does the code for an empty dictionary look like?
```python
{}
```

### 2. What does a dictionary value with a key `'foo'` and a value `42` look like?
```python
{'foo': 42}
```
### 3. What is the main difference between a dictionary and a list?
```
List: items are ordered.
Dictionary: items are unordered.
```

### 4. What happens if you try to access `spam['foo']` if `spam` is `{'bar': 100}`?
```python
KeyError
```
### 5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat'` in `spam` and `'cat'` in `spam.keys()`?
```
There is no difference. It checks if the value 'cat' exists as a key value in the dictionary.
```
### 6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()`?
```
'cat' in spam: Checks whether 'cat' exists as a key value in the dictionary 'spam'.
'cat' in spam.values(): Checks whether 'cat' exists as a value for any of the keys in 'spam'.
```
### 7. What is a shortcut for the following code?
```python
if 'color' not in spam:
    spam['color'] = 'black'
```
```python
spam.setdefault('color', 'black')
```
### 8. What module and function can be used to “pretty print” dictionary values?
```python
pprint.pprint()
```
