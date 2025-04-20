s = {1 , 2, 2, 2, 2, 6, 7}
                        #Properties
print(s,type(s))        #can't change existing item
s.add(566)              #unordered 
print(s, type(s))       #unidexed
s.remove(2)             #can't index items
print(s) 
s.clear() 
print(s)   

s = {8, 9, 6, 7}
s1 = {7,6,2,0}

print(s.union(s1))
print(s.intersection(s1))



