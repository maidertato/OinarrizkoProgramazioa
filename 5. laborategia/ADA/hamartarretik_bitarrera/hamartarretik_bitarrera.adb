function hamartarretik_bitarrera (n: in integer) return integer is

   --- Sarrera: zenbaki hamartar bat
   --- Aurre-baldintza: zenbakia osokoa da
   --- Irteera: zenbaki bitar bat
   --- Post-baldintza: emaitza, sarrerako zenbaki hamartarraren zenbaki bikoiti baliokidea izango da

   hamartar_lag : integer;
   bitar, kont : Integer := 0;

begin
   hamartar_lag := n;


    loop exit when (hamartar_lag = 0);
      if (hamartar_lag rem 2 /= 0) then
         bitar := bitar + (10**kont);
    --else
    --   bitar := bitar + (hamartar_lag rem 2)*(10**kont);
      end if;

      kont := kont + 1;
      hamartar_lag := hamartar_lag/2;

    end loop;

   return bitar;

end hamartarretik_bitarrera;
