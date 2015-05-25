"""
Largest palindrome product
Problem 4
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Check if number is a palindrome
# def isPalindrome (num):
#     s = str(num)
#     j, k = 0, len(s) - 1
#
#     while j <= k:
#         if s[j] != s[k]:
#             return False
#         j, k = j + 1, k - 1
#
#     return True

# Accepts the "top half" of a palindrome
# Ex. Given max=413, Returns 413314
def buildPalindrome (max):
    return int(str(max) + str(max)[::-1])

# Accepts a palindrome and largest valid factor
# Counting down from largest n-digit factor,
# attempts to find a pair of n-digit factors
def findComplimentaryFactor (palindrome, max):
    i = max
    while palindrome / i <= max:
        if palindrome % i == 0:
            return True
        i -= 1

    return False

# Accepts digit-count (n) for palindrome dual-factor
# Counting down from largest n-digit factor, builds
# a palindrome and attempts to find a complimentary
# n-digit factor
def findLargestPalindromeProduct (digits):
    max = current = 10**digits - 1
    min = 10**(digits - 1)

    while current > min:
        current -= 1
        palindrome = buildPalindrome(current)

        if(findComplimentaryFactor(palindrome, max)):
            return palindrome

    return False

print findLargestPalindromeProduct(3)
