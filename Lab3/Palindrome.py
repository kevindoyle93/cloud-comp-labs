import sys

str1 = sys.argv[1]
str2 = str1[::-1]

if (str1 == str2):
  ans = True
  print(ans)
else:
  ans = False
  print(ans)