def hamartarretik_bitarrera(num):

    #	EGUNERAKETAK	#

    lag=num				# Zenbakiarekin zuzenean lan egitea ekiditzeko, lag erabiliko dugu
    bitar=0				# Emango dugun erantzuna hasieran 0 izango da
    kont=0				# Kontagailuak posizioa adierazteko erabilgarria da

    while (lag != 0):							# laguntzailea>0 den bitartean, buklean jarraitu
        if (lag%2!=0):							# laguntzailea bakoitia bada
            bitar = bitar+(10**kont)			# 1 bat gehituko da bitarraren ezkerraldean

       #else:      								# laguntzailea bikoitia bada, ez dugu ezer 
       #    bitar = bitar+(lag%2)*(10**kont)    # gehituko, baina kontagailua handituko da
       #kasu honetak, baldintzak			    # eta laguntzailea zatitu. Hobeto ulertzeko, 
       #adierazten duen bezala, lag%2=0			# ezkerrekoa begiratu

        kont = kont +1							# baldintza bakoitzetik ateratzerakoan,
        lag = lag//2 							# eguneraketak egin

    return bitar

def proba():
    #1. Proba
    hamartar=1
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 1 da eta programak 1 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #2. Proba
    hamartar=2
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 2 da eta programak 10 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #3. Proba
    hamartar=5
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 5 da eta programak 101 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #3. Proba
    hamartar=24
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 24 da eta programak 11000 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #4. Proba
    hamartar=127
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 127 da eta programak 1111111 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #4. Proba
    hamartar=146
    emaitza=hamartarretik_bitarrera(hamartar)
    pantaila='Hamartarra 146 da eta programak 10010010 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)

proba()
