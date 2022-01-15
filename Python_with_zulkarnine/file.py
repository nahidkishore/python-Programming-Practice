with open('lorem.txt',mode='r') as lorem_file:
  for line in lorem_file.readlines():
    print(line)
    
print('finished')