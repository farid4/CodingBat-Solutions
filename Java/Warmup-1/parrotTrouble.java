public boolean parrotTrouble(boolean talking, int hour) {
  return talking && hour<7 || talking && hour>20;
}
