import requests
import re

def prenesi_podatke(link):
    html = requests.get(link)
    # with open("html.txt", "w", encoding="utf8") as dat:
    #     print(html.text, file=dat)
    return html.text

# prenesi_podatke("https://okusno.je/iskanje")

def najdi_recept(html: str):
    vzorec = r'<span></span></div></div></a><a href=/recept/.*?<span></span>'
    return re.findall(vzorec, html, flags=re.DOTALL)

print(len(najdi_recept(prenesi_podatke("https://okusno.je/iskanje"))))
