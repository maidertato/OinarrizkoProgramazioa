num = int(input("Sartu zenbaki hamartar bat: "))
print ('Sartu duzun zenbakia',num,'da.')

lag=num				
bitar=0				
kont=0				

while (lag != 0):							
    if (lag%2!=0):							
        bitar = bitar+(10**kont)			
                                                        
    kont = kont +1						   
    lag = lag//2
                
print ("Zenbaki hau bitarrean hurrengoa da:", bitar)