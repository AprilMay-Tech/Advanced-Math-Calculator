import numpy as np
import math
from math import factorial
from math import comb
import fractions
from fractions import Fraction

print("Welcome to the AprilMay, Tech MathCalculator!")
print("This is version 2.0, make sure to check for updates")
print("Services Available:")
print("Operators")
print("1.  Add large factors")
print("2.  Subtract large factors")
print("3.  Multiply large factors")
print("4.  Divide large factors")
print("5.  Synthetic Division")
print("Find Factors / Primes")
print("6.  Find all Factors")
print("7.  Determine if a number is prime")
print("Calculate Powers and Roots")
print("8.  Calculate the nth Power")
print("9. Calculate the nth Root")
print("10. Display Rows of Pascal's Triangle")
print("Convert Numbers")
print("11. Convert Decimals and Fractions")
print("12. Convert Degrees and Radians")
print("Calculate Formulas")
print("13. Calculate Logarithms")
print("14. Quadratic Formula")
print("15. Distance Formula")
print("16. Pythagoreum Theorum")
print("Display Mathematical Figures")
print("17. Display to the nth row of Pascal's Triangle")
print("18. Display to the nth number of Fibonacci Sequence")
print("Calculate SA and Volume")
print("19. Calculate Lateral Surface Area")
print("20. Calculate Total Surface Area")
print("21. Calculate Volume")
print("Sine, Cosine, and Tangent")
print("22. Calculate Sine")
print("23. Calculate Cosine")
print("24. Calculate Tangent")
print("25. Calculate Asine")
print("26. Calculate Acosine")
print("27. Calculate Atangent")
print("Permutations and Combinations")
print("28. Calculate Permutations")
print("29. Calculate Combinations")
print("Fraction Operators")
print("30. Add Fractions")
print("31. Subtract Fractions")
print("32. Multiply Fractions")
print("33. Divide Fractions")
choice1 = int(input("Choose a service:\n"))
if (choice1 == 1):
    a = int(input("Enter the first value:\n"))
    b = int(input("Enter the second value:\n"))
    print(a + b)

elif (choice1 == 2):
    a = int(input("Enter the first value:\n"))
    b = int(input("Enter the second value:\n"))
    print(a - b)

elif (choice1 == 3):
    a = int(input("Enter the first value:\n"))
    b = int(input("Enter the second value:\n"))
    print(a * b)

elif (choice1 == 4):
    a = int(input("Enter the first value:\n"))
    b = int(input("Enter the second value:\n"))
    print(a / b)

elif (choice1 == 5):
    print("Choose what kind of equation is used:")
    print("1. Quadratic Equation")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        a = float(input("Enter the 'a' value:\n"))
        b = float(input("Enter the 'b' value:\n"))
        c = float(input("Enter the 'c' value:\n"))
        d = float(input("Enter the 'root' value:\n"))
        coefficients = [a, b, c]
        a, b, c = coefficients
        if (len(coefficients) != 3):
            raise ValueError("You must have 3 coefficients")
        x = [a, a * d + b, (a * d + b) * d + c]
        print(f"{coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]} / {d} is {x}")

elif (choice1 == 6):
    N = int(input("Enter a number to be factored:\n"))
    for x in range (1, N + 1):
        if N % x == 0:
            print(x, end=" ")

elif (choice1 == 7):
    n = input("Enter the number to be checked:\n")
    if (n % 2 == 0):
        print(f"{n} is not a Prime Number")

    elif (n == 2):
        print(f"{n} is a Prime Number")

    else:
        is_prime = True
        for i in range(3, n, 2):
            if n % i == 0:
                is_prime = False
                break
        
        if (is_prime):
            print(f"{n} is a Prime Number")

        else:
            print(f"{n} is not a Prime Number")

elif (choice1 == 8):
    a = float(input("Enter the base:\n"))
    b = float(input("Enter the power:\n"))
    print(a ** b)

elif (choice1 == 9):
    a = float(input("Enter the base:\n"))
    b = float(input("Enter the index:\n"))
    c = np.reciprocal(b)
    print(a ** c)

