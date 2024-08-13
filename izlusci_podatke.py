import requests
import re

def prenesi_podatke(link):
    html = requests.get(link)
    # with open("html.txt", "w", encoding="utf8") as dat:
    #     print(html.text, file=dat)
    return html.text

def najdi_recept(html: str):
    vzorec = r'<span></span></div></div></a><a href=/recept/.*?<span></span>'
    return re.findall(vzorec, html, re.DOTALL)

def najdi_url(recept: str):
    vzorec = re.compile(
        r'<span></span></div></div></a><a href=(?P<url>.+*) class=',
        re.DOTALL
    )
    najdba = vzorec.search(recept)
    return najdba["url"]