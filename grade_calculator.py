# TechRise 3.0 - Student Grade Calculator

# 1. Accept Inputs
student_name = input("Enter Student Name: ")

english_score = float(input("Enter English Score: "))
math_score = float(input("Enter Mathematics Score: "))
computer_score = float(input("Enter Computer Science Score: "))

# 2. Calculate Total and Average
total_score = english_score + math_score + computer_score
average_score = total_score / 3

# 3. Determine Grade based on Average
if average_score >= 70 and average_score <= 100:
    grade = 'A'
elif average_score >= 60:
    grade = 'B'
elif average_score >= 50:
    grade = 'C'
elif average_score >= 45:
    grade = 'D'
elif average_score >= 40:
    grade = 'E'
else:
    grade = 'F'

# 4. Display Results
print("\n======= STUDENT RESULT =======")
print(f"Student Name  : {student_name}")
print(f"Total Score   : {total_score:.2f}")
print(f"Average Score : {average_score:.2f}")
print(f"Grade         : {grade}")
print("==============================")