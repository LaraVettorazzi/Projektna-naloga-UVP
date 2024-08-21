import requests
import re

def prenesi_podatke(link):
    html = requests.get(link)
    return html.text

def najdi_recept(html: str):
    vzorec = r'<span></span></div></div></a><a href=/recept/.*?<span></span>'
    return re.findall(vzorec, html, re.DOTALL)

def najdi_url(recept: str):
    vzorec = re.compile(
        r'<span></span></div></div></a><a href=(?P<url>.+?) class=',
        re.DOTALL
    )
    najdba = vzorec.search(recept)
    return najdba["url"]

def izlusci_podatke(recept: str):
    vzorec = re.compile(
        r'Compatible content="ie=edge"><title>(?P<ime>.+?) \| Okusno.je</title>',
        re.DOTALL
    )
    najdba = vzorec.search(recept)
    slovar = {}
    slovar['ime'] = najdba['ime']
    return slovar

def vse_strani():
    podatki = prenesi_podatke('https://okusno.je/iskanje')
    vzorec = re.compile(
        r'<button class="button-pag dark:text-white" name=p value=(?P<st_strani>\d+?)>Konec',
        re.DOTALL
    )
    najdba = vzorec.search(podatki)
    return int(najdba['st_strani'])
