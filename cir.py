def cer():
  r = float(input("Radius: "))
  pi = 3.14
  return 2 * pi * r
def are():
  r = float(input("Radius: "))
  pi = 3.14
  return pi * r * r
def ssa():
  r = float(input("Radius: "))
  pi = 3.14
  return 4 * pi * r * r
def svl():
  r = float(input("Radius: "))
  pi = 3.14
  return 4 / 3 * pi * r * r * r
def cys():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return 2 * pi * r * ( r + h )
def cyv():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return pi * r * r * h
def cos():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  a = h ** 2 + r ** 2
  pi = 3.14
  return pi * r * ( r + a ** .5 )
def cov():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return pi * r * r * h / 3
def col():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  a = h ** 2 + r ** 2
  pi = 3.14
  return pi * r * ( a ** .5 )