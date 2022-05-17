with Ada.Integer_Text_IO, Ada.Text_IO;
use Ada.Integer_Text_IO, Ada.Text_IO;

procedure digitu_bakoitiak_kontatu is

   zenb,kont: Integer;                    --'Zenb' teklatutik zenbaki bat jasotzeko erabiliko dugu, eta 'kont'
                                          -- zenbaki bakoitien kopurua zenbatzeko.
begin
   kont := 0;                             --Hasiera batean, 'kont'-ren balioa hutsa izango da.
   put("Sartu osoko zenbaki bat: ");
   get(zenb);
                                          -- Orain, digitu bakoitien kopurua lortu.
   while(zenb /= 0) loop
      -- zenb:= zenb                      -- baldintza hau idaztea ez da beharrezkoa
	  if(zenb rem 2 = 1) then             -- Zatiketaren hondarra = 1 bada, orduan...
	      kont := kont+1;                 -- digitu bakoitien kopurua handitu.
	  end if;
      zenb := zenb/10;                    -- Zenbakia zati hamar zatitu prozesua berriro hasteko.
   end loop;

   put_line("Zuk sartutako zenbakiak ");
   put(kont);                             -- 'Kont'-ek zenbaki bakoitien kopurua gorde du.
   put(" digitu bakoiti ditu.");

end digitu_bakoitiak_kontatu;
