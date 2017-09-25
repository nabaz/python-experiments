# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .
# Student 1 received a  73, and the next multiple of 5  from 73 is 73. Since 75-73 < 3 , the student's grade is rounded to 75.
# Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70-67 = 3, the grade will not be modified and the student's final grade is 67.
# Student 3 received a 38 , and the next multiple of 5 from  38 is 40. Since 40-38 < 3, the student's grade will be rounded to 40.
# Student 4 received a grade below 38, so the grade will not be modified and the student's final grade is 33.

def solve(grade):
    result = []
    for i in grade:
        if i >= 38 and grade < 40:
            result.append(40)
        elif i % 10 >= 3 and i % 10 < 5 and i > 40:
            result.append(i + (5 - (i % 10)))
        else:
            result.append(i)
            
    print(result)


a = [23, 80, 96, 18, 73, 78, 60, 60, 15, 44, 15, 10, 5, 46, 84, 33, 60, 14, 71, 65, 2, 5, 97, 0]
s = solve(a)
