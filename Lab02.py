# Course: ITI 1120
# Lab 02
# Balaji, Aparna
# 300462188

import math

# Programming Exercise 1

def repeater(s1, s2, n):
    return ("_" + (s1 + s2) * n + "_")

# Programming Exercise 2

def roots(a, b, c):
    x1 = ((-1 * b) + (math.sqrt ((b ** 2) - (4 * a * c)))) / 2 * a
    x2 = ((-1 * b) + (math.sqrt ((b ** 2) - (4 * a * c)))) / 2 * a
    print ("The quadratic equation with coefficients a = " , a , " b = " , b , " c = " , c , " has the following solutions (i.e. roots):")
    print (x1, " and " , x2)
    return (x1, x2)


# Programming Exercise 3

def real_roots(a,b,c):
    real = (b ** 2 - (4 * a * c)) >= 0
    return (real)

# Programming Exercise 4

def reverse(x):
    first_digit = x // 10
    second_digit = (x % 10) * 10
    return (first_digit + second_digit)
