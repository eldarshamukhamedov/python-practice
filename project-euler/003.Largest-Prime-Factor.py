"""
Largest prime factor
Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Note: Using 600851475143 will make Python explode (stack too deep)
cases = [13196, 10086647, 600851475143]

# Accepts a number and a possible factor of the number
# Checks if factor is a valid factor of the number
# If it is, divides number by the factor and recurses,
# If it is not, increments factor and recurses
# Note: factor is not actually prime at the moment
def defactor (number, factor):
    print number, factor

    if (factor**2 > number):
        return number

    elif (number % factor == 0):
        return defactor(number/factor, factor)

    else:
        return defactor(number, factor + 1)

print 'Largest Prime Factor: {0}'.format(defactor(600851475143, 2))
