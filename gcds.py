a = int(input("Enter a divident : "))
b = int(input("Enter a divisor : "))

while True:
  q = int(a/b)
  r = a-(b*q)
  print(f"Quetient = {q} and Remainder = {r}")
  if r==0:
    break
  else:
    gcd = r
  a,b=b,r

print(f"GCD = {gcd}")
