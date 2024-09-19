# Number of labs or quizzes completed
completed_labs = int(input("Enter the number of labs completed: "))
completed_quizzes = int(input("Enter the number of quizzes completed: "))

# Grades for assignments
assignment_1 = float(input("Enter grade for Assignment 1: "))
assignment_2 = float(input("Enter grade for Assignment 2: "))
assignment_3 = float(input("Enter grade for Assignment 3: "))
assignment_4 = float(input("Enter grade for Assignment 4: "))

# Grades for midterms and final
midterm_1 = float(input("Enter grade for Midterm 1: "))
midterm_2 = float(input("Enter grade for Midterm 2: "))
final_exam = float(input("Enter grade for Final Exam: "))

# Grades for midterm and final preparation
preparation_grade = float(input("Enter grade for Midterms and Final Preparation: "))


# Weights
lab_weight = 0.20
quiz_weight = 0.15
assignment_weight = 0.16
midterm_weight = 0.25
final_weight = 0.18
preparation_weight = 0.06


# Grade for course
course_grade = ((completed_labs/6) * 100 * lab_weight) + ((completed_quizzes/6) * 100 * quiz_weight) + (((assignment_1 + assignment_2 + assignment_3 + assignment_4)/4) * assignment_weight) + (((midterm_1 + midterm_2)/2) * midterm_weight) + (final_exam * final_weight) + (preparation_grade * preparation_weight)
grade_rounded = round(course_grade, 2)


print(f"Your grade for this course is {grade_rounded}")

