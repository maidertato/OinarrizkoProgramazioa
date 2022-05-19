def trukatu (a,b):
    lag = a
    a = b
    b = lag
    
    return a,b

def ordenatuBI (a,b):
    if (b > a):								
        a,b =trukatu(a,b)					

    return a,b

def ordenatuHIRU (a,b,c):
    a,b = ordenatuBI(a,b)					
    a,c = ordenatuBI(a,c)					
    b,c = ordenatuBI(b,c)                   
    return a,b,c

def proba():
    a = int(input('Sartu a zenbakia'))
    b = int(input('Sartu b zenbakia'))
    c = int(input('Sartu c zenbakia'))
    print('Sartu dituzun zenbakien ordena hurrengoa da:',a,b,c)
    
    a,b,c=ordenatuHIRU(a,b,c)
    print("Zenbakiak ordenaturik hurrengoak dira:", a,b,c)
    
proba()

