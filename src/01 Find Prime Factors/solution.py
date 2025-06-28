import math

def get_prime_factors(num):
  factors = []
  divisor = 2
  num2 = num

  while math.prod(factors) != num2:
    if num % divisor == 0:
      factors.append(divisor)
      num = num/divisor
    else:
      divisor = divisor + 1

  return(factors)

print(get_prime_factors(10))
print(get_prime_factors(100))
print(get_prime_factors(97))
