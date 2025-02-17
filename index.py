import numpy as np
import math
from math import factorial
from math import comb
from math import sqrt
import fractions
from fractions import Fraction
from matplotlib import pyplot as plt
import sympy as sy
from sympy import fibonacci
import matplotlib.pyplot as plt
import itertools
import operator

print("Welcome to MATRIXNumber Python Calculator!")
print("This is version 1.5; make sure to check for updates!")
print("")
print("Services available:")
print("1.  Find all Factors")
print("2.  Calculate the nth Power")
print("3.  Calculate the nth Root")
print("4.  Display Rows of Pascal's Triangle")
print("5.  Convert Degrees and Radians")
print("6.  Calculate for Logarithms")
print("7.  Calculate Matrix / Matrices")
print("8.  Calculate for Pythagoream Theorum")
print("9.  Calculate Triginomic Functions")
print("10. Calculate for Surface Area")
print("11. Calculate for Volume")
print("12. Calculate Permutation")
print("13. Calculate Combination")
print("14. Add, Subtract, Multiply, and Divide Fractions")
print("15. Quadratic Formula")
print("16. Multiplication / Division")
print("17. Distance Formula")
print("18. Synthetic Division")
print("19. Convert Decimals and Fractions")
print("20. Display Fibonacci Sequence")
choice1 = int(input("Choose a service: "))
if (choice1 == 1):
    N = int(input("Enter a number to be factored: "))
    for x in range (1, N + 1):
        if N % x == 0:
            print(x, end=" ")
                            
elif (choice1 == 2):
    N = float(input("Enter a number to be put to the nth power: "))
    m = float(input("Enter the nth power: "))

    num = np.power(N, m)
    print(num)
        

elif (choice1 == 3):
    N = int(input("Enter a number to be rooted to the nth power: "))
    m = int(input("Enter the nth root: "))

    a = N
    n = m
    print(np.power(a, (1/n)))

elif (choice1 == 4):
    N = int(input("Enter a row of Pascal's Triangle: "))
    for i in range(N):
        for j in range(N - i + 1):
            print(end=" ")

        for j in range(i + 1):
            print(factorial(i)//(factorial(j) * factorial(i - j)), end=" ")

        print("\n")

elif (choice1 == 5):
    print("Services available:")
    print("1. Degrees -> Radians")
    print("2. Radians -> Degrees")
    N = int(input("Choose a service: "))
    if (N == 1):
        d = float(input("Enter the angle in degrees: "))

        r = float(d * (math.pi / 180))
        print(r)

    elif (N == 2):
        r = float(input("Enter the angle in radians: "))

        d = float(r * (180 / math.pi))
        print(d)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 6):
    N = input("Does your logarithm have a base? [Y / n]: ")
    if (N == 'Y'):
        a = float(input("Enter the Argument: "))
        b = float(input("Enter the Logarithm Base: "))

        print(math.log(a, b))

    elif (N == 'n'):
        a = float(input("Enter the Argument: "))
        x = float(input("Enter the Exponent: "))

        print(math.log(a, exp(x)))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 7):
    print("Operators available:")
    print("Currently, only Multiplication is supported")
    print("1. Multiplication")
    N = int(input("Select an operator: "))
    if (N == 1):
        matrix_a_row = int(input("Enter the number of rows for Matrix A: "))
        matrix_a_col = int(input("Enter the number of columns for Matrix A: "))
        
        matrix_b_row = int(input("Enter the number of rows for Matrix B: "))
        matrix_b_col = int(input("Enter the number of columns for Matrix B: "))

        if (matrix_a_col == matrix_b_row):
            print("Enter values for Matrix A:")
            matrix_a = [[int(input(f"column {j + 1} -> Enter {i + 1} element:")) for j in range(matrix_a_col)] for i in range(matrix_a_row)]
            
            print("Enter values for Matrix B:")
            matrix_b = [[int(input(f"column {j + 1} -> Enter {i + 1} element:")) for j in range(matrix_a_col)] for i in range(matrix_b_row)]

            print("Matrix-A")
            for i in matrix_a:
                print(i)

            print()

            print("Matrix-B")
            for i in matrix_b:
                print(i)

            result = [[0 for j in range(matrix_b_col)] for i in range(matrix_a_row)]

            for i in range(len(matrix_a)):
                for j in range(len(matrix_b[0])):
                    for k in range(len(matrix_b)):
                       result[i][j] += matrix_a[i][k] * matrix_b[k][j]

            print("The product of Matrix-A and Matrix-B:")
            for i in result:
                print(i)
        
        else:
            print("Multiplication of these matrices is not possible (columns of matrix-a = row of matrix-b)")