elif (choice1 == 10):
    N = int(input("Enter a row of Pascal's Triangle:\n"))
    for i in range(N):
        for j in range(N - i + 1):
            print(end=" ")

        for j in range(i + 1):
            print(factorial(i)//(factorial(j) * factorial(i - j)), end=" ")

        print("\n")

elif (choice1 == 11):
    print("Services Available:")
    print("1. Decimals -> Fractions")
    print("2. Fractions -> Decimals")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        a = float(input("Enter the number to be converted:\n"))
        print(fractions.Fraction(a))

    elif (N == 2):
        a = int(input("Enter the numerator:\n"))
        b = int(input("Enter the denominator:\n"))
        print(a / b)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 12):
    print("Services available:")
    print("1. Degrees -> Radians")
    print("2. Radians -> Degrees")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        d = float(input("Enter the angle in degrees:\n"))
        r = float(d * (math.pi / 180))
        print(r)

    elif (N == 2):
        r = float(input("Enter the angle in radians:\n"))
        d = float(r * (180 / math.pi))
        print(d)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 13):
    b = float(input("Enter the 'base' value:\n"))
    x = float(input("Enter the 'exponent' value:\n"))
    print(math.log(b, x))

elif (choice1 == 14):
    a = float(input("Enter the 'a' value:\n"))
    b = float(input("Enter the 'b' value:\n"))
    c = float(input("Enter the 'c' value:\n"))
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

elif (choice1 == 15):
    x1 = float(input("Enter the 'x1' value:\n"))
    y1 = float(input("Enter the 'y1' value:\n"))
    x2 = float(input("Enter the 'x2' value:\n"))
    y2 = float(input("Enter the 'y2' value:\n"))
    print(math.sqrt(math.exp2(x1 - x2) + math.exp2(y1 - y1)))

