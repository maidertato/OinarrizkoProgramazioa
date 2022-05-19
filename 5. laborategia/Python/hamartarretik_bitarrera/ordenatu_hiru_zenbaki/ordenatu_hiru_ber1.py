def trukatu (a,b):							# bi zenbaki elkartrukatzeko
    lag = a									# laguntzaile bat erabiliko dugu
    a = b									# lehenik aldatuko dugun zenbakiaren
    b = lag									# balioa gordeta izateko
    
    return a,b


def ordenatuBI (a,b):						# Sartutako bigarren zenbakia lehen
    if (b > a):								# zenbakia baino handiagoa bada,
        a,b =trukatu(a,b)					# trukaketa egingo dugu

    return a,b

def ordenatuHIRU (a,b,c):					# Honen bidez, hiru zenbaki ezberdinen
    a,b = ordenatuBI(a,b)					# arteko ordena ezarriko da, ordenatuBi
    a,c = ordenatuBI(a,c)					# erabiliz (zenbaki bakoitza beste bi
    b,c = ordenatuBI(b,c)                   # zenbakiekin ordenatuko da
    
    return a,b,c

def proba():
    #guztiz desordenatuta
    # 2, 5, 7
    n1=2
    n2=5
    n3=7
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("2,5,7 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))
    
  
    # 2, 7, 5
    n1=2
    n2=7
    n3=5
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("2,7,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))

    # 7, 2, 5
    n1=7
    n2=2
    n3=5
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("7,2,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))

    # 7, 5, 2
    n1=7
    n2=5
    n3=2
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("7,5,2 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))

    # 2, 5, 7
    n1=2
    n2=5
    n3=7
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("2,5,7 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))

    # 2, 7, 5
    n1=2
    n2=7
    n3=5
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print("2,7,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3))
    
    
    

proba()
