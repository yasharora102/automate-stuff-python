## Practice Questions
### 1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?
```
Excel Spreadsheets can have values of data types other than strings,cells can have varying widths and heights,cells can have different fonts, sizes, or color settings.
```
### 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
```
File object returned from open().
```
### 3. What modes do File objects for reader and writer objects need to be opened in?
```
read-binary ('rb') for reader objects
write-binary ('wb') for writer objects
```
### 4. What method takes a list argument and writes it to a CSV file?
```
writerow()
```
### 5. What do the delimiter and lineterminator keyword arguments do?
```
delimiter: changes the string used to separate cells in a row
lineterminator: changes the string used to separate rows

```
### 6. What function takes a string of JSON data and returns a Python data structure?
```
json.loads()
```
### 7. What function takes a Python data structure and returns a string of JSON data?
```
json.dumps()
```