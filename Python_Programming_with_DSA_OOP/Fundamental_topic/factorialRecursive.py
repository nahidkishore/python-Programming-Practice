def fact(n):
  if n==1:
    return 1
  else:
    return n * fact(n-1)
  
result=fact(5)
print(result)

## using for loop

def factorial(num):
  fact=1
  for i in range(1,num+1):
    fact=fact*i
  return fact
test=factorial(6)
print(test)


