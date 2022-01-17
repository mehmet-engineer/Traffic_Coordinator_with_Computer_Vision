# Genel Trafik Koordinatörü Algoritması

Algoritma, insansız hava araçlarına trafik denetleyicisi görev kabiliyeti kazandırmak üzere tasarlanmıştır. Özellikle Quadcopter İHA'ların (drone) kamerasına entegre 
edilmek üzere Python dilinde şahsımca özgün olarak geliştirilmiştir. Günümüzde birçok araç sürücüsü emniyet şeridini kullanarak diğer sürücülerin hakkını gasp etmekte,
trafikteki adalet duygusunun sarsılmasına sebep olmaktadır. Bu soruna bir çözüm olarak geliştirilen Trafik Koordinatörü İHA'nın görev algoritması araç tespiti, 
emniyet şeridi tespiti ve denetleme olmak üzere 3 ayrı bölümden oluşmaktadır. Tek bir yazılım döngüsü içerisinde araçların şerit içerisinde seyri denetlenebilmektedir. 
Araçlar şerit ihlali yaptığı sıradaki görüntüsü İHA kamerası üzerinden yüksek çözünürlüklü olarak alınabilmektedir. Alınan bu ihlal fotoğrafları anlık olarak mail 
yoluyla ilgili kuruma iletilmektedir.

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/algoritma.png)


Trafik araçlarının tanınması için YOLO V4 Tiny nesne tespit algoritması kullanılmıştır. Tespit edilen kara araçları araba, otobüs, ağır vasıta olmak üzere 3 ayrı kategoride değerlendirilmektedir. Yazılımda araçların sınıflarına göre sayımı yapılmaktadır. Böylece trafik yoğunluğu belirlenmektedir.
Araç Tespiti ve YOLO V4 için -> https://github.com/mehmet-engineer/YOLO_V4_Arac_Kontrol_Algoritmasi

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/arac_tespit.png)


Emniyet şeridi tespiti için “Hough Line” teorisi kullanılmıştır. Algılanan şeritlerin konumuna göre araçların seyri denetlenebilmekte ve ihlal gerçekleştiğinde anlık olarak bildirim sağlanabilmektedir.
Şerit Tespiti ve HoughLine Teorisi için -> https://github.com/mehmet-engineer/OpenCV_Serit_Tespit_Yazilimi

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/serit.png)

