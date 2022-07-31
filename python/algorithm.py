import AlgorithmQuestions as algorithm_questions

dsa = algorithm_questions.AlgorithmQuestions()

test_case_a = [5, 2, 4, 6, 1, 3]
print('insertion_sort: ', dsa.insertion_sort(test_case_a))

test_case_b = [31, 21, 4, 7, 9]
print('insertion_sort_ex: ', dsa.insertion_sort_ex(test_case_b))

test_case_c = [1, 3, 4, 7, 2]
print('linear_search: ', dsa.linear_search(test_case_c, 7))

# Find the largest number in the array using divide and conquer method. 
test_data_d = [1, 3, 2, 8, 9, 10, 15, 7, 0]
print('divide_conquer: ', dsa.divide_conquer(test_data_d))

dsa.for_loop_recursion(0, 5)

print('factorial: ', dsa.factorial(10))

# Data modeling

