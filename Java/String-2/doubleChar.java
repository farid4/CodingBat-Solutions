public String doubleChar(String str) {
  char[] arr = new char[2 * str.length()];
    int count = 0;
      
    for(int i = 0; i < str.length(); i++) {
        arr[count] = str.charAt(i);
        count++;
        arr[count] = str.charAt(i);
        count++;
    }
                            
    return new String(arr);
}
