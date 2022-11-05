# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  count1=0
  count2=0
  for i in range (len(str)-2):
    if str[i:i+3] == "cat":
      count1 +=1
    if str[i:i+3] == "dog":
      count2 +=1

  if count1 == count2:
    return True
    
  return False
