# Total starts at 2 because we know the second term is 2
total = 2

fib1 = 1
fib2 = 2

temp = 0

while temp < 4000000:
  temp = fib1 + fib2
  fib1 = fib2
  fib2 = temp

  if temp % 2 == 0:
    total += temp

print total