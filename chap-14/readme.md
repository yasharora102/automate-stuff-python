## Practice Questions
### 1. What three files do you need for EZSheets to access Google Sheets?
```
credentials file
token file for Google Sheets
token file for Google Drive
```
### 2. What two types of objects does EZSheets have?
```
ezsheets.Spreadsheet
ezsheets.Sheet
```
### 3. How can you create an Excel file from a Google Sheet spreadsheet?
```
downloadAsExcel() Spreadsheet
```
### 4. How can you create a Google Sheet spreadsheet from an Excel file?
```
ezsheets.upload() and pass filename
```
### 5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?
```
ss['Students']['B2']
```
### 6. How can you find the column letters for column 999?
```
ezsheets.getColumnLetterOf(999)
```
### 7. How can you find out how many rows and columns a sheet has?
```
sheet.rowCount and sheet.columnCount
```
### 8. How do you delete a spreadsheet? Is this deletion permanent?
```
By delete() Sheet, only permanent if permanent=True passed. Else remains in trash od Google Drive.
```
### 9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
```
createSpreadsheet() and createSheet()
```
### 10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
```
EZSheets will throttle the method calls.
```