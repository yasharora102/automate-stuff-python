## Practice Questions
### 1. What is the Unix epoch?
```
A reference moment that date and time programs use.
```
### 2. What function returns the number of seconds since the Unix epoch?
```python
time.time()
```
### 3. How can you pause your program for exactly 5 seconds?
```python
time.sleep(5)
```
### 4. What does the round() function return?
```
Returns the nearest integer to the argument passed.
```
### 5. What is the difference between a datetime object and a timedelta object?
```
datetime: specific moment in time.
timedelta: duration of time.
```
### 6. Using the datetime module, what day of the week was January 7, 2019?
```
Using datetime.datetime(2019, 1, 7).weekday(), 0 was returned which means Monday.
```
### 7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?
```python
threadObj = threading.Thread(target=spam) threadObj.start()
```
### 8. What should you do to avoid concurrency issues with multiple threads?
```
Make sure that code running in one thread does not read or write the same variables as code running in another thread.
```