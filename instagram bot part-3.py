from selenium import webdriver
from getpass import getpass
import time
import requests
import json
import re
import os
import sys
import locale
import subprocess
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
dil=locale.getdefaultlocale()
os.system('cls' if os.name == 'nt' else 'clear')
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    if dil[0]=="tr_TR":
       print("""
    #######################################################
    #                                                     #  
    # Cüneyt TANRISEVER // Instagram BoT                  #
    #                                                     #  
    #######################################################
    """)
    else:
       print("""
    ########################################################
    #                                                      #    
    # Cüneyt TANRISEVER // Instagram BoT                   #
    #                                                      #  
    ########################################################
    """)
intro()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
sira=0
secimler=["Yapmak istediğiniz işlemi seçiniz ","Select the action you want to do "]
print(secimler[0] if dil[0] == 'tr_TR' else secimler[1])

def soru():
    global secimsor
    secim=["1) Toplu resim  indirmek için 1'i tuşlayınız.\n2) Toplu Beğeni için 2'yi tuşlayınız.\n3) Toplu beğeni kaldırmak için 3'ü tuşlayınız.\n4) Listedeki kullanıcıları otomatik takip etmek için 4'ü tuşlayınız.\n5) Listedeki kullanıcıları otomatik takip bırakmak için 5'i tuşlayınız.\n6) Takipçi listesi çekmek için 6 tuşlayınız.\n7) Takip edilenlerin listesi çekmek için 7 tuşlayınız.\n8) Takibe takip etmeyenleri takip etmeyi bırakmak için 8 tuşlayınız.\nSeçiminiz = ","1) Press 1 to download a mass picture\n2) Press 2 for a mass likes\n3) Press 3 to remove a mass likes\n4) Press 4 to automatically follow the users in the list\n5) Automatically press the users in the list Press 5 to unfollow\n6) Press 6 to take a follower list\n7) Press 7 to get a list of followers.\n8) unfollow unfollowers.\nYour choice = "]
    secimsor=input(secim[0] if dil[0] == 'tr_TR' else secim[1])
    if secimsor != '1' and secimsor != '2' and secimsor != '3' and secimsor != '4' and secimsor != '5' and secimsor != '6' and secimsor != '7' and secimsor != '8':
        intro()
        print("\n**********Hatalı cevap verdiniz tekrar deneyiniz.**********\n") 
        soru()
soru()       
sorskul=["İnstagram kullanıcı adınızı giriniz = ","Enter your username = "]

sorssifre=["İnstagram kullanıcı şifrenizi giriniz = ","Enter your user password = "]
kullaniciadi = input(sorskul[0] if dil[0] == 'tr_TR' else sorskul[1])
kulsifre = getpass(sorssifre[0] if dil[0] == 'tr_TR' else sorssifre[1])
takipetmeyenler=[]
def Basla():
    global resimlinkleri
    global driver
    global rq
    global begensssison
    global say 
    global paddrs
    global ekle
    driver = webdriver.Chrome(options=options)
    os.system('cls' if dil[0] == 'tr_TR' else 'clear')
    intro()
    bilgi=["İnstagram'a giriş yapılıyor...","Logging into instagram..."]
    print(bilgi[0] if dil[0] == 'tr_TR' else bilgi[1])
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(7)
    kulladi = driver.find_element_by_name('username')
    sifre = driver.find_element_by_name('password')
    giris = driver.find_element_by_xpath("//button[@type='submit']")
    kulladi.send_keys(kullaniciadi)
    sifre.send_keys(kulsifre)
    giris.click()
    driver.implicitly_wait(10)
    try:
        buton=driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/section/main/div/div/div/div/button")
    except NoSuchElementException:
        buton=driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button")
    buton.click()
    driver.implicitly_wait(5)
    buton2=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    buton2.click()
    addrs1="https://www.instagram.com/"
    
    driver.get(addrs1)
    say=0
    resimlinkleri=[]
    ekle="https://www.instagram.com/p/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }
    #print(driver.get_cookies())
    cookies = driver.get_cookies()
    rq=requests.session()
    begensssison=requests.session()
    for cookie in cookies:
        rq.cookies.set(cookie['name'], cookie['value'])
        begensssison.cookies.set(cookie['name'], cookie['value'])
    rq.headers.update(headers)
    #secimsor="2"
    token=rq.cookies["csrftoken"]
    headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36','X-CSRFToken':token}
    begensssison.headers.update(headers1)
