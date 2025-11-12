w = float(input("Enter width:"))
h = float(input("Enter height:"))
b = float(input("Enter base:"))

A = 1/2 * b * h

print(f"Area of Triangle: {A}")

if w == h == b:
    print("Equilateral Triangle")
elif w == h or w == b or b == h:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")