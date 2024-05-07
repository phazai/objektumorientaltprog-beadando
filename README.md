A feladat során egy egyszerű szálloda szobafoglalási rendszert kell megvalósítani Pythonban. A rendszernek képesnek kell lennie szobák kezelésére, foglalások kezelésére, létrehozására és lemondására, valamint a foglalások listázására.


Osztályok Létrehozása
---------

- Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám).
- Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.
- Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)
- Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)

Foglalások Kezelése
---------

- Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. 
-  Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását.
-  Implementálj egy metódust, ami listázza az összes foglalást.

Felhasználói Interfész és adatvalidáció
---------

- Készíts egy egyszerű felhasználói interfészt (konzolos, szöveg alapú, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás).
- A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. 
- Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek.
- Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik.