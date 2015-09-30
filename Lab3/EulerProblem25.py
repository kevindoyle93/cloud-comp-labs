fib1 = 1
fib2 = 1

temp = 0
ansFound = False
count = 2

while ansFound == False:
  temp = fib1 + fib2
  fib1 = fib2
  fib2 = temp

  count = count + 1

  if (fib2 // pow(10, 999) == 1):
    ansFound = True

print(count)