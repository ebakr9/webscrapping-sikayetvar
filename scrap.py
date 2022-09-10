import requests
import pandas as pd
from bs4 import BeautifulSoup
sirketismi = "geldipazarcom"
url1 = "https://www.sikayetvar.com/"+sirketismi
liste = ["Şirket","Başlık","Keyword","Çözüldü mü?"]
useragent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}


page = requests.get(url1,headers=useragent)
icerik = BeautifulSoup(page.content,"html.parser")

#marka ismi
company = icerik.find('h1', {'class': 'brand-name'}).get_text()
print(company+"ile ilgili şikayetler!")

#tüm yorumlardan tek başlık çekme
genelsikayet = icerik.find("div",{"class":"brand-detail-complaint-list"})
tumbaslik = genelsikayet.find_all("h2",{"class":"complaint-card__title"})
for tekbaslik in tumbaslik:
    print(tekbaslik.text)
#print(len(tumbaslik))

#Birden fazla sayfa oldugunu bıldırme
sayfasayisi = icerik.find_all("a",{"class":"pager"})
for teksayfa in sayfasayisi:
    teksayfatext = (teksayfa.text)
#print(teksayfatext)
maxnumberofpage = int(teksayfatext)+1
dongusayisi = 1
while dongusayisi < maxnumberofpage:
    url2 = "https://www.sikayetvar.com/"+sirketismi+"?page="+str(dongusayisi)
    dongusayisi += 1
    page = requests.get(url2,headers=useragent)
    icerik = BeautifulSoup(page.content,"html.parser")

    #marka ismi
    company = icerik.find('h1', {'class': 'brand-name'}).get_text()

    #tüm yorumlardan tek başlık çekme
    genelsikayet = icerik.find("div",{"class":"brand-detail-complaint-list"})
    tumbaslik = genelsikayet.find_all("h2",{"class":"complaint-card__title"})
    for tekbaslik in tumbaslik:
        print(tekbaslik.text)
    print("Şikayet Sayısı: "+str(len(tumbaslik)))
    #Çözülen sorunları analiz etme
    cozulensikayetler = icerik.find_all("div",{"class":"solved-badge"})
    print("Toplam çözülen şikayet sayısı: "+str(len(cozulensikayetler)))




 



