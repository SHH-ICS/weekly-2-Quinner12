import math
while True:
    print("Please Input, Diameter") 
    Diameter = int(input(""))
    if Diameter < 0:
        print("Diameter must be positive")
        continue

    break
Circumference = Diameter * math.pi
Area = 1/4* math.pi * Diameter ** 2
print("The circumference is") 
print (Circumference)
print("The Area is") 
print (Area)