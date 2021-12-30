## Practice Questions
### For the following questions, imagine you have a Workbook object in the variable wb, a Worksheet object in sheet, a Cell object in cell, a Comment object in comm, and an Image object in img.
#
### 1. What does the openpyxl.load_workbook() function return?
```
Workbook object
```
### 2. What does the wb.sheetnames workbook attribute contain?
```
Worksheet object.

```
### 3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?
```
wb['Sheet1']
```
### 4. How would you retrieve the Worksheet object for the workbook’s active sheet?
```
wb.active
```
### 5. How would you retrieve the value in the cell C5?
```
sheet['C5'].value
```
### 6. How would you set the value in the cell C5 to "Hello"?
```
sheet['C5'] = 'Hello'
```
### 7. How would you retrieve the cell’s row and column as integers?
```
cell.row and cell.column
```
### 8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?
```
They hold the highest column and row with values in the sheet as integer values.
```
### 9. If you needed to get the integer index for column 'M', what function would you need to call?
```
openpyxl.cell.column_index_from_string('M')
```
### 10. If you needed to get the string name for column 14, what function would you need to call?
```
openpyxl.cell.get_column_letter(14)
```
### 11. How can you retrieve a tuple of all the Cell objects from A1 to F1?
```
sheet['A1':'F1']
```
### 12. How would you save the workbook to the filename example.xlsx?
```
wb.save('example.xlsx’)
```
### 13. How do you set a formula in a cell?
```
Set the cell’s value attribute to a string of the formula text.
```
### 14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?
```
When calling load_workbook(), pass True for the data_only keyword argument.
```
### 15. How would you set the height of row 5 to 100?
```
sheet.row_dimensions[5].height = 100
```
### 16. How would you hide column C?
```
sheet.column_dimensions['C'].hidden = True
```
### 17. What is a freeze pane?
```
Freeze panes are rows and columns that will always appear on the screen.
```
### 18. What five functions and methods do you have to call to create a bar chart?
```python
openpyxl.chart.Reference()
openpyxl.chart.Series()
openpyxl.chart.BarChart()
chartObj.append(seriesObj)
add_chart()
```