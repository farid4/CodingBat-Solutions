public String frontTimes(String str, int n) {
  
  String result = "";
  
  for(int i=0; i<n; i++) {
  if(str.length()<3) 
      result = result + str;
      else {
      result = result + str.substring(0,3);
      }
  }
  
  return result;
}
