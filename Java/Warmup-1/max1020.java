public int max1020(int a, int b) {
  
  boolean aa = a>=10 && a<=20;
  boolean bb = b>=10 && b<=20;
  
  if ( aa && !bb )
    return a;
  if ( !aa && bb )
    return b;
    
  if (aa && bb) {
      if (a>b)
          return a;
          
      return b;
  }
  return 0;
      
}
