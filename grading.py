def grading(homework, assessment, final_exam):
    percentageh = homework/25 *100
    percentagea = assessment/50 *100
    percentagef = final_exam/100 *100
    average = (percentageh + percentagea + percentagef)//3
    if average >= 70:
        letter = 'A'
    elif average >= 60:
        letter = 'B'
    elif average >= 50:
        letter = 'C'
    elif average >= 40:
        letter = 'D'
    else:
        letter = 'E'
    return average, letter

name = input('What is the student name? ')
homework_grade = int(input('What is the homework score? '))
assessment_grade = int(input('What is the assessment score? '))
final_exam_grade = int(input('What is the final exam score? '))

score = grading(homework_grade, assessment_grade, final_exam_grade)

print(f"The student's name is {name} and their score final grade was {score[0]}% giving you a {score[1]}")