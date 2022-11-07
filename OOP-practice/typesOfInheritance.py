# Multi_Level  Inheritance

class A: 
  def display1 (self):
    print('I am A class')
  
class B(A): 
  #display1 class B te chole ashche
  def display2 (self):
    print('I am B class')


class C(B): 
  #display1 and display2 class C te chole ashche
  def display3 (self):
    #super(). use korle object e bar bar display 1,2 likhte hobe na
    print('I am C class')  
    
obj=C()
obj.display1()
obj.display2() 
obj.display3()   


#using Super(). class

class X:
  def display1(self):
    print("i am inside X class")
    
    
class Y(X):
  def display2(self):
    print("i am inside Y class")


class Z(Y):
  def display3(self):
    #using super(). class
    super().display1()
    super().display2()
    print("i am inside Z class")        
    
    

test=Z()
test.display3()


print('This is now # Multiple  Inheritance class')
# Multiple  Inheritance

class P:
  def display(self):
    print("i am inside P class")
    
    
class Q:
  def display(self):
    print("i am inside Q class")


#R er moddhe P class age dichi,tay, P class er output dekhabe, jodi, Q class age ditam tahole  class er output dekhabe... R(Q,P)
class R(P,Q):  
  pass
  
    

test=R()
test.display()
