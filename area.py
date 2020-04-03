import math
print("code to print area and perimeter of circle")
radius=float(input("enter the radius of tge circle:"))
area=math.pi*(radius**2)
perimeter=2*math.pi*radius
print(f"area of circle is:",round(area,6)) 
print(f"and the perimeter of circle is:",round(perimeter,6))
