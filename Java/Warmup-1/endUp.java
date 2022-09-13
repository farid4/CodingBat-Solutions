public String endUp(String str) {
  if (str.length() <3) 
    return str.toUpperCase();
    
  String last = str.substring(str.length()-3);
  return str.substring(0,str.length()-3) + last.toUpperCase();
}