elif (choice1 == 8):
    print("Services available:")
    print("1. a^2 + b^2 = c^2")
    print("2. c^2 - a^2 = b^2")
    N = int(input("Choose a service: "))
    if (N == 1):
        a = float(input("Enter the 'a' value: "))
        b = float(input("Enter the 'b' value: "))
        
        A = np.power(a, 2)
        B = np.power(b, 2)

        C = A + B
        c = np.sqrt(C)
        print(c)

    elif (N == 2):
        a = float(input("Enter the 'a' value: "))
        c = float(input("Enter the 'c' value: "))

        A = np.power(a, 2)
        C = np.power(c, 2)

        B = C - A
        b = np.sqrt(B)
        print(b)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 9):
    print("Services available:")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Asin")
    print("5. Acos")
    print("6. Atan")
    N = int(input("Chose a service: "))
    if (N == 1):
        print("Services available:")
        print("1. Sin with degrees")
        print("2. Sin with radians")
        n = int(input("Chose a service: "))
        if (n == 1):
            X = float(input("Enter the angle in degrees: "))
            x = float(X * (math.pi / 180))

            print(math.sin(x))

        elif (n == 2):
            x = float(input("Enter the angle in radians [use 3.14159 for pi]: "))

            print(math.sin(x))

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (n == 2):
        print("Services available:")
        print("1. Cos with degrees")
        print("2. Cos with radians")
        nn = int(input("Chose a service: "))
        if (nn == 1):
            X = float(input("Enter the angle in degrees: "))
            x = float(X * (math.pi / 180))

            print(math.cos(x))

        elif (nn == 2):
            x = float(input("Enter the angle in radians [use 3.14159 for pi]: "))

            print(math.cos(x))

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (n == 3):
        print("Services available:")
        print("1. Tan with degrees")
        print("2. Tan with radians")
        nn = int(input("Chose a service: "))
        if (nn == 1):
            X = float(input("Enter the angle in degrees: "))
            x = float(X * (math.pi / 180))

            print(math.tan(x))

        elif (nn == 2):
            x = float(input("Enter the angle in radians [use 3.14159 for pi]: "))

            print(math.tan(x))

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (n == 4):
        X = float(input("Enter the arcsin [-1 - 1]: "))

        print(math.asin(X))

    elif (n == 5):
        X = float(input("Enter the arccos [-1 - 1]: "))

        print(math.acos(X))

    elif (n == 6):
        X = float(input("Enter the arctan [-1 - 1]: "))

        print(math.atan(X))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 10):
    print("Services available:")
    print("1. Surface Area of a Cube")
    print("2. Surface Area of a Prism")
    print("3. Surface Area of a Pyramid")
    print("4. Surface Area of a Hemisphere")
    print("5. Surface Area of a Sphere")
    print("6. Surface Area of a Cylindar")
    print("7. Surface Area of a Cone")
    N = int(input("Chose a service: "))
    if (N == 1):
        l = float(input("Enter the 'length' value: "))
        w = float(input("Enter the 'width' value: "))
        h = float(input("Enter the 'height' value: "))

        x = float((l * w) * 6)
        print(x)

    elif (N == 2):
        print("Services available:")
        print("1. Rectangular Prism")
        print("2. Triangular Prism")
        n = int(input("Chose a service: "))
        if (n == 1):
            l = float(input("Enter the 'length' value: "))
            w = float(input("Enter the 'width' value: "))
            h = float(input("Enter the 'height' value: "))

            x = float(2 * ((l * w) + (l * h) + (w * h)))
            print(x)

        elif (n == 2):
            b = float(input("Enter the 'base length' value: "))
            h = float(input("Enter the 'height' value: "))
            l = float(input("Enter the 'base width' value: "))
            s = float(input("Enter the 'slant height' value: "))

            x = float(2 * (1/2 * b * h) + (2 * l * s) + (l * b))
            print(x)

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (N == 3):
        b = float(input("Enter the 'base' value: "))
        s = float(input("Enter the 's' value: "))

        x = float((2 * b * s) + (b * b))
        print(x)

    elif (N == 4):
        r = float(input("Enter the 'radius' value: "))

        x 

    elif (N == 5):
        r = float(input("Enter the 'radius': "))

        x = float(4 * math.pi() * (r * r))
        print(x)

    elif (N == 6):
        r = float(input("Enter the 'radius' value: "))
        h = float(input("Enter the 'height' value: "))

        x = float((2 * math.pi() * (r * r)) + (2 * math.pi * r * h))
        print(x)

    elif (N == 7):
        r = float(input("Enter the 'radius' value: "))
        s = float(input("Enter the 's' value: "))

        x = float((math.pi() * r * s) + (math.pi() * (r * r)))
        print(x)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 11):
    print("Services available:")
    print("1. Volume of a Cube")
    print("2. Volume of a Prism")
    print("3. Volume of a Pyramid")
    print("4. Volume of a Hemisphere")
    print("5. Volume of a Sphere")
    print("6. Volume of a Cylindar")
    print("7. Volume of a Cone")
    N = int(input("Chose a service: "))
    if (N == 1):
        l = float(input("Enter the 'length' value: "))
        w = float(input("Enter the 'width' value: "))
        h = float(input("Enter the 'height' value: "))

        x = float(l * w * h)
        print(x)

    elif (N == 2):
        print("Services available:")
        print("1. Rectangular Prism")
        print("2. Triangular Prism")
        n = int(input("Chose a service: "))
        if (n == 1):
            l = float(input("Enter the 'length' value: "))
            b = float(input("Enter the 'width' value: "))
            h = float(input("Enter the 'height' value: "))

            x = float(l * b * h)
            print(x)

        elif (n == 2):
            a = float(input("Enter the 'area of base' value: "))
            h = float(input("Enter the 'height' value: "))

            x = float(1/3 * a * h)
            print(x)

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (N == 3):
        a = float(input("Enter the 'area of the base' value: "))
        h = float(input("Enter the 'height' value: "))

        x = float(1/3 * a * h)
        print(x)

    elif (N == 4):
        r = float(input("Enter the 'radius' value: "))

        x = float(2/3 * math.pi() * (r * r * r))
        print(x)

    elif (N == 5):
        r = float(input("Enter the 'radius' value: "))

        x = float(4/3 * (math.pi() * (r * r * r)))
        print(x)

    elif (N == 6):
        r = float(input("Enter the 'radius' value: "))
        h = float(input("Enter the 'height' value: "))

        x = float(math.pi * (r * r) * h)
        print(x)

    elif (N == 7):
        r = float(input("Enter the 'radius' value: "))
        h = float(input("Enter the 'height' value: "))
        
        x = float(1/3 * math.pi() * (r * r) * h)
        print(x)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 12):
    a = int(input("Enter the 'n' value: "))
    b = int(input("Enter the 'k' value: "))

    c = a - b
    x = factorial(a)
    X = factorial(c)
    print(x / X)

