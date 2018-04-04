import numpy as np





def bisection(equation, boundOne, boundTwo):
    for i in range(0, 20):
        mid = (boundOne + boundTwo) / 2.0
        if (equation(boundOne) * equation(mid) > 0):
            boundOne = mid
        else:
            boundTwo = mid

    return mid


def newton(equation, derivative, boundOne):
    errorEstimate = 0.000001
    for i in range(0, 80):
        if (abs(equation(boundOne)) < errorEstimate):
            return boundOne
        else:
            boundOne = boundOne - equation(boundOne) / derivative(boundOne)


def secant(equation, boundOne, boundTwo):
    errorEstimate = 0.01
    for i in range(0, 80):
        secantLine = boundTwo - equation(boundTwo) * ((boundTwo - boundOne) / (equation(boundTwo) - equation(boundOne)))
        if (secantLine - boundTwo < errorEstimate):
            return secantLine
        else:
            boundOne = boundTwo
            boundTwo = secantLine

            # def a(x):
            #     return (x ** 3 - 2 * x - 5)
            #
            # def b(x):
            #     return (np.exp(-x) - x)
            #
            # def c(x):
            #     return (x * np.sin(x) - 1)
            #
            # def d(x):
            #     return (x ** 3 - 3 * x ** 2 + 3 * x - 1)
            #
            # def da(x):
            #     return (3 * x ** 2 - 2)
            #
            # def db(x):
            #     return ((-1) * np.exp(-x) - 1)
            #
            # def dc(x):
            #     return (np.sin(x) + x * np.cos(x))
            #
            # def dd(x):
            #     return (3 * x ** 2 - 6 * x + 3)


# print(bisection(a, 0, 2.000001))
# print(bisection(b, 0, 2.000001))
# print(bisection(c, 0, 2.000001))
# print(bisection(d, 0, 2.000001))
# print(" ")
# print(secant(a, 0, 3))
# print(secant(b, 0, 3))
# print(secant(c, 0, 3))
# print(secant(d, 0, 3))
# print(" ")
# print(newton(a, da, 3))
# print(newton(b, db, 3))
# print(newton(c, dc, 3))
# print(newton(d, dd, 3))