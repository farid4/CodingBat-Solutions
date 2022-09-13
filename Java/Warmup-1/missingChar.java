public String missingChar(String str, int n) {
  String first = str.substring(0,n);
  String last = str.substring(n+1);
  return first + last;
}