def cikis():
    os.chdir("../")
    ckm=os.getppid()
    kmt="Taskkill /F /PID {}".format(ckm)
    kmt1="kill -9 {}".format(ckm)
    driver.close()
    driver.quit()
    if os.name == 'nt':
        output = subprocess.check_output(kmt, shell=True)
    else:
        output = subprocess.check_output(kmt1, shell=True)
    sys.exit()
takipci=[]
takipsor=""
def takipcilistesi(a):
    global takipsor
    sor1=["Takipçi listesi alınacak kullanıcı adını giriniz = ","Enter the name to use the follower list ="]
    sor=input(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
    takipsor=sor
    Basla()
    addrs1="https://www.instagram.com/"+sor
    driver.get(addrs1)
    tikla="document.querySelector(\"li.Y8-fY:nth-child(2) > a:nth-child(1)\").click()"
    driver.execute_script(tikla)
    time.sleep(3)
    def kaydirs():
        global takipci
        global say
        say=0
        kaydir = """a=document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP");
    a.scrollTo(0,a.scrollHeight)"""
        mesaj=["Lütfen Bekleyiniz.Takipçileriniz kayıt ediliyor.","Please wait. Your followers are being recorded."]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        while True:
            if say==2:
                kaynak=driver.page_source
                bul="<a class=\"FPmhX notranslate  _0imsa \" title=\"(.*?)\" href="
                bulunantakipci=re.findall(bul,kaynak)
                yaz=open("takipciler.txt","w")
                for i in bulunantakipci:
                    i.encode("utf-8")
                    takipci.append(i)
                    yaz.write(str(i)+"\n")
                yaz.close()
                mesaj=["Takipçilerin 'takipciler.txt' dosyasına kayıt edildi.","Your followers are registered in the 'takipciler.txt' file."]
                print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
                mesaj=["Toplam {} takipçiniz var.".format(len(takipci)),"You have a total of {} followers.".format(len(takipci))]
                print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
                break
            else:
                driver.execute_script(kaydir)
                time.sleep(2)
                onceki_kaynak=driver.page_source
                driver.execute_script(kaydir)
                time.sleep(2)
                sonraki_kaynak=driver.page_source
                if onceki_kaynak==sonraki_kaynak:
                    say+=1
                else:
                    say=0
    kaydirs()
    if a==0:
        cikis()
takipedilen=[]
def takipedilenler(a):
    if a==0:
        sor1=["Takip edilenler listesi alınacak kullanıcı adını giriniz = ","Enter the name to use the follower list ="]
        sor=input(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
        Basla()
    else:
        sor=takipsor
    addrs1="https://www.instagram.com/"+sor
    driver.get(addrs1)
    git="document.querySelector(\"#react-root > section > main > div > header > section > ul > li:nth-child(3) > a\").click()"
    driver.execute_script(git)
    time.sleep(3)
    def kaydirs():
        say1=0
        global takipedilen
        kaydir = """a=document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP");
    a.scrollTo(0,a.scrollHeight)"""
        mesaj=["Lütfen Bekleyiniz.Takip edilenler kayıt ediliyor.","Please wait. Your followers are being recorded."]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        while True:
            if say1==2:
                kaynak=driver.page_source
                bul="<a class=\"FPmhX notranslate  _0imsa \" title=\"(.*?)\" href="
                bulunantakipci=re.findall(bul,kaynak)
                yaz=open("takipedilenler.txt","w")
                for i in bulunantakipci:
                    i.encode("utf-8")
                    takipedilen.append(i)
                    yaz.write(str(i)+"\n")
                yaz.close()
                mesaj=["Takip ettikleriniz 'takipedilenler.txt' dosyasına kayıt edildi.","Your followers are saved in the 'takipedilenler.txt' file"]
                print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
                mesaj=["Toplam {} takip ettiğiniz kişi var.".format(len(takipedilen)),"You have a total of {} people you follow.".format(len(takipedilen))]
                print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
                break
            else:
                driver.execute_script(kaydir)
                time.sleep(2)
                onceki_kaynak=driver.page_source
                driver.execute_script(kaydir)
                time.sleep(2)
                sonraki_kaynak=driver.page_source
                if onceki_kaynak==sonraki_kaynak:
                    say1+=1
                else:
                    say1=0
    kaydirs()
    if a==0:
        cikis()
def takiptencikma(a):
    if a==1:
        oku=open("kullanicilar.txt","r").readlines()
        Basla()
        mesaj=["Kullanıcı listesi okunuyor","Reading user list"]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        mesaj=["Kullanıcılar takipten çıkarılıyor...","Users are unfollowed..."]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        for i in oku:
            urlprf=rq.get("https://www.instagram.com/"+i.replace("\n","").replace("\r","")+"?__a=1")
            kynk=urlprf.content
            dex4=json.loads(kynk)
            resim=dex4["graphql"]["user"]["id"]
            takipadres="https://www.instagram.com/web/friendships/{}/unfollow/".format(resim)
            user=begensssison.post(takipadres,data="")
        mesaj=["Toplam {} tane kullanıcı takipten çıkarıldı".format(len(oku)),"Total {} users unfollowed".format(len(oku))]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        cikis()
    elif a==2:
        
        mesaj=["Kullanıcılar takipten çıkarılıyor...","Users are unfollowed..."]
        print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
        for i in takipetmeyenler:
            urlprf=rq.get("https://www.instagram.com/"+i.replace("\n","").replace("\r","")+"?__a=1")
            kynk=urlprf.content
            dex4=json.loads(kynk)
            resim=dex4["graphql"]["user"]["id"]
            takipadres="https://www.instagram.com/web/friendships/{}/unfollow/".format(resim)
            user=begensssison.post(takipadres,data="")
    
if secimsor=="1":
    Basla()
    sor1=["Resimlerini İndirmek veya beğeni için İstediğiniz Kullanıcıyı Giriniz = ","Enter User to Download Pictures or Likes = "]
    sor=input(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
    addrs="https://www.instagram.com/"+sor+"/"
    paddrs=addrs+"?__a=1"
    driver.get(addrs)
    def say1():
        global say
        say+=1
        time.sleep(3)
    sor1=["Resimler seçiliyor. Lütfen bekleyiniz...","Pictures are selected. Please wait..."]
    print(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
        
    while True:
        if say==2:
            break
        else:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak=driver.page_source
            ara=re.findall("<a href=\"/p/(.*?)/\" tabindex=\"0\">",kaynak)
            for i in ara:
                ekle1=ekle+i+"/?__a=1"
                resimlinkleri.append(ekle1)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak1=driver.page_source
                    
            if kaynak==kaynak1:
                say1()
            else:
                pass
    resimlinkleri=list(set(resimlinkleri))
    dizin=os.path.isdir(sor)
    try:
        if dizin:
            kmt="RD /S /Q {}".format(sor)
            lnxkmt="rm -rf {}".format(sor)
            os.system(kmt if os.name=="nt" else lnxkmt)
            shutil.rmtree(sor)
    except:
        pass
    os.mkdir(sor)
    os.chdir(sor)
    sira=0
    
    prf=rq.get(paddrs)
    kaynak2=prf.content
    a="<html><head></head><body><pre style=\"word-wrap: break-word; white-space: pre-wrap;\">"
    dex4=json.loads(kaynak2)
    resim=dex4["graphql"]["user"]["profile_pic_url_hd"]
    rsm=resim.replace("amp;","")
    git=rq.get(rsm)
    open(sor+"_profil.jpg", 'wb').write(git.content)

    resimsayisi=0
    bul="src\":\"(.*?)}],\"accessibility_caption"
    sor2=["İndirme başladı. Lütfen bekleyiniz...","Download started. Please wait..."]
    print(sor2[0] if dil[0] == 'tr_TR' else sor2[1])
    for i in resimlinkleri:
        git=rq.get(i)
        dex1=git.content
        cc= str(dex1).encode("utf-8")
        ara=re.findall(bul,str(cc))
        if len(ara)!=0:
            resimsayisi+=len(ara)
        for j in ara:
            ayir=str(j).split("src")
            a=str(ayir[-1]).split(",")
            urlc=a[0].replace("\":","").replace("\\\\u0026","&").replace("\"","")
            git1=rq.get(urlc)
            sira+=1
            ad=sor+str(sira)+".jpg"
            open(ad, 'wb').write(git1.content)
    ab=[str(sira+1)+" tane resim indirildi.",str(sira)+"  image has been downloaded."]
    print(ab[0] if dil[0] == 'tr_TR' else ab[1])
    print("--------------------------------------------------")
    cikis()
elif secimsor=="2":
    sor1=["Toplu gönderi beğeni için kullanıcı adınını giriniz = ","Enter username for mass post like ="]
    sor=input(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
    Basla()
    addrs="https://www.instagram.com/"+sor+"/"
    paddrs=addrs+"?__a=1"
    driver.get(addrs)
    def say1():
        global say
        say+=1
        time.sleep(3)
    sor1=["Gönderiler seçiliyor. Lütfen bekleyiniz...","Selecting posts. Please wait..."]
    print(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
        
    while True:
        if say==2:
            break
        else:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak=driver.page_source
            ara=re.findall("<a href=\"/p/(.*?)/\" tabindex=\"0\">",kaynak)
            for i in ara:
                ekle1=ekle+i+"/?__a=1"
                resimlinkleri.append(ekle1)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak1=driver.page_source
                    
            if kaynak==kaynak1:
                say1()
            else:
                pass
    resimlinkleri=list(set(resimlinkleri))
    for i in resimlinkleri:
       # print (i)
        prf=rq.get(i)
        kaynak2=prf.content
        dex4=json.loads(kaynak2)
        resim=dex4["graphql"]["shortcode_media"]["id"]
        #print(resim)
        begen="https://www.instagram.com/web/likes/{}/like/".format(resim)
        yardir=begensssison.post(begen,data="")
    print("{} gönderiye ve içindekilere like atıldı".format(len(resimlinkleri)))
    cikis()
elif secimsor=="3":
    sor1=["Toplu gönderi beğeni kaldırmak için kullanıcı adınını giriniz = ","Enter username for mass post unlike ="]
    sor=input(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
    Basla()
    addrs="https://www.instagram.com/"+sor+"/"
    paddrs=addrs+"?__a=1"
    driver.get(addrs)
    def say1():
        global say
        say+=1
        time.sleep(3)
    sor1=["Gönderiler seçiliyor. Lütfen bekleyiniz...","Selecting posts. Please wait..."]
    print(sor1[0] if dil[0] == 'tr_TR' else sor1[1])
        
    while True:
        if say==2:
            break
        else:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak=driver.page_source
            ara=re.findall("<a href=\"/p/(.*?)/\" tabindex=\"0\">",kaynak)
            for i in ara:
                ekle1=ekle+i+"/?__a=1"
                resimlinkleri.append(ekle1)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            kaynak1=driver.page_source
                    
            if kaynak==kaynak1:
                say1()
            else:
                pass
    resimlinkleri=list(set(resimlinkleri))
    for i in resimlinkleri:
       # print (i)
        prf=rq.get(i)
        kaynak2=prf.content
        dex4=json.loads(kaynak2)
        resim=dex4["graphql"]["shortcode_media"]["id"]
        #print(resim)
        begenme="https://www.instagram.com/web/likes/{}/unlike/".format(resim)
        yardir=begensssison.post(begenme,data="")

    mesaj=["{} gönderiye ve içindekilere unlike atıldı".format(len(resimlinkleri)),"disliked the post and its contents".format(len(resimlinkleri))]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    cikis()
elif secimsor=="4":
    oku=open("kullanicilar.txt","r").readlines()
    Basla()
    mesaj=["Kullanıcı listesi okunuyor","Reading user list"]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    mesaj=["Kullanıcılar takip ediliyor...","Users are tracked..."]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    for i in oku:
        urlprf=rq.get("https://www.instagram.com/"+i.replace("\n","").replace("\r","")+"?__a=1")
        kynk=urlprf.content
        dex4=json.loads(kynk)
        resim=dex4["graphql"]["user"]["id"]
        takipadres="https://www.instagram.com/web/friendships/{}/follow/".format(resim)
        user=begensssison.post(takipadres,data="")
    print("Toplam {} tane kullanıcı takip edildi".format(len(oku)))
    mesaj=["Toplam {} tane kullanıcı takip edildi".format(len(oku)),"Total {} users followed".format(len(oku))]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    cikis()

elif secimsor=="5":
    takiptencikma(1)


elif secimsor=="6":
    takipcilistesi(0)
elif secimsor=="7":
    takipedilenler(0)
elif secimsor=="8":
    takipcilistesi(1)
    takipedilenler(1)
    yaz=open("takip_etmeyenler_listesi.txt","w")
    for i in takipedilen:
        if i not in takipci:
            takipetmeyenler.append(i)
            i.encode("utf-8")
            yaz.write(str(i)+"\n")
    yaz.close()
    
    mesaj=["Takip etmeyenler \"takip_etmeyenler_listesi.txt\" dosyasına yazdırıldı.","Unfollowers have been printed to \"takip_etmeyenler_listesi.txt\"."]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    takiptencikma(2)
    mesaj=["Toplam {} tane kullanıcı takipten çıkarıldı".format(len(takipetmeyenler)),"Total {} users unfollowed".format(len(takipetmeyenler))]
    print(mesaj[0] if dil[0] == 'tr_TR' else mesaj[1])
    cikis()
else:
    print("Hatalı seçim")

















