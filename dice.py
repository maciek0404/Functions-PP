def f(dice):
    if not dice:
        return None
    
    max_powtorzen = 0
    zwycieska_kostka = int(dice[0])
    
    aktualne_powtorzenia = 0
    poprzednia_cyfra = None
    
    for cyfra in dice:
        if cyfra == poprzednia_cyfra:
            
            aktualne_powtorzenia += 1
        else:
         
            aktualne_powtorzenia = 1
            poprzednia_cyfra = cyfra
        
        
        if aktualne_powtorzenia > max_powtorzen:
            max_powtorzen = aktualne_powtorzenia
            zwycieska_kostka = int(cyfra)
            
    return zwycieska_kostka