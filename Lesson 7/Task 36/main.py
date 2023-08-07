def print_operation_table(operation, num_rows, num_columns):
    operation.insert(0, 0)
    str_1 = "" 
    for i in range (1, num_rows*num_columns + 1):
        str_1 = str_1 + str(operation[i]) + " "   
        if i % num_columns == 0:
            print (str_1)
            str_1 = ""
    return 

num_rows = 6
num_columns = 6
num_rows_list = []
num_columns_list = []

for i in range (1, num_rows + 1):
    for j in range (1, num_columns + 1):
        num_rows_list.append(i)
        num_columns_list.append(j)

print_operation_table(list(map(lambda x, y: x*y , num_rows_list, num_columns_list)), num_rows, num_columns)