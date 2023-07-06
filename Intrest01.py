#Interest Calculator
p = float(input("Enter Principle Amount : "))
r = float(input("Enter Rate of Interest : "))
t = float(input("Enter Period of paying Amount : "))

def Interest(p,r,t):
  result = (p*r*t) / 100
  print(result)

Interest(p,r,t)
