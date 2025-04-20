marks = {                     
    "Harry" : 100,             
    "Aiaby" : 200,              
    "esha"  : 300, 
     0 : "Aibay"            
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({'Harry': 99, "Renuka" :55})
print(marks)
#Differe
print(marks.get("Harry2"))  #None
# print(marks["Harry2"])    #Error

print(marks.pop("Harry"))  # Output: 3
print(marks)  # Output: {'a': 1, 'c': 4}


