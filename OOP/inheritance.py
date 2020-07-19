#parent class, super class
#child class, sub class

class Phone:
  def call(self):
    print('You can call')
  def message (self):
    print('You can message')
    
class Samsung:
  def call(self):
    print('You can call')
  def message (self):
    print('You can message')
  def photo (self):
    print('You can take photo')
    
    
p=Phone()
p.message()
p.call()


s=Samsung()
s.call()
s.message()
s.photo()


print('Easy Way to inheritance use child class')
#Easy Way to inheritance use child class
class Phone:
  def call(self):
    print('You can call')
  def message (self):
    print('You can message')
    
class Samsung(Phone):
  #call & message kaj korteche... 
  #samsung er vitore "Phone" ke child class hisabe create koreche.....sejonno "samsung " class e o call & message kaj korche
  """ def call(self):
    print('You can call')
  def message (self):
    print('You can message') """
  def photo (self):
    print('You can take photo')
    
    
p=Phone()
p.message()
p.call()


s=Samsung()
s.call()
s.message()
s.photo()
