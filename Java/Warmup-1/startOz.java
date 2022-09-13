public String startOz(String str) {
  String result = "";
  if (str.length() <1) return result;
  
  if ((str.length() ==1) && (str.charAt(0) == 'o'))
     return result + "o";
     
  if (str.charAt(0) == 'o')
      result += "o";
      
  if (str.charAt(1) == 'z')
      result += "z";  
      
  if (str.substring(0,1).equals("oz"))
      result += "oz";
      
  return result;
}
