number = int(input("Your grade is: "))

if(number<=100 and number>=90):
    grade="A+"
elif(number<=100 and number>=80):
    grade="A"
elif(number<=100 and number>=70):
    grade="B"
elif(number<=100 and number>=60):
    grade="C"
elif(number<=100 and number>=50):
    grade="D"
elif(number<=100 and number>=40):
    grade="E"

print("your grade is ", grade)