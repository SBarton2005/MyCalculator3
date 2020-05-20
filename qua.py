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
  if xa < 0:
    if xb < 0:
      return f"(x+{xa*-1})(x+{xb*-1})"
    return f"(x+{xa*-1})(x-{xb})"
  if xb < 0:
    return f"(x-{xa})(x+{xb*-1})"
  return f"(x-{xa})(x-{xb})"
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
  b = h * 2 * a
  c = (h ** 2) * a + k
  return f"{a}x^2+{b}x+{c}"