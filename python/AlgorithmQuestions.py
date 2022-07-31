class AlgorithmQuestions:
    def __init__(self):
        pass

    def for_loop_recursion(self, start, end):
        if start == end:
           return 'loop ended'
        print('for loop: ', start)
        start += 1
        return self.for_loop_recursion(start, end)

    def factorial(self, n):
       if n == 0:
        return 1
       else:
        return self.factorial(n - 1) * n 


    def insertion_sort(self, arr):
        """Insertion algorithm. Insertion algorithm is an algorithm for sorting small number of elements eg: [5,2,4,6,1,3] solution:
        A = [5,2,4,6,1,3]
        for j = 2 to A.length
            key = A[j]
            #Insert A[j] into the sorted sequence A[1..j-1]
            i = j - 1
            while i > 0 and A[i] > key
              A[i + 1] = A[i]
              i = i - 1
              A[i + 1] = key"""

        for j in range(len(arr)):
            key = arr[j]
            i = j - 1
            while i > 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i = i - 1
                arr[i + 1] = key
        return arr

    def insertion_sort_ex(self, arr):
        """exercise 1Rewrite the INSERTION-SORT procedure to sort 
        into non increasing instead of non decreasing order."""
        for j in range(len(arr)):
            key = arr[j]
            i = j - 1
            while i > 0 and arr[i] < key:
                arr[i + 1] = arr[i]
                i = i - 1
                arr[i + 1] = key
        return arr

    def linear_search(self, arr, v):
        """exercise 2, Consider the searching problem: 
        Input: A sequence of n numbers A[1,2...n] and a value v.Output: 
        An index i such that v = A[i] or the special value NIL if 
        does notappear in A."""
        value = 0
        for i in arr:
            if v == i:
                value += i
        return value

    def divide_conquer(self, test_data):
        """Divide and conquer algorithm: 
        Many useful algorithms are recursive in structure: 
        to solve a given problem, they call themselves recursively 
        one or more times to deal with closely related sub problems. 
        These algorithms typically follow a divide-and-conquer approach: 
        they break the problem into several sub problems that are 
        similar to the original problem but smaller in size, 
        solve the sub problems recursively, and then combine these solutions 
        to create a solution to the original problem.
        The divide-and-conquer paradigm involves three steps at each level 
        of the recursion: Divide: the problem into a number of sub problems 
        that are smaller instances of the same problem.Conquer: 
        the sub problems by solving them recursively. 
        If the sub problem sizes are small enough, however, just solve the 
        sub problems in a straightforward manner.Combine: the solutions 
        to the sub problems into the solution for the original problem"""

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
