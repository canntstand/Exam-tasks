import sys

sys.setrecursionlimit(3000)

count = 0


def F(n):
  global count
  count += 1

  if n <= 1:
    return 1
  elif n % 100 == 0:
    return F(n - 1) * F(n - 2) + F(1)
  else:
    return n * F(n - 1)

F(2042)

print("Количество вызовов:", count)