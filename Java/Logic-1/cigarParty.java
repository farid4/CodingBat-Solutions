public boolean cigarParty(int cigars, boolean isWeekend) {
    if(isWeekend)
        return 40 <= cigars;
          
    return 40 <= cigars && cigars <= 60;
}
