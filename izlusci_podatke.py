import requests
import re

def prenesi_podatke(link):
    html = requests.get(link)
    return html.text

def najdi_recept(html: str):
    vzorec = r'<a href=/recept/.*?<span></span>'
    return re.findall(vzorec, html, re.DOTALL)

def najdi_url(recept: str):
    vzorec = re.compile(
        r'<a href=(?P<url>.+?) class=',
        re.DOTALL
    )
    najdba = vzorec.search(recept)
    return najdba["url"]

def izlusci_podatke(recept: str):
    vzorec = re.compile(
        r'Compatible content="ie=edge"><title>(?P<ime>.+?) \| Okusno.je</title>.*?'
        r'"description":(?P<opis>.+?),"prepTime".*?'
        r'"recipeCategory":"(?P<kategorija>.+?)".*?'
        r'"recipeIngredient":\[(?P<sestavine>.+?)],.*?'
        r'"recipeInstructions":(?P<koraki>.*?)"nutrition".*?'
        r'difficulty-(?P<tezavnost>\d).*?'
        r'SKUPAJ</span>\n(?P<cas>.*?)</div></div></div>.*?'
        r'<tr><td><td>(?P<hranilna_vrednost>.*?)<td>',
        re.DOTALL
    )
    najdba = vzorec.search(recept)
    slovar = {}
    slovar['ime'] = najdba['ime']
    slovar['kategorija'] = najdba['kategorija']
    slovar['tezavnost'] = najdba['tezavnost']
    slovar['cas'] = cas_v_minutah(najdba['cas'])
    slovar['hranilna_vrednost'] = hranilna_vrednost_v_kcal(najdba['hranilna_vrednost'])
    slovar['koraki'] = najdba['koraki']
    slovar['sestavine'] = najdba['sestavine']
    slovar['opis'] = najdba['opis']
    return slovar

def vse_strani():
    podatki = prenesi_podatke('https://okusno.je/iskanje')
    vzorec = re.compile(
        r'<button class="button-pag dark:text-white" name=p value=(?P<st_strani>\d+?)>Konec',
        re.DOTALL
    )
    najdba = vzorec.search(podatki)
    return int(najdba['st_strani'])

def cas_v_minutah(niz):
    if 'h' in niz:
        vzorec = re.compile(
            r'(?P<ure>\d+) h (?P<minute>\d+) min'
        )
        najdba = vzorec.search(niz)
        return int(najdba['ure']) * 60 + int(najdba['minute'])
    else:
        vzorec = re.compile(
            r'(?P<minute>\d+) min'
        )
        najdba = vzorec.search(niz)
        return int(najdba['minute'])

def hranilna_vrednost_v_kcal(niz):
    vzorec = re.compile(
            r'(?P<kcal>[\d\.]+) kCal'
        )
    najdba = vzorec.search(niz)
    return int(round(float(najdba['kcal']), 0))