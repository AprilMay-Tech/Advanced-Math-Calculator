import numpy as np
import math
from math import factorial

print("Welcome to MATRIXNumber Python Calculator!")
print("Services available:")
print("1. Find all factors")
print("2. Calculate the nth power")
print("3. Calculate the nth root")
print("4. Display rows of Pascal's Triangle")
print("5. Convert Degrees and Radians")
print("6. Calculate for Logarithms")
print("7. Calculate Matrix / Matrices")
choice1 = int(input("Choose a service: "))
if (choice1 == 1):
    N = int(input("Enter a number to be factored: "))
    for x in range (1, N + 1):
        if N % x == 0:
            print(x, end=" ")
                            
elif (choice1 == 2):
    N = int(input("Enter a number to be put to the nth power: "))
    m = int(input("Enter the nth power: "))

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
    N = int(input("Does your logarithm have a base? [1 = Y / 2 = n]: "))
    if (N == 1):
        a = float(input("Enter the Logarithm: "))
        b = float(input("Enter the Logarithm Base: "))

        print(math.log(a, b))

    elif (N == 2):
        a = float(input("Enter the Logarithm: "))

        print(math.log(a))

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

else:
    print("ERROR: Please enter a valid number from the menu above")
