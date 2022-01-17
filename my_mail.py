import os, datetime
import smtplib
from email.message import EmailMessage
import imghdr
import cv2

""" mail gonderilemiyorsa (gonderici icin) guvenlik izni linki;
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O4l98tsVh7qi9-6Opwr3JUrFe18SR4hoo6pEzgZwuDENk9zyWfsPWdZe3mrk2WPF8X19QeclxB3vfgrjBTOXPwOzyDig
"""

def Kamera_mail():
    
    try:
        cam = cv2.VideoCapture(0)
        _,img = cam.read()
        cv2.imwrite("deneme.jpg",img)

        mesaj = EmailMessage()

        mesaj["Subject"] = "Otonom Mail Deneme"
        mesaj["From"] = "kahramanxx10@gmail.com"
        mesaj["To"] = "mk10_1907@hotmail.com"

        mesaj.set_content("Merhaba, bu bir python denemesidir. Saygilarimla Mehmet Kahraman :)")
        with open("deneme.jpg","rb") as file:
            image_data = file.read()
            image_name = file.name
            image_type = imghdr.what(file.name)

        mesaj.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login("mail_address","password")
            smtp.send_message(mesaj)
        print("mail gonderildi...")
    
    except:
        print("mail gonderilemedi...")
        pass

def tespit_mail(file_name):

    try:
        mesaj = EmailMessage()

        mesaj["Subject"] = "Otonom Mail Deneme"
        mesaj["From"] = "mail_address_from"
        mesaj["To"] = "mail_address_to"

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
        mesaj.set_content("Merhaba, saat {}:{} itibariyle havadan resmi cekilen aracin serit ihlali yaptigi tespit edilmistir. Saygilarimizla GOKUCARI 21 Takimi.".format(hour,minute))

        with open("ihlal_fotolar\\"+file_name,"rb") as file:
            image_data = file.read()
            image_name = file.name
            image_type = imghdr.what(file.name)
        mesaj.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login("mail_address","password")
            smtp.send_message(mesaj)
        print("mail gonderildi...")
    
    except:
        print("mail gonderilemedi...")
        pass
