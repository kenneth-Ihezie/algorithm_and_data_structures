"""
Insertion algorithm.
Insertion algorithm is an algorithm for sorting
small number of elements
eg: [5,2,4,6,1,3]
solution:
A = [5,2,4,6,1,3]
for j = 2 to A.length
    key = A[j]
    #Insert A[j] into the sorted sequence A[1..j-1]
    i = j - 1
    while i > 0 and A[i] > key
          A[i + 1] = A[i]
          i = i - 1
    A[i + 1] = key
"""

 
def insertion_sort(arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


test_case_a = [5, 2, 4, 6, 1, 3]
# print(insertion_sort(test_case_a))



"""
exercise 1
Rewrite the INSERTION-SORT procedure to sort into non increasing instead of non decreasing order.
"""


def insertion_sort_ex(arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


test_case_b = [31, 21, 4, 7, 9]
# print(insertion_sort_ex(test_case_b))

"""
exercise 2
Consider the searching problem:
Input: A sequence of n numbers A[1,2...n] and a value v.
Output: An index i such that v = A[i] or the special value NIL if  does not
appear in A.
"""


def linear_search(arr, v):
    value = 0
    for i in arr:
        if v == i:
            value += i
    return value


test_case_c = [1, 3, 4, 7, 2]
# print(linear_search(test_case_c, 7))

"""
Divide and conquer algorithm:
Many useful algorithms are recursive in structure: to solve a given problem, they
call themselves recursively one or more times to deal with closely related sub problems. These algorithms typically 
follow a divide-and-conquer approach: they
break the problem into several sub problems that are similar to the original problem but smaller in size, solve the 
sub problems recursively, and then combine these
solutions to create a solution to the original problem.
The divide-and-conquer paradigm involves three steps at each level of the recursion:
Divide: the problem into a number of sub problems that are smaller instances of the
same problem.
Conquer: the sub problems by solving them recursively. If the sub problem sizes are
small enough, however, just solve the sub problems in a straightforward manner.
Combine: the solutions to the sub problems into the solution for the original problem
"""

"""
Find the largest number in the array using divide and conquer method. 
"""
test_data_d = [1, 3, 2, 8, 9, 10, 15, 7, 0]


def divide_conquer(test_data):
    test_data_len = len(test_data)
    global test_data_mid_point
    global index_sum
    global first_sum
    first_sum = 0
    global second_sum
    second_sum = 0
    test_data_mid_point = test_data_len // 2
    for i in range(0, test_data_mid_point):
        index_sum = test_data[i]
        if index_sum > first_sum:
            first_sum = index_sum
    for i in range(test_data_mid_point + 1, len(test_data)):
        index_sum = test_data[i]
        if index_sum > second_sum:
            second_sum = index_sum
    if first_sum > second_sum:
        return first_sum
    else:
        return second_sum


# print(divide_conquer(test_data_d))


"""
def for_loop_recursion(start, num):
    if start == num:
        return 'loop ended'
    print(start)
    start += 1
    return for_loop_recursion(start, num)


print(for_loop_recursion(5, 50))
"""
import random as rd


unsorted = []
for i in range(2, 100):
    unsorted.append(rd.randrange(i))

def bigSorting(unsorted):
    unsorted.sort()
    if len(unsorted) == 1:
        print(unsorted[0])
        return
    size = 0
    print(unsorted[size])
    unsorted.remove(unsorted[size])
    return bigSorting(unsorted)


# bigSorting(unsorted)

string_arr = ['k', 'g', 'a', 'c', 'e']
string_arr.sort(reverse=True)
# print(string_arr)

set_in = 'aabbccdde'
# set_arr = []
# for i in set_in:
#     set_arr.append(i)
out = set(set_in)
#print(out)


# from . import AlgorithmQuestions as aq

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n 

# print(factorial(10))

# Data modeling

print(60 ^ 13)

