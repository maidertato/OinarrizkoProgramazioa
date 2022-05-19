num = int(input("Sartu zenbaki hamartar bat: "))
print ('Sartu duzun zenbakia',num,'da.')

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
    lag = lag//2                            # eguneraketak egin
           
print ("Zenbaki hau bitarrean hurrengoa da:", bitar)