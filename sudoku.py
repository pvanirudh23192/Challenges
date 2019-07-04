correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

def gen_for_row(custom_list, length):
    sum = 0
    for each_element in custom_list:
        sum = sum+int(each_element)

def my_gen_for_row(input_list, column_number):
    column_sum = 0
    for i in range(3):
        coulumn_sum += input_list[i,column_number]
    return column_sum


# Define a function check_sudoku() here:
def check_sudoku(input_list):
    number_of_rows = len(input_list)
    number_of_columns = number_of_rows
    sum = (1/2)*(number_of_rows)*(number_of_rows+1)
    for each_row in input_list:
        row_sum = gen_for_row(each_row, number_of_rows)
        if sum!=row_sum:
            return False
    for column in range(3):
       column_sum = my_gen_for_row(input_list,column)
       if sum!=column_sum:
            return False
    return True


#print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True
