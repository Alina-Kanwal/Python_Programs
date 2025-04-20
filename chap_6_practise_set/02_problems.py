marks1 = int(input('Enter Marks 1: '))
marks2 = int(input('Enter Marks 1: '))
marks3 = int(input('Enter Marks 1: '))

total_percantage = (100*(marks1 + marks2 + marks3)) / 2

if(total_percantage>=40 and marks1>33 and marks2>33 and marks3>33):
  print("You are passed")

else:
  print("You are failed")  