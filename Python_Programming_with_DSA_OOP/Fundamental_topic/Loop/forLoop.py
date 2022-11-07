def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

even_numbers=[]
user_input=int(input('please enter a number: '))
# starting=0
# while starting<user_input:
#   if is_even(starting):
#     even_numbers.append(starting)
    
#   starting+=1

for num in range(0, user_input):
  if is_even(num):
     even_numbers.append(num)
  
print(f'even numbers: {even_numbers}')
print('finished')