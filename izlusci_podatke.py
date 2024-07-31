import requests

def prenesi_podatke(link):
    html = requests.get(link)
    with open("html.txt", "w", encoding="utf8") as dat:
        print(html.text, file=dat)

prenesi_podatke("https://okusno.je/iskanje")