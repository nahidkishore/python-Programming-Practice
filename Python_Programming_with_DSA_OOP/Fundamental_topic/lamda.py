def calculate(a,b):
  return a*a + 2*a*b +b*b
test=calculate(2,3)
print(test)
print(calculate(3,4))

##
testLambda= (lambda x,y:x*x + 2*x*y+y*y)(2,3)
print(testLambda)

##Cube

cube=(lambda x:x*x*x)(3)
print(cube)