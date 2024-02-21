from terminaltables import SingleTable

table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = SingleTable(table_data)
table.inner_row_border = True
print(table.table)
