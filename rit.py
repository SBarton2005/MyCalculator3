def pll():
  a = float(input("Leg: "))
  b = float(input("Leg: "))
  c = (a ** 2) + (b ** 2)
  return c ** .5
def phl():
  a = float(input("Hypotenuse: "))
  b = float(input("Leg: "))
  c = (a ** 2) - (b ** 2)
  return c ** .5
def che():
  a = float(input("Leg: "))
  b = float(input("Leg: "))
  c = float(input("Hypotenuse: "))
  return (a ** 2) + (b ** 2) == c ** 2
def gen():
  a = int(input("Odd number: "))
  b = (a ** 2) / 2
  c = b - .5
  d = b + .5
  return c, d
def sin():
  a = float(input("Opposite: "))
  b = float(input("Hypotenuse: "))
  return a / b
def cos():
  a = float(input("Adjacent: "))
  b = float(input("Hypotenuse: "))
  return a / b
def tan():
  a = float(input("Opposite: "))
  b = float(input("Adjacent: "))
  return a / b