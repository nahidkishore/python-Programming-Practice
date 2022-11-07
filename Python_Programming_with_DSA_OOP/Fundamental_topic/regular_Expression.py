 #match method

import re
pattern=r'color';
if re.match(pattern,'Black is my favourite color, I love light gray color also'):
  print('Match')
else:
  print('Not Matched')
  
  
#search Method

import re
pattern=r'color';
if re.search(pattern,' Black is my favourite color, I love light gray color also'):
  print('Match')
else:
  print('Not Matched')
  
  
  #Find All method
  
  
  import re
  pattern = r"color";
  print(re.findall(pattern,'Black is my favourite color, I love light gray color also'))


#more Search function

import re
pattern =r'color';
text='my favourite color is green';
result=re.search(pattern,text);
if result:
  print(result.start())
  print(result.end())
  print(result.span())
  

