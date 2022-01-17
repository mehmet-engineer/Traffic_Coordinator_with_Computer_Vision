import datetime

def report(dosya_1,dosya_2,arac_sayaci):
    
    print("Rapor hazirlaniyor...")

    dosya_2.close()

    zaman = datetime.datetime.now()
    saat = zaman.hour
    dk = zaman.minute
    if saat < 10:
        hour = "0" + str(saat)
    else:
        hour = saat
    if dk < 10:
        minute = "0" + str(dk)
    else:
        minute = dk

    tarih = "{}.{}.{}".format(zaman.day,zaman.month,zaman.year)

    dosya_2 = open("ihlal_fotolar\\ihlaller.txt", "r")
    ihlaller = dosya_2.read()

    string = """
    
    GOKUCARI 21 TRAFIK KOORDINATORU IHA
    TRAFIK RAPORU
    ------------------

    Gorevin yapildigi tarih = {}
    Gorevin yapildigi saat = {}:{}

    TESPIT EDILEN ARACLAR:
    {} Araba,
    {} Agir Arac,
    olmak uzere toplam {} tasit tespit edildi.

    DENETLENEN SERIT IHLALLERI:
{}
    -----------------------------------------------------------------

    """.format(tarih,hour,minute,arac_sayaci[0],arac_sayaci[1],str(arac_sayaci[0]+arac_sayaci[1]),ihlaller)

    dosya_1.write(string)
    dosya_1.close()

    print("Rapor olusturuldu.")