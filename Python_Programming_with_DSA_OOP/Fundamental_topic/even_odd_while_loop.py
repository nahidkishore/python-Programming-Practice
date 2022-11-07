def is_even(number):
  if number%2 == 0:
    return True
  else:
    return False
  
  #while loop

# starting=0
# while starting<10:
#   if is_even(starting):
#     print(f'{starting} is even')
#   else:
#     print(f'{starting} is odd')
#   starting=starting+1
  
# print('finished')

#show array List
# even_numbers=[]
# user_input=int(input('limit: '))
# starting=0
# while starting<user_input:
#   if is_even(starting):
#     even_numbers.append(starting)
#   starting=starting+1
# print(f'Even number : {even_numbers}')
# print('finished')

  #### for loop
even_numbers=[]
starting=0
user_input=int(input('limit: '))

for value in range (0, user_input):
  if is_even(value):
    even_numbers.append(value)
    
print(f'Even number : {even_numbers}')
print('finished')