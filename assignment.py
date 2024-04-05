import math
while True:
    print("Please Input, Diameter") 
    Diameter = int(input(""))
    if Diameter < 0:
        print("Diameter must be positive")
        continue

    break
circumference = Diameter * math.pi
area = 1/4* math.pi * Diameter ** 2
Circumference = round(circumference)
Area = round(area)
print("The Circumference is") 
print (Circumference)
print("The Area is") 
print (Area)