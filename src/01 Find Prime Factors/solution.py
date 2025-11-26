import math

# Define function to get prime factors
def get_prime_factors(num):
  factors = [] # Empty vector to store prime factors
  divisor = 2 # Divisor first prime
  num2 = num
  # While loop until product of factors equal to number
  while math.prod(factors) != num2:
    # If the remainder of the division is equal to 0, add divisor to factors
    # else, sum 1 to the divisor and try again.
    if num % divisor == 0:
      factors.append(divisor)
      num = num/divisor
    else:
      divisor = divisor + 1
  # Return the vector with the prime factors
  return(factors)

# Test function
print(get_prime_factors(10))
print(get_prime_factors(100))
print(get_prime_factors(97))
