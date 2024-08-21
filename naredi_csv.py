import csv
from izlusci_podatke import prenesi_podatke, najdi_recept, najdi_url, izlusci_podatke, vse_strani

def naredi_csv():
    with open('recepti.csv', 'w', encoding='utf8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'Ime',
                'Kategorija'
            ]
        )
        for stran in range(1, 4): #popravi na vse_strani() + 1
            podatki = prenesi_podatke(f'https://okusno.je/iskanje?t=recipe&sort=score&p={stran}')
            recepti = najdi_recept(podatki)
            for recept in recepti:
                url = najdi_url(recept)
                vsebina_recept = prenesi_podatke('https://okusno.je' + url)
                podatki_recept = izlusci_podatke(vsebina_recept)
                pisatelj.writerow(
                    [
                        podatki_recept['ime'],
                        podatki_recept['kategorija']
                    ]
                )

naredi_csv()        




