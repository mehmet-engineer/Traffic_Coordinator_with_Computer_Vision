# Genel Trafik Koordinatörü Algoritması

Algoritma, insansız hava araçlarına trafik denetleyicisi görev kabiliyeti kazandırmak üzere tasarlanmıştır. Özellikle Quadcopter İHA'ların (drone) kamerasına entegre 
edilmek üzere Python dilinde şahsımca özgün olarak geliştirilmiştir. Günümüzde birçok araç sürücüsü emniyet şeridini kullanarak diğer sürücülerin hakkını gasp etmekte,
trafikteki adalet duygusunun sarsılmasına sebep olmaktadır. Bu soruna bir çözüm olarak geliştirilen Trafik Koordinatörü İHA'nın görev algoritması araç tespiti, 
emniyet şeridi tespiti ve denetleme olmak üzere 3 ayrı bölümden oluşmaktadır. Tek bir yazılım döngüsü içerisinde araçların şerit içerisinde seyri denetlenebilmektedir. 
Araçlar şerit ihlali yaptığı sıradaki görüntüsü İHA kamerası üzerinden yüksek çözünürlüklü olarak alınabilmektedir. Alınan bu ihlal fotoğrafları anlık olarak mail 
yoluyla ilgili kuruma iletilmektedir.


Emniyet şeridi tespiti için “Hough Line Detection” teorisi kullanılmıştır. “YOLOv4-tiny” yöntemiyle tespit edilen araçlar
