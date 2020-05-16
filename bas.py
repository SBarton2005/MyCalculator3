def add():
  a = input("#s you want to add, seperate with spaces: ")
  a = a.split(" ")
  c = 0
  for b in a:
    c += float(b)
  return c
def sub():
  a = input("# you want to subtract from: ")
  b = input("# you want to subtract: ")
  return float(a) - float(b)
def mul():
  a = input("#s you want to multiply, seperatre with spaces: ")
  a = a.split(" ")
  c = 1
  for b in a:
    c *= float(b)
  return c
def div():
  print("This is to divide a number, if you want to get the remainder try \'bas_rem\'")
  a = input("# you want to be divided: ")
  b = input("# you want it to be divided by: ")
  return float(a) / float(b)
def rem():
  print("This is to get the remainder, if you want to divide a number try \'bas_div\'")
  a = input("# you want to be divided: ")
  b = input("# you want it to be divided by: ")
  return float(a) % float(b)
def asc():
  a = input("#s you want to add, seperate with spaces: ")
  a = a.split(" ")
  b = input("#s you want to subtract, seperate with spaces: ")
  b = b.split(" ")
  c = 0
  for d in a:
    c += int(d)
  for e in b:
    c -= int(e)
  return c
def mdc():
  a = input("#s you want to multiply, seperate with spaces: ")
  a = a.split(" ")
  b = input("#s you want to divide by, seperate with spaces: ")
  b = b.split(" ")
  c = 1
  for d in a:
    c *= int(d)
  for e in b:
    c /= int(e)
  return c
def exp():
  a = input("Base: ")
  b = input("Exponent: ")
  return float(a) ** int(b)
def roo():
  a = input("Radicand: ")
  b = input("Index: ")
  return float(a) ** (1 / int(b))
def fac():
  a = int(input("Factorial of: "))
  i = 1
  if a > 0:
    while a > 0:
      i *= a
      a -= 1
    return i
  else:
    return "You can only find the factorial of a natural number"