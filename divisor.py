#finding divisors of given number
num = int(input("Enter the number : "))
print(f"The divisors of {num} :")
for i in range(1,num):
  if(num % i == 0):
    print(i)
  else:
     exit  
