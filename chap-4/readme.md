## Practice Questions
### 1. What is []?
```
Square brackets [] are used to declare a list in Python.
```
### 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
```python
spam[2]="Hello"
```
### For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
#
### 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
```python
>>> spam[int(int('3' * 2) // 11)]
'd'
```
### 4. What does spam[-1] evaluate to?
```python
>>> spam[-1]
'd'
```
### 5. What does spam[:2] evaluate to?
```python
>>> spam[:2]
['a', 'b']
```

### For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
#
### 6. What does bacon.index('cat') evaluate to?
```python
>>> bacon.index('cat')
1
```

### 7. What does bacon.append(99) make the list value in bacon look like?
```python
>>> bacon.append(99)
>>> bacon
[3.14, 'cat', 11, 'cat', True, 99]
```
### 8. What does bacon.remove('cat') make the list value in bacon look like?
```python
>>> bacon.remove('cat')
>>> bacon
[3.14, 11, 'cat', True, 99]
```

### 9. What are the operators for list concatenation and list replication?
```
For concatenation: >>> list1 + list2
For replication:   >>> listname * 3
```

### 10. What is the difference between the append() and insert() list methods?
```python
append(): inserts value at the end of the list.
insert(): inserts value at the specified index number.
```

### 11. What are two ways to remove values from a list?
```python
list_name.remove(value_to_be_removed)
del list_name[index_number_to_be_removed]
```

### 12. Name a few ways that list values are similar to string values.
```
Both can be concatenated and replicated. Can access any particular value by providing the value's index number from 
both. 
```
### 13. What is the difference between lists and tuples?
```
List[]   -> Mutable data type   -> Values can be altered.
Tuple()  -> Immutable data type -> Values can't be altered.

```
### 14. How do you type the tuple value that has just the integer value 42 in it?
```python
tupple_name = (42)
```
### 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
```python
>>> tuple([list_name[index]])
>>> list([tuple_name[index]])
```
### 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
```
They contain references to list values.
```
### 17. What is the difference between copy.copy() and copy.deepcopy()?
```
copy.copy(): shallow copy of a list.

copy.deepcopy(): extensive copy of a list which includes nested list(s) (if any, can't be achieved by copy.copy()) 
```
