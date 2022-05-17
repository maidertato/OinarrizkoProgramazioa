with Ada.Integer_Text_IO, Ada.Text_IO;
use Ada.Integer_Text_IO, Ada.Text_IO;

procedure bitarretik_hamartarrera is
   bitar, hamartar, ber: Integer;         -- hiru aldagai beharko ditugu: bitarra, hamartarra, eta bitarretik hamartarrera
                                          -- pasatzeko erabiliko dugun potentziak adierazten duen aldagaia (ber).
begin
   put("Sartu zenbaki bat bitarrez eta 1ekin hasten dena: ");
   get(bitar);
   hamartar := 0;
   ber := 0;                              -- lehen posizioan egonda, 1 = 2^0 dela dakigu (ondorioz, ber=0)

   while(bitar>0) loop                    -- bitarra = 0 denean, gelditu
      if (bitar rem 2=1) then
         hamartar := hamartar+2**ber;     -- hamartarreren balioa handituz
      end if;
      ber := ber+1;                       -- berretzailea edo posizioa handitu
      bitar := bitar/10;                  -- bitarraren balioa txikituz
   end loop;

   put_line("Zenbakia hamartarrez honakoa da:");
   put(hamartar);

end bitarretik_hamartarrera;
