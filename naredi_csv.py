import csv
from izlusci_podatke import prenesi_podatke, najdi_recept, najdi_url, izlusci_podatke, vse_strani

def naredi_csv():
    with open('recepti.csv', 'w', encoding='utf8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'Ime',
                'Kategorija',
                'Težavnost',
                'Čas (min)',
                'Hranilna vrednost (kcal/100g)',
                'Koraki',
                'Sestavine',
                'Opis',
                'Dolžina opisa (besede)'
            ]
        )
        for stran in range(1, 3): #popravi na vse_strani() + 1
            podatki = prenesi_podatke(f'https://okusno.je/iskanje?t=recipe&sort=score&p={stran}')
            recepti = najdi_recept(podatki)
            for recept in recepti:
                url = najdi_url(recept)
                vsebina_recept = prenesi_podatke('https://okusno.je' + url)
                podatki_recept = izlusci_podatke(vsebina_recept)
                pisatelj.writerow(
                    [
                        podatki_recept['ime'],
                        podatki_recept['kategorija'],
                        podatki_recept['tezavnost'],
                        podatki_recept['cas'],
                        podatki_recept['hranilna_vrednost'],
                        podatki_recept['koraki'],
                        podatki_recept['sestavine'],
                        podatki_recept['opis'],
                        podatki_recept['st_besed']
                    ]
                )

naredi_csv()        




