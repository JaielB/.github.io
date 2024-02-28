letter_grade = 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'
grade = int(input('Enter a number grade: '))

if 93 <= grade <= 100:
    letter_grade = 'A'

if 90 <= grade <= 92:
    letter_grade = 'A-'

if 87 <= grade <= 89:
    letter_grade = 'B+'

if 83 <= grade <= 86:
    letter_grade = 'B'

if 80 <= grade <= 82:
    letter_grade = 'B-'

if 77 <= grade <= 79:
    letter_grade = 'C+'

if 73 <= grade <= 76:
    letter_grade = 'C'

if 70 <= grade <= 72:
    letter_grade = 'C-'

if 67 <= grade <= 69:
    letter_grade = 'D+'

if 63 <= grade <= 66:
    letter_grade = 'D'

if 60 <= grade <= 62:
    letter_grade = 'D-'

if 60 > grade:
    letter_grade = 'F'
print(f'Your letter grade for {grade} is {letter_grade}.')