elif (choice1 == 13):
    a = int(input("Enter the 'n' value: "))
    b = int(input("Enter the 'k' value: "))

    print(comb(a, b))

elif (choice1 == 14):
    print("Services available:")
    print("1. Addition")
    print("2. Subraction")
    print("3. Multiplication")
    print("4. Division")
    N = int(input("Chose a service: "))
    if (N == 1):
        a = int(input("Enter the 'numerator' value of Fraction 1: "))
        b = int(input("Enter the 'denominator' value of Fraction 1: "))
        c = int(input("Enter the 'numerator' value of Fraction 2: "))
        d = int(input("Enter the 'denominator' value of Fraction 2: "))

        x = fractions.Fraction(a, b)
        y = fractions.Fraction(c, d)
        print(x + y)

    elif (N == 2):
        a = int(input("Enter the 'numerator' value of Fraction 1: "))
        b = int(input("Enter the 'denominator' value of Fraction 1: "))
        c = int(input("Enter the 'numerator' value of Fraction 2: "))
        d = int(input("Enter the 'denominator' value of Fraction 2: "))

        x = fractions.Fraction(a, b)
        y = fractions.Fraction(c, d)
        print(x - y)

    elif (N == 3):
        a = int(input("Enter the 'numerator' value of Fraction 1: "))
        b = int(input("Enter the 'denominator' value of Fraction 1: "))
        c = int(input("Enter the 'numerator' value of Fraction 2: "))
        d = int(input("Enter the 'denominator' value of Fraction 2: "))

        x = fractions.Fraction(a, b)
        y = fractions.Fraction(c, d)
        print(x * y)

    elif (N == 4):
        a = int(input("Enter the 'numerator' value of Fraction 1: "))
        b = int(input("Enter the 'denominator' value of Fraction 1: "))
        c = int(input("Enter the 'numerator' value of Fraction 2: "))
        d = int(input("Enter the 'denominator' value of Fraction 2: "))

        x = fractions.Fraction(a, b)
        y = fractions.Fraction(c, d)
        print(x / y)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 15):
    a = float(input("Enter the 'a' value: "))
    b = float(input("Enter the 'b' value: "))
    c = float(input("Enter the 'c' value: "))

    y = (b ** 2 - (4 * a * c))
    xp = ((-b + (y) ** 0.5) / 2 * a)
    xn = ((-b - (y) ** 0.5) / 2 * a)
    print(f"Discriminent: {y}, Roots: {xp}, {xn}")
    if (y == 0):
        print("One real root")

    elif (y > 0):
        print("Two real roots")

    elif (y < 0):
        print("No real roots")

    else:
        print("Invalid character")
        
