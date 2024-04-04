import math
while True:
    print("Please Input, Diameter") 
    Diameter = int(input(""))
    if Diameter < 0:
        print("Diameter must be positive")
        continue

    break
circumference = Diameter * math.pi
Area = 1/4* math.pi * Diameter ** 2
print("The circumference is") 
print (circumference)
print("The Area is") 
print (Area)