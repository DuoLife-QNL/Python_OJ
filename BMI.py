weight, height = map(float, input().split())

bmi = weight / (height ** 2)

if bmi < 18.5:
    grade = 'A'
elif 18.5 <= bmi < 24:
    grade = 'B'
elif 24 <= bmi < 28:
    grade = 'C'
else:
    grade = 'D'

print("{}:{:.2f}".format(grade, bmi))