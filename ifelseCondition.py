a=200
b=33
c=500
if a>b and c>a:
  print("both are true")
  
x=33
y=33
if y>x:
  print("y is bigger")
elif x == y:
    print(" x and y are equal")

#Nested if
#You can have if statements inside if statements, this is called nested if statements.

x=41

if x>10:
  print("above ten")
  if x>20:
   print("also above 20")
else:
  print("but not above 20")
 #test4 
a=40
if a>50:
  if a>33:
    print("hello dear")
else:
  print("not hello")
  
  
  #test4
  
  num1=400
  num2=500
  num3=450
  
  if num1>num2:
    if num1>num3:
      print("num1 bigger")
      
    else:
      print("num3 bigger")
      
  if num2>num1:
    if num2>num3:
      print("num2 bigger")
    else:
      print("num3 is bigger")
    
    
 #This technique is known as Ternary Operators, or Conditional Expressions.
    a = 530
    b = 730
print("A") if a > b else print("=") if a == b else print("B")
  


  