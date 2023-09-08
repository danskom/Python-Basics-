#quadratic equations

import math



a = -4  # Coefficient for x^2
b = 12  # Coefficient for x
c = 1.5  # Constant term

discriminant = b**2 - 4*a*c

print(discriminant)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The equation has two real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The equation has one real root: {root}")
else:
    print("The equation has no real roots")
