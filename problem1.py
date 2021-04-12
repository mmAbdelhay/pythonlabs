import math

x1 = int(input("plese enter x1 : "))
x2 = int(input("plese enter x2 : "))
y1 = int(input("plese enter y1 : "))
y2 = int(input("plese enter y2 : "))

distance = float(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))

print(distance)
