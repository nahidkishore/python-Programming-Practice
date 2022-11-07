""" 
i=0
while i<=10:
  print('bangladesh')
  i=i+1
  
  
  # user input
  
  sum=0;
  i=1;
  n=int(input('enter number :'))
  while i<=n:
    sum=sum+i
    i=i+1
    
  print(sum) """

#for loop

num=[10,13,24,56,54]

for x in num:

 print(x)
#sum
for x in num:
  sum=sum+x

print(sum)

#
name=['nahid','niloy','jannat','tania','naima']

for x in name:
  print(x)
  
#The break Statement
print('break statement')

for x in name:
  print(x)
  if x== 'tania':
    break
  
# another 

for x in name:
  if x=='jannat':
    break
  print(x)
  
#The range() Function

for x in range(15):
  print(x)
  
#
for x in range(10, 15):
  print(x)
  
#series
#1+2+3+.....+n


n=int(input('enter number: '))
sum=0
for x in range(1,n+1):
  sum=sum+x
print(sum)

#2+4+6+.....+n

n=int(input('enter positive number'))
sum=0
for x in range(2, n+2):
  sum=sum+x
  print(x,sum)

#another option
""" n=int(input('Please enter positive number:'))
#sum=0
 for x in range(2, n+1,3):
  #sum=sum+x
  print(x) """
  #2+4----+n
  
n=int(input('enter positive number'))
sum=0
for x in range (2,n+1,2):
  
  sum=sum+x
print(sum)
