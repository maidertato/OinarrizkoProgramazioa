# Hasieraketak
#	1. Sartu nahi dugun zenbakia teklatutik hartu eta pantailaratu

bitar=int(input("Sartu zenbaki bat bitarrez eta 1ekin hasten dena"))
print ("Sartu dizun zenbaki bitarra hurregoa da:", bitar)

# 	2. berretzaile gisa erabiliko dugun zenbakia zerora eguneratu.
# 	Gogoratu! 2^0=1
#	Horrez gain, zenbaki hamartarra bilduko duen aldagaia sortu

ber = 0
hamartar = 0

#sortu zenbakia hamartarrez
while(bitar > 0):						# bitarra=0 denean, gelditu
    if (bitar%2 == 1):					
        hamartar = hamartar+2**ber		# hamartarraren balioa handituz
    bitar = bitar // 10					# bitarraren balioa txikituz
    ber = ber+1							# berretzailea edo posizioa handitu
                                        # potentzia bezala erabiltzeko  

print("Zenbakia hamartarrez honakoa da: ", hamartar)
