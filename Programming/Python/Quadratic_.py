import math
class Quadratic:

    a = int()
    b = int()
    c = int()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def getc(self):
        return self.c

    def evaluate(self,x):
        return((self.a * (x * x)) + (self.b * (x))+ self.c)
    def discriminant(self):
        return (self.b * self.b - (4 * self.a * self.c))

    def isImaginaryRoots(self):
        discriminant = self.discriminant()
        return discriminant < 0

    def isRealRoots(self):
        discriminant = self.discriminant()
        return discriminant >= 0

    def firstRoot(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        elif discriminant == 0:
            return - self.b / (2 * self.a)
        else:
            x1 = ((-self.b + math.sqrt(self.discriminant()) / (2 * self.a)) * 1)
            x2 = ((-self.b + math.sqrt(self.discriminant()) / (2 * self.a)) * -1)
            return min(x1, x2)

    def secondRoot(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        elif discriminant == 0:
            return - self.b / (2 * self.a)
        else:
            x1 = ((-self.b + math.sqrt(self.discriminant()) / (2 * self.a)) * 1)
            x2 = ((-self.b + math.sqrt(self.discriminant()) / (2 * self.a)) * -1)
            return max(x1, x2)

    def isPerfectSquare(self):
        x1 = self.firstRoot()
        x2 = self.secondRoot()
        if x1 is not None and x2 is not None and x1 == x2:
            return True
        else:
            return False



a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
Math = Quadratic(a,b,c)

print()
print("Quadratic Expression:", f"{a}x2+{b}x+{c}")

if Math.isImaginaryRoots():
    print("The roots are imaginary")
else:
    x1 = Math.firstRoot()
    x2 = Math.secondRoot()
    print(f"The roots are real: x1 =", x2, "; x2 =", x1)

if Math.isPerfectSquare():
    print("It is a perfect square")
else:
    print("It is not a perfect square.")

print()
print("Evaluating the expression:")
x = int(input("Enter x: "))
result = Math.evaluate(x)
print("Result:", result)