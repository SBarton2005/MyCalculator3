import bas, cir, qua, rit
def cbas():
  p = input("Bas Operation: ")
  if p == "add":
    return bas.add()
  elif p == "sub":
    return bas.sub()
  elif p == "mul":
    return bas.mul()
  elif p == "div":
    return bas.div()
  elif p == "rem":
    return bas.rem()
  elif p == "asc":
    return bas.asc()
  elif p == "mdc":
    return bas.mdc()
  elif p == "exp":
    return bas.exp()
  elif p == "roo":
    return bas.roo()
  elif p == "fac":
    return bas.fac()
  else:
    return "You didn\'t pick a bas operation. Try add, sub, mul, div, rem, asc, mdc, exp, roo, or fac."
def cqua():
  p = input("Qua Operation: ")
  if p == "roo":
    return qua.roo()
  elif p == "sol":
    return qua.sol()
  elif p == "ver":
    return qua.ver()
  elif p == "fac":
    return qua.fac()
  elif p == "vef":
    return qua.vef()
  elif p == "vts":
    return qua.vts()
  else:
    return "You didn\'t pick a qua operation. Try roo, sol, ver, or fac."
def crit():
  p = input("Rit Operation: ")
  if p == "pll":
    return rit.pll()
  elif p == "phl":
    return rit.phl()
  elif p == "gen":
    return rit.gen()
  elif p == "che":
    return rit.che()
  elif p == "sin":
    return rit.sin()
  elif p == "cos":
    return rit.cos()
  elif p == "tan":
    return rit.tan()
  else:
    return "You didn\'t pick a rit operation. Try pll, phl, gen, che, sin, cos, or tan."
def ccir():
  p = input("Cir Shape: ")
  if p == "cer":
    return cir.cer()
  elif p == "are":
    return cir.are()
  elif p == "ssa":
    return cir.ssa()
  elif p == "svl":
    return cir.svl()
  elif p == "cys":
    return cir.cys()
  elif p == "cyv":
    return cir.cyv()
  elif p == "cos":
    return cir.cos()
  elif p == "cov":
    return cir.cov()
  elif p == "col":
    return cir.col()
  else:
    return "You didn\'t pick a cir opperation. Try cer, are, ssa, svl, cys, cyv, cos, cov, or col."
def mai():
  c = True
  while c == True:
    o = input("Section: ")
    if o == "bas":
      print(cbas())
    elif o == "qua":
      print(cqua())
    elif o == "rit":
      print(crit())
    elif o == "cir":
      print(ccir())
    else:
      print("You didn\'t pick one of the sections we have operations for. Try bas, mul, qua, rit, or cir")
    i = input("Continue: ")
    if i == "n":
      c = False
  return None