elif (choice1 == 16):
    print("Services available:")
    print("1. a^2 + b^2 = c^2")
    print("2. c^2 - a^2 = b^2")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        a = float(input("Enter the 'a' value:\n"))
        b = float(input("Enter the 'b' value:\n"))
        A = np.power(a, 2)
        B = np.power(b, 2)
        C = A + B
        c = np.sqrt(C)
        print(c)

    elif (N == 2):
        a = float(input("Enter the 'a' value:\n"))
        c = float(input("Enter the 'c' value:\n"))
        A = np.power(a, 2)
        C = np.power(c, 2)
        B = C - A
        b = np.sqrt(B)
        print(b)

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 17):
    N = int(input("Enter a row of the Pascal Triangle to display to:\n"))
    for i in range(N):
        for j in range(N - i + 1):
            print(end=" ")

        for j in range(i + 1):
            print(factorial(i)//(factorial(j) * factorial(i - j)), end=" ")

        print("\n")

elif (choice1 == 18):
    def fib(N, prev1, prev2):
        if (N < 3):
            return
        
        fn = prev1 + prev2
        prev2 = prev1
        prev1 = fn
        print(fn, end="")
        fib(n - 1, prev1, prev2)

    def print_fib(N):
        if (N < 1):
            print("ERROR: This number is invalid")

        elif (N == 1):
            print("0")

        elif (N == 2):
            print("0 1")

        else:
            print("0 1", end="")
            fib(n, 1, 0)

        if __name__ == "__main__":
            N = int(input("Enter the number of Fibonacci Sequence to be displayed:\n"))

elif (choice1 == 19):
    print("Services available:")
    print("1. Lateral Surface Area of a Cube")
    print("2. Lateral Surface Area of a Prism")
    print("3. Lateral Surface Area of a Pyramid")
    print("4. Lateral Surface Area of a Hemisphere")
    print("5. Lateral Surface Area of a Sphere")
    print("6. Lateral Surface Area of a Cylindar")
    print("7. Lateral Surface Area of a Cone")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        l = float(input("Enter the 'length' value:\n"))
        print(float(l ** 4))

    elif (N == 2):
        l = float(input("Enter the 'length' value:\n"))
        w = float(input("Enter the 'width' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print((h * 2) * (l + w))

    elif (N == 3):
        b = float(input("Enter the 'base perimiter' value:\n"))
        s = float(input("Enter the 'slant height' value:\n"))
        print(float(1/2 * b * s))

    elif (N == 4):
        r = float(input("Enter the 'radius' value:\n"))
        print(float(2 * math.pi() * (r ** 2)))

    elif (N == 5):
        r = float(input("Enter the 'radius' value:\n"))
        print(float(4 * math.pi() * (r ** 2)))

    elif (N == 6):
        h = float(input("Enter the 'height' value:\n"))
        r = float(input("Enter the 'radius' value:\n"))
        print(float(2 * math.pi() * r * h))

    elif (N == 7):
        h = float(input("Enter the 'height' value:\n"))
        s = float(input("Enter the 'slant height' value:\n"))
        r = float(input("Enter the 'radius' value:\n"))
        print(float(math.pi() * r * s))

elif (choice1 == 20):
    print("Services available:")
    print("1. Total Surface Area of a Cube")
    print("2. Total Surface Area of a Prism")
    print("3. Total Surface Area of a Pyramid")
    print("4. Total Surface Area of a Hemisphere")
    print("5. Total Surface Area of a Sphere")
    print("6. Total Surface Area of a Cylindar")
    print("7. Total Surface Area of a Cone")
    N = int(input("Choose a service:\n"))
    if (N == 1):
        l = float(input("Enter the 'length' value:\n"))
        print(float((l ** 6)))

    elif (N == 2):
        print("Services available:")
        print("1. Rectangular Prism")
        print("2. Triangular Prism")
        n = int(input("Chose a service:\n"))
        if (n == 1):
            l = float(input("Enter the 'length' value:\n"))
            w = float(input("Enter the 'width' value:\n"))
            h = float(input("Enter the 'height' value:\n"))
            print(float(2 * ((l * w) + (l * h) + (w * h))))

        elif (n == 2):
            b = float(input("Enter the 'base length' value: "))
            h = float(input("Enter the 'height' value: "))
            l = float(input("Enter the 'base width' value: "))
            s = float(input("Enter the 'slant height' value: "))
            print(float(2 * (1/2 * b * h) + (2 * l * s) + (l * b)))

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (N == 3):
        b = float(input("Enter the 'base perimiter' value:\n"))
        s = float(input("Enter the 'slant height' value:\n"))
        print(float((2 * b * s) + (b * b)))

    elif (N == 4):
        r = float(input("Enter the 'radius' value:\n"))
        print(float(r ** 3))

    elif (N == 5):
        r = float(input("Enter the 'radius':\n"))
        print(float(4 * math.pi() * (r ** 2)))

    elif (N == 6):
        r = float(input("Enter the 'radius' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print(float((2 * math.pi() * (r * r)) + (2 * math.pi * r * h)))

    elif (N == 7):
        r = float(input("Enter the 'radius' value:\n"))
        s = float(input("Enter the 'slant height' value:\n"))
        print(float((math.pi() * r * s) + (math.pi() * (r * r))))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 21):
    print("Services available:")
    print("1. Volume of a Cube")
    print("2. Volume of a Prism")
    print("3. Volume of a Pyramid")
    print("4. Volume of a Hemisphere")
    print("5. Volume of a Sphere")
    print("6. Volume of a Cylindar")
    print("7. Volume of a Cone")
    N = int(input("Chose a service:\n"))
    if (N == 1):
        l = float(input("Enter the 'length' value:\n"))
        w = float(input("Enter the 'width' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print(float(l * w * h))

    elif (N == 2):
        print("Services available:")
        print("1. Rectangular Prism")
        print("2. Triangular Prism")
        n = int(input("Chose a service:\n"))
        if (n == 1):
            l = float(input("Enter the 'length' value:\n"))
            b = float(input("Enter the 'width' value:\n"))
            h = float(input("Enter the 'height' value:\n"))
            print(float(l * b * h))

        elif (n == 2):
            a = float(input("Enter the 'area of base' value:\n"))
            h = float(input("Enter the 'height' value:\n"))
            print(float(1/3 * a * h))

        else:
            print("ERROR: Please enter a valid number from the menu above")

    elif (N == 3):
        a = float(input("Enter the 'area of the base' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print(float(1/3 * a * h))

    elif (N == 4):
        r = float(input("Enter the 'radius' value:\n"))
        print(float(2/3 * math.pi() * (r ** 3)))

    elif (N == 5):
        r = float(input("Enter the 'radius' value:\n"))
        print(float(4/3 * (math.pi() * (r ** 3))))

    elif (N == 6):
        r = float(input("Enter the 'radius' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print(float(math.pi * (r ** 2) * h))

    elif (N == 7):
        r = float(input("Enter the 'radius' value:\n"))
        h = float(input("Enter the 'height' value:\n"))
        print(float(1/3 * math.pi() * (r * r) * h))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 22):
    print("Services available:")
    print("1. Sin with degrees")
    print("2. Sin with radians")
    N = int(input("Chose a service:\n"))
    if (N == 1):
       X = float(input("Enter the angle in degrees:\n"))
       x = float(X * (math.pi / 180))
       print(math.sin(x))

    elif (N == 2):
       x = float(input("Enter the angle in radians [use 3.14159 for pi]:\n"))
       print(math.sin(x))

    else:
       print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 23):
    print("Services available:")
    print("1. Cos with degrees")
    print("2. Cos with radians")
    N = int(input("Chose a service:\n"))
    if (N == 1):
        X = float(input("Enter the angle in degrees:\n"))
        x = float(X * (math.pi / 180))
        print(math.cos(x))

    elif (N == 2):
        x = float(input("Enter the angle in radians [use 3.14159 for pi]:\n"))
        print(math.cos(x))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 24):
    print("Services available:")
    print("1. Tan with degrees")
    print("2. Tan with radians")
    N = int(input("Chose a service:\n"))
    if (N == 1):
        X = float(input("Enter the angle in degrees:\n"))
        x = float(X * (math.pi / 180))
        print(math.tan(x))

    elif (N == 2):
        x = float(input("Enter the angle in radians [use 3.14159 for pi]:\n"))
        print(math.tan(x))

    else:
        print("ERROR: Please enter a valid number from the menu above")

elif (choice1 == 25):
    print("")
    X = float(input("Enter the arcsin [-1 - 1]:\n"))
    print(math.asin(X))

elif (choice1 == 26):
    X = float(input("Enter the arccos [-1 - 1]:\n"))
    print(math.acos(X))

elif (choice1 == 27):
    X = float(input("Enter the arctan [-1 - 1]:\n"))
    print(math.atan(X))

elif (choice1 == 28):
    n = float(input("Enter the base value:\n"))
    k = float(input("Enter the modifying value:\n"))
    a = n - k
    x = factorial(n)
    X = factorial(a)
    print(x / X)

elif (choice1 == 29):
    n = float(input("Enter the base value:\n"))
    k = float(input("Enter the modifying value:\n"))
    print(comb(n, k))

elif (choice1 == 30):
    a = int(input("Enter the 'numerator' value of Fraction 1:\n"))
    b = int(input("Enter the 'denominator' value of Fraction 1:\n"))
    c = int(input("Enter the 'numerator' value of Fraction 2:\n"))
    d = int(input("Enter the 'denominator' value of Fraction 2:\n"))
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x + y)

elif (choice1 == 31):
    a = int(input("Enter the 'numerator' value of Fraction 1:\n"))
    b = int(input("Enter the 'denominator' value of Fraction 1:\n"))
    c = int(input("Enter the 'numerator' value of Fraction 2:\n"))
    d = int(input("Enter the 'denominator' value of Fraction 2:\n"))
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x - y)

elif (choice1 == 32):
    a = int(input("Enter the 'numerator' value of Fraction 1:\n"))
    b = int(input("Enter the 'denominator' value of Fraction 1:\n"))
    c = int(input("Enter the 'numerator' value of Fraction 2:\n"))
    d = int(input("Enter the 'denominator' value of Fraction 2:\n"))
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x * y)

elif (choice1 == 33):
    a = int(input("Enter the 'numerator' value of Fraction 1:\n"))
    b = int(input("Enter the 'denominator' value of Fraction 1:\n"))
    c = int(input("Enter the 'numerator' value of Fraction 2:\n"))
    d = int(input("Enter the 'denominator' value of Fraction 2:\n"))
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x / y)

else:
    print("ERROR: Please enter a valid number from the menu above")
