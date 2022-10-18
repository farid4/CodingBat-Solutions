def caught_speeding(speed, is_birthday):
    inc = 5 if is_birthday else 0
    
    if speed <= 60 + inc:
        return 0
              
    if 60 + inc < speed and speed <= 80 + inc:
        return 1
                        
    return 2
