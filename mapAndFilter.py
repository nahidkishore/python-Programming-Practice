#Map function
def square (x):
  return x*x
num=[1,2,3,4,5]

result=list(map(square,num))

print(result)


#Filter function
#filter

age=[19,32,22,34,30,26,27,29]
def ageCheck(x):
  if x<27:
    return False
  else:
    return True
adult=filter(ageCheck,age)

for x in adult:
  print (x)