grocery_list=['rice','potato','tomato','egg','water','milk','others']

# for item in grocery_list:
#   print(item)

# for loop continue statement
for item in grocery_list:
  if item=='tomato':
    continue
  print(item)
print ('starting break statement')
## for loop break statement
for item in grocery_list:
  if item=='tomato':
    break
  print(item)