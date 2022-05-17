#Hasieraketak eginez hasi

#	1. Sartu nahi dugun zenbakia teklatutik hartu eta pantailaratu
zenb=int(input("Sartu osoko zenbaki bat: "))
print ("Sartu duzun zenbakia hurrengoa da: ", zenb)

#	2. Kontagailua eguneratu zerora
kont = 0

#digitu bakoiti bakoitzeko, kontagailua handitu gure zenbakia = 0 izan arte
#gure zenbakia txikitxeko, kont+1 egin ondoren zenb/10 eginez txikituko dugu

while(zenb != 0):
    if (zenb%2 == 1):
        kont = kont+1
   
    zenb = zenb//10;
    
print("Zuk sartutako zenbakiak", kont , "digitu bakoiti ditu.")
