tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_print(tableData):
    
    #getting the maximum column width required
    column_width = []
    for i in range(len(tableData)):
        string_length=[]
        for j in range(len(tableData[i])):
            string_length.append(len((tableData[i][j])))
        column_width.append(max(string_length))
    
    #printing the table
    for row in range(len(tableData[0])): #rows
        for column in range(len(tableData)): #columns
            print(tableData[column][row].rjust(column_width[column]), end=' ')
        print()

table_print(tableData)