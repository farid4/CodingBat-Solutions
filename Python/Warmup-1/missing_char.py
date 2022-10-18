def missing_char(str, n):
  front = str[0:n]
  back = str[n+1:len(str)]
  return front  + back
