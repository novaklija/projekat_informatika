def upisi_pacijenta(pacijent):
    f = open("pacijenti.txt", "a")
    za_ispis = f'{pacijent["korisnicko_ime"]},{pacijent["lozinka"]},{pacijent["ime"]},{pacijent["prezime"]},{pacijent["jmbg"]},{pacijent["datum_rodjenja"]},{pacijent["broj_zdravstvene_knjizice"]}'
    f.write(za_ispis)

def registracija():
    kor_ime = input("Unesite Vaše korisničko ime: ")
    lozinka = input("Unesite Vašu lozinku: ")
    ime = input("Unesite Vaše ime: ")
    prezime = input("Unesite Vaše prezime: ")
    jmbg = input("Unesite Vaš JMBG: ")
    dat_rodj = input("Unesite Vaš datum rođenja: ")
    br_zdr_knjiz = input("Unesite Vaš broj zdravstvene knjižice: ")
