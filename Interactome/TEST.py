# Python3 program for calculating
# factorial of a number using
# Stirling Approximation
import math
 
# Function for calculating factorial
def stirlingFactorial(n):
    if (n == 1):
        return 1
     
    # value of natural e
    e = 2.71
     
    # evaluating factorial using
    # stirling approximation
    z = (math.sqrt(2 * 3.14 * n) * math.pow((n / e), n))
    return math.floor(z)
 
# Driver Code
print(stirlingFactorial(1))
print(stirlingFactorial(2))
print(stirlingFactorial(3))
print(stirlingFactorial(4))
print(stirlingFactorial(5))
print(stirlingFactorial(6))
print(stirlingFactorial(7))
 
# This code is contributed by mits