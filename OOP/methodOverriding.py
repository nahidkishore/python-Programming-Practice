class Phone:
  def __init__(self):
    print('I am in a phone class')
    
class Samsung(Phone):
  pass  
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


s=Samsung()


#Method Overriding

class Phone:
  def __init__(self):
    print('I am in a phone class')
    
class Samsung(Phone):
  def __init__(self):
    super(). __init__()  #jodi phone class and samsung class 2ta e print korate chai tahole " super(). _init_" use korbo
    print('I am in a samsung class')
  
 


s=Samsung()


