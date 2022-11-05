# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  newstr = []
  
  for i in range (len(str)):
    newstr.append(2*str[i])
    
  return "".join(newstr)
