import numpy as np

def horner(x, func=[]):
    n = len(func)
    der = [0 for i in range(len(func) - 1)]
    i = 0
    y = 0
    print("Coefficients of P(t):")
    print(func)

    for i in range(n):
        y = func[i] + y
        if i + 1 < len(func):
            der[i] = y
            y = y * x

    print("\nP(4) = ")
    print(y)
    print("\nCoefficients of P'(t):")
    print(der)

    y = 0
    for i in range(len(der)):
        y = der[i] + y
        if i + 1 < len(der):
            y = y * x

    print("\nP'(4) = ")
    print(y)
    print("\n")


# Test Cases
#   The int array "coeff" are the list of coefficients of the input function
#   The int "evalAt" will evaluate the function at that value, as well as its derivative.

#   Testing p(x) = 4x^4 - 5x^3 + 6x^2 - 7x + 8 at X=3
coeff = [4, -5, 6, -7, 8]
evalAt = 3
horner(evalAt, coeff)

#   Testing p(x) = 2x^5 - 3x^4 + 4x^3 - 20x^2 + 18x + 32 at X=2
coeff = [2, -3, 4, -20, 18, 32]
evalAt = 2
horner(evalAt, coeff)

