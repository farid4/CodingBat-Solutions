public String backAround(String str) {
  if (str.length() <2) 
      return str + str + str;
      
  return str.charAt(str.length()-1) + str + str.charAt(str.length()-1);
}
