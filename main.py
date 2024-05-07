from abc import ABC, abstractmethod
from datetime import datetime

# Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám).
class Szoba(ABC):
  def __init__(self, szobaszam, ar ):
    self.szobaszam=szobaszam
    self.ar=ar

  @abstractmethod
  def __str__(self):
    pass

# Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.

class EgyagyasSzoba(Szoba):
  def __init__(self, szobaszam, ar):
    super().__init__(szobaszam, ar)

  def __str__(self):
    return f"Egyágyas szoba {self.szobaszam}, Ár: {self.ar} Ft " 

class KetagyasSzoba(Szoba):
  def __init__(self, szobaszam, ar):
    super().__init__(szobaszam, ar)

  def __str__(self):
    return f"Kétágyas szoba {self.szobaszam}, Ár: {self.ar} Ft " 

# Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)

# Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)
# Tervezői döntés: A foglalások a szállodához tartoznak, benne tárolom

class Szalloda:
  def __init__(self, nev):
    self.nev=nev
    self.szobak = []
    self.foglalasok = []

  def uj_szoba(self, szoba):
    self.szobak.append(szoba)

# Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. 
  def foglalas(self, datum):
    # gyűjtsük ki egy listába a foglalt szobaszámokat
    foglalt_szobaszamok=[]
    for foglalas in self.foglalasok:
      if foglalas[1]==datum:
        foglalt_szobaszamok.append(foglalas[0])

# szobák listázása (de csak azokat amik szabadok)
    szabad_szobaszamok=[]
    for szoba in self.szobak:
      if szoba.szobaszam not in foglalt_szobaszamok:
        print(szoba)
        szabad_szobaszamok.append(szoba.szobaszam)

# ha nincs erre a dátumra szabad szoba
    if len(szabad_szobaszamok)==0:
      input("Erre a napra jelenleg nincs szabad szobánk. Kérjük próbáljon egy másik időpontot! \n Nyomj ENTERT a folytatáshoz!")
      return

    hanyas=input("Írja be a kívánt szoba számot: ")
    if hanyas in foglalt_szobaszamok:
      input("Erre a szobára nem lehet már foglalni, próbáljon meg egy másikat! \nNyomjon ENTERT a folytatáshoz! ")
      return
    if hanyas not in szabad_szobaszamok:
      input("Helytelen szobát adott meg! Próbáljon egy másikat! \nNyomjon ENTERT a folytatáshoz! ")
      return

# kikeressük a foglalandó szoba árát
    ar = None
    for szoba in self.szobak:
      if szoba.szobaszam == hanyas:
        ar=szoba.ar

    self.foglalasok.append( [hanyas,datum ] ) 
    input("Sikeres foglalás! \nNyomjon ENTERT a folytatáshoz!")
    return ar


# Implementálj egy metódust, ami listázza az összes foglalást.

  def foglalasok_listaz(self):
    print("Foglalt szobák:")
    for elem in self.foglalasok:
      print("Szobaszám:", elem[0], "Dátum:" , str(elem[1]).split(" ")[0]  )  

    if len(self.foglalasok)==0:
      input("Nincsenek foglalások \n Nyomjon ENTERT a folytatáshoz!")
      return False
    else:
      input("Nyomjon ENTERT a folytatáshoz!")  
      return True

# Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását.

  def lemondas(self):
    
    ret = self.foglalasok_listaz()
    if ret == False:
      return 

    szobaszam = input("Írja be a törölni kívánt szobaszámot: ")
    datum = input("Törölni kívánt foglalás dátuma (ÉÉÉÉ-HH-NN): " )
    if len(datum) != 10 or datum.count("-") != 2 or not datum.replace("-","").replace("-","").isnumeric() :
      input("Nem megfelelő formátumú dátumot adott meg! Próbálja újra és nyomjon egy ENTERT!")
      return
    vagott_datum = datum.split("-")
    datum_igazi = datetime( int(vagott_datum[0]),int(vagott_datum[1]) , int(vagott_datum[2]))

    csomag = [szobaszam, datum_igazi]
    
# Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek.
    if csomag in self.foglalasok:
      self.foglalasok.remove(csomag)
      input("Sikeres lemondás! \nNyomjon ENTERT a folytatáshoz! ")
    else:
      input("Nincs ilyen foglalás! Próbálja Újra! \nNyomjon ENTERT a folytatáshoz!  ")



######################
def main():

# Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik
  szalloda = Szalloda("Aranyhomok Szálloda")
  print(szalloda.nev)

  sz1 = EgyagyasSzoba("101", 90000)
  sz2 = EgyagyasSzoba("102", 90000)
  sz3 = KetagyasSzoba("201", 130000)

  szalloda.uj_szoba(sz1)
  szalloda.uj_szoba(sz2)
  szalloda.uj_szoba(sz3)

  szalloda.foglalasok.append( ["101", datetime(2024, 6, 1) ] )
  szalloda.foglalasok.append( ["201", datetime(2024, 6, 1) ] )
  szalloda.foglalasok.append( ["102", datetime(2024, 6, 15) ] )
  szalloda.foglalasok.append( ["101", datetime(2024, 7, 25) ] )
  szalloda.foglalasok.append( ["201", datetime(2024, 7, 26) ] )

# Készíts egy egyszerű felhasználói interfészt (konzolos, szöveg alapú, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás).

  while 10>1:
    print("Főmenü")
    print("------")
    print("1.: Foglalás")
    print("2.: Lemondás")
    print("3.: Foglalások listázása")
    print("4.: Kilépés")
    print()

    try:
      menupont=int( input("Válasszon egy menü pontot: ") )
    except ValueError:
      input("Számot adjon meg! \nNyomjon egy ENTERT a folytatáshoz!")
      continue

    if menupont==4:
      break
    elif menupont==3:
      szalloda.foglalasok_listaz()
    elif menupont==2:
      szalloda.lemondas()
    elif menupont==1: 
# A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni)
      datum = input("Adja meg a foglalás (ÉÉÉÉ-HH-NN) dátumát: " )
      if len(datum) != 10 or datum.count("-") != 2 or not datum.replace("-","").replace("-","").isnumeric() :
        input("Nem megfelelő formátumú dátumot adott meg! Próbálja újra és nyomjon egy ENTERT!")
        continue

      vagott_datum = datum.split("-")
      datum_igazi = datetime( int(vagott_datum[0]),int(vagott_datum[1]) , int(vagott_datum[2]))

      if datum_igazi >= datetime.now():
        szalloda.foglalas(datum_igazi)
      else:
        print("Hibás dátum, kérem próbálja újra!")

    else:
      input("Nem megfelelő számot adott meg! Kérem próbálja újra és nyomjon egy ENTERT!")

# csak futtatás esetén indul a main ha ezt leírjuk (import esetén nem)
if __name__ == "__main__":
  main()




