def roo():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  d = (b ** 2) - (4 * a * c)
  e = d ** .5
  fa = - b + e
  fb = - b - e
  ga = fa / 2 / a
  gb = fb / 2 / a
  return ga, gb
def ver():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  x = - b / 2 / a
  y = (a * x* x) + (b * x) + c
  return x, y
def sol():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  x = float(input("x: "))
  y = (a * x * x) + (b * x) + c
  return y
def fac():
  xa, xb = roo()
  a = input("a again: ")
  if xa < 0:
    if xb < 0:
      return f"{a}(x+{xa*-1})(x+{xb*-1})"
    return f"{a}(x+{xa*-1})(x-{xb})"
  if xb < 0:
    return f"{a}(x-{xa})(x+{xb*-1})"
  return f"{a}(x-{xa})(x-{xb})"
def vef():
  h, k = ver()
  a = float(input("a again: "))
  if h < 0:
    if k < 0:
      return f"{a}(x{h})^2{k}"
    else:
      return f"{a}(x{h})^2+{k}"
  elif k < 0:
    return f"{a}(x-{h})^2{k}"
  else:
    return f"{a}(x-{h})^2+{k}"
def vts():
  h = float(input("x coordinate of vertex: "))
  k = float(input("y coordinate of vertex: "))
  a = float(input("a: "))
  b = -1 * h * 2 * a
  c = (h ** 2) * a + k
  if b < 0:
    if c < 0:
      return f"{a}x^2 {b}x {c}"
    return f"{a}x^2 {b}x + {c}"
  if c < 0:
    return f"{a}x^2 + {b}x {c}"
  return f"{a}x^2 + {b}x + {c}"
def exp():
  a = float(input("Coefficent 1: "))
  b = float(input("Constant 1: "))
  c = float(input("Coefficent 2: "))
  d = float(input("Constant 2: "))
  h = float(input("Outside Input: "))
  e = h * a * c
  f = h * ((a * d) + (b * c))
  g = h * b * d
  if f < 0:
    if g < 0:
      return f"{e}x^2 {f}x {g}"
    return f"{e}x^2 {f}x + {g}"
  if g < 0:
    return f"{e}x^2 + {f}x {g}"
  return f"{e}x^2 + {f}x + {g}"