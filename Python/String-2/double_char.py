def double_char(str):
  newstr = []
  
  for i in range (len(str)):
    newstr.append(2*str[i])
    
  return "".join(newstr)
