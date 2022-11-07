marks=int(input('Enter your number: '))

def showGrade(grade):
  print(f"you got: {grade}")


if marks>=80:
  showGrade('A+')
elif marks<80 and marks>=70:
  showGrade('A')
elif marks<70 and marks>=60:
  showGrade('A-')
elif marks>=33:
  showGrade('passed')
else:
  showGrade('F')