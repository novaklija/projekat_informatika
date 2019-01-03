import Pacijent
import Moduli.Lekari as lekari

lista_pacijenata = []

def prijava():
    kor_ime = input ("Korisnicko ime: ")
    lozinka = input ("Lozinka: ")

    if kor_ime == "Pera" and lozinka == "123":
        return "lekar"
    return "pacijent"

def upisi_pacijenta(pacijent):
    f = open("pacijenti.txt", "a")
    za_ispis = f"{pacijent["korisnicko_ime"]},{pacijent["lozinka"]},{pacijent["ime"]},{pacijent["prezime"]},{pacijent["jmbg"]},{pacijent["datum_rodjenja"]},{pacijent["broj_zdravstvene_knjizice"]}"
    f.write(za_ispis)


def registracija():
 kor_ime = input("Korisnicko ime: ")
 lozinka = input("Lozinka: ")
 ime = input("Ime: ")
 prezime = input("Prezime: ")
 jmbg = input ("JMBG: ")
 datum = input ("Datum rodjenja: ")
 knjizica = input("Broj zdravstvene knjizice: ")

 pacijent = {}
 pacijent["korisnicko_ime"] = kor_ime
 pacijent["lozinka"] = lozinka
 pacijent["ime"] = ime
 pacijent["prezime"] = prezime
 pacijent["jmbg"] = jmbg
 pacijent["datum_rodjenja"] = datum
 pacijent["broj_zdravstvene_knjizice"] = knjizica
 print(pacijent)

 upisi_pacijenta(pacijent)

def procitaj_pacijente():
    f = open("pacijenti.txt", "r")

    pacijenti = f.readlines()

    lista_pacijenata = []

    for pacijent in pacijenti:
        podaci = pacijent.strip().split(" , ")
        f.close()
        pacijent = {}
        pacijent["korisnicko_ime"] = podaci[0]
        pacijent["lozinka"] = podaci[1]
        pacijent["ime"] = podaci[2]
        pacijent["prezime"] = podaci[3]
        pacijent["jmbg"] = podaci[4]
        pacijent["datum_rodjenja"] = podaci[5]
        pacijent["broj_zdravstvene_knjizice"] = podaci[6]

        lista_pacijenata.append(pacijent)
        return lista_pacijenata


def ispisi_pacijente():
    print("-"*50)

    lista pacijenata = procitaj_pacijente()

    for pacijent in lista_pacijenata:
        za_ispis = "{:15}{:15}{:15}{:15}{:15}"\
        .format(pacijent["ime"],
        pacijent["prezime"],
        pacijent["jmbg"],
        pacijent["datum_rodjenja"],
        pacijent["broj_zdravstvene_knjizice"],
        )
        print(za_ispis)


def main():
  print ("1. Prijava")
  print ("2. Registracija")

  opcija = int(input("Unesite opciju: "))
  if opcija == 1:
        uloga = prijava()
        if uloga == "pacijent":
            pacijent.meni_pacijenta()
        else:
            lekari.meni_lekari()
  elif opcija == 2:
      registracija()
      ispisi_pacijente()

main()