elif (choice1 == 16):
    print("Services available:")
    print("1. Multiplication")
    print("2. Division")
    N = int(input("Chose a service: "))
    if (N == 1):
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))

        print(a * b)

    elif (N == 2):
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))

        print(a / b)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 17):
    x1 = float(input("Enter the 'x1' value: "))
    y1 = float(input("Enter the 'y1' value: "))
    x2 = float(input("Enter the 'x2' value: "))
    y2 = float(input("Enter the 'y2' value: "))

    print(math.sqrt(math.exp2(x1 - x2) + math.exp2(y1 - y1)))

elif (choice1 == 18):
    print("This is for quadratic formulas right now")
    a = float(input("Enter the 'a' value: "))
    b = float(input("Enter the 'b' value: "))
    c = float(input("Enter the 'c' value: "))
    d = int(input("Enter the 'root' value: "))

    coefficients = [a, b, c]
    a, b, c = coefficients

    if (len(coefficients) != 3):
        raise ValueError("You must have 3 coefficients")

    x = [a, a * d + b, (a * d + b) * d + c]
    print(f"{coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]} / {d} is {x}")

elif (choice1 == 19):
    print("Services available:")
    print("1. Decimal -> Fraction")
    print("2. Fraction -> Decimal")
    N = int(input("Chose a service: "))
    if (N == 1):
        a = float(input("Enter the decimal: "))

        print(fractions.Fraction(a))

    elif (N == 2):
        a = int(input("Enter the numerator value: "))
        b = int(input("Enter the denominator value: "))

        print(a / b)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 20):
    n = int(input("Enter the number of Fibonacci Sequence to be displayed: "))
    print(fibonacci(n))

else:
    print("ERROR: Please enter a valid number from the menu above")
