def slo():
  xa = float(input("1st x coordinate: "))
  ya = float(input("1st y coordinate: "))
  xb = float(input("2nd x coordinate: "))
  yb = float(input("2nd y coordinate: "))
  y = ya - yb
  x = xa - xb
  return y / x
def pts():
  x = float(input("x coordinate: "))
  y = float(input("y coordinate: "))
  m = slo()
  a = m
  b = 1
  c = m * -x + y
  if a < 0:
    return f"{-a}x + {b}y = {c}"
  return f"{a}x - {b}y = {-c}"
def pti():
  x = float(input("x coordinate: "))
  y = float(input("y coordinate: "))
  m = slo()
  b = m * -x + y
  if b < 0:
    return f"y = {m}x {b}"
  return f"y = {m}x + {b}"
def stp():
  pass
def sti():
  pass
def itp():
  pass
def its():
  pass