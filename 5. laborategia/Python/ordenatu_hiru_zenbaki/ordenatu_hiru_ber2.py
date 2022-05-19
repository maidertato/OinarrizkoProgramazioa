def trukatu (a,b):							# bi zenbaki elkartrukatzeko,
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
    a = int(input('Sartu a zenbakia'))
    b = int(input('Sartu b zenbakia'))
    c = int(input('Sartu c zenbakia'))
    print('Sartu dituzun zenbakien ordena hurrengoa da:',a,b,c)
    
    a,b,c=ordenatuHIRU(a,b,c)
    print("Zenbakiak ordenaturik hurrengoak dira:", a,b,c)
    
proba()

