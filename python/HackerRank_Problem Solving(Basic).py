"""
Grading Students.
Question Link = https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
"""
#solution of the above question is below....

def grading_students(grades):
    final_grades = []
    for i in grades:
        if i < 38:
            final_grades.append(i)
            continue
        else:
            if i % 5 >= 1:
                approx_value = approx_num(i)
                approx_grade = approx_value - i
                if approx_grade < 3:
                    final_grades.append(approx_value)
                else:
                    final_grades.append(i)
            else:
                final_grades.append(i)

    return final_grades


                

def approx_num(grade):
     checks = [1, 2, 3, 4]
     for i in checks:
         if (grade + i) % 5 == 0:
             return grade + i


#you can add or change the test case.
test = [73, 38, 67, 33]
print(grading_students(test))






