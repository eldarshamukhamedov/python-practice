"""
Multiples of 3 and 5
Problem 1
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def countUp (base, index, upperBound):
    value = base * index
    if (value >= upperBound):
        return 0
    else:
        return value + countUp(base, index + 1, upperBound)

def sumOfMultiples (upperBound):
    return countUp(3, 1, upperBound) + countUp(5, 1, upperBound) - countUp(3 * 5, 1, upperBound)

print sumOfMultiples (1000)
