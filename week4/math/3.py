import math

a = int(input("Input number of sides: "))
b = float(input("Input lenght of side: "))

area = (a * b**2) / (4 * math.tan(math.pi / a))
print("Area:", round(area, 2))