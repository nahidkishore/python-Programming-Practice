def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

even_numbers=[]
starting=0
while starting<100:
  if is_even(starting):
    even_numbers.append(starting)
    
  starting+=1
print(f'even numbers: {even_numbers}')
print('finished')