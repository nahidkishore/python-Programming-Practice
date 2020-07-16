i=1
while i<=10:
  print (i)
  i+=1  #i=i+1
#test2
print ("program End")
i=4
while i<10:
  print ("Bangladesh")
  i+=1  #i=i+1
  
#sum of N number

sum=0
i=1
while i<=20:
  sum=sum+i
  i=i+1
print(sum)

#using user input

n=int(input("Enter the number: "))
sum=0
i=1
while i<=n:
  sum=sum+i
  i=i+1
print(sum)

# series type like--- 2+4+6+8+-----+n
n=int(input("Enter the number here for series: "))
sum=0
i=2
while i<=n:
  sum=sum+i
  i=i+2
print(sum)


#The break Statement
# With the break statement we can stop the loop even if the while condition is true:

i=1
while i<=50:
    print(i)
    i=i+1
    if i==25:
      break
  
  #The continue Statement   #With the continue statement we can stop the current iteration, and continue with the next:
i=0

while i<=6:
  
  
  
  i=i+1
  if i==3:
    continue
  print(i)  