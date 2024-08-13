import csv
from izlusci_podatke import prenesi_podatke, najdi_recept, najdi_url, izlusci_podatke

def naredi_csv():
    podatki = prenesi_podatke('https://okusno.je/iskanje')
    recepti = najdi_recept(podatki)
    with open('recepti.csv', 'w', encoding='utf8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'Ime'
            ]
        )
        for recept in recepti:
            url = najdi_url(recept)
            vsebina_recept = prenesi_podatke('https://okusno.je' + url)
            podatki_recept = izlusci_podatke(vsebina_recept)
            pisatelj.writerow(
                [
                    podatki_recept['ime']
                ]
            )

naredi_csv()        




