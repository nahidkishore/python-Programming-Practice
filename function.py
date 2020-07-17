def add(x,y,z):
  sum=x+y+z
  print(sum)
add(3,4,5)


# Function using return 

def addition(p,q,r):
  sum=p+q+r
  return sum
result=addition(20,30,50)
print(result)

#length check
def test(num):
  
  i=0
  while i<len(num):
    i=i+1
  return i
check=test([10,20,30,40,50,60])
print(check)


#length addition


def test(num):
  sum=0
  i=0
  while i<len(num):
    sum=sum+num[i]
    i=i+1
  return sum
check1=test([10,20,30,40,50,60])
print(check1)

#wood Calculator

def woodCalculator(chair,table,bed):
  woodCount=1*chair+3*table+5*bed
  return woodCount
total=woodCalculator(3,4,5)
print(total)

#inch to feet

def inchToFeet(inch):
  feet=inch/12
  return feet
checkFeet=inchToFeet(60)
print(checkFeet)


# Grade report check

def gradeReport(grade):
  if grade>=90 and grade<=93:
    status='Your Grade is A'
    return status
    #print(' Your Grade is A')
  elif grade>=87 and grade<=89:
    status1='Your Grade is A-'
    return status1
    #print('Your grade is A-')
  elif grade>=83 and grade<=86:
    status2='Your Grade is B+'
    return status2
    #print('Your grade is B+')
  elif grade>=80 and grade<=82:
    status3='Your Grade is B'
    return status3
    #print('Your grade is B')
  elif grade>=77 and grade<=79:
    status4='Your Grade is B-'
    return status4
    #print('Your grade is B-')
  elif grade>=73 and grade<=76:
    status='Your Grade is C+'
    return status
    #print('Your grade is C+')
  elif grade>=70 and grade<=72:
    status5='Your Grade is C'
    return status5
    #print('Your grade is C')
  elif grade>=66 and grade<=69:
    status6='Your Grade is C-'
    return status6
    #print('Your grade is C-')
  elif grade>=60 and grade<=65:
    status7='Your Grade is D'
    return status7
    #print('Your grade is C')
  else:
    status8='Retake this course'
    return status8
    #print(' Retake this course')


totalMark=gradeReport(86)
print(totalMark)



# brick Calculation

def brickCalculation(building):
  if building>=0 and building<=10:
    upToTen=1000*15
    return upToTen
  elif building>=11 and building<=20:
    upToTwenty=1000*12
    return upToTwenty
  elif building>20:
    other=1000*10
    return other

totalBrick=brickCalculation(14)
print('you will need to ', totalBrick , 'bricks')


#tinny Friend


def tinnyFriend(friend):
  min=friend[0]
  for i in range(0,len(friend)):
    name=friend[i]
    if len(name)<len(min):
      min=name
  return min

minName=tinnyFriend(['nahid','nil','naima'])

print(minName)    
      
     