class student:
  roll=''
  gpa=''
  
  
  def __init__(self,roll,gpa):
    self.roll=roll
    self.gpa=gpa
  
  
  def display(self):
    print(f"Roll:{self.roll}, GPA:{self.gpa}")
    
    
nahid=student(101,3.15)

nahid.display()


naima=student(102,3.5)

naima.display()



