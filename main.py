#opencv-pyhton kütüphanesi kuruldu import edildi
import cv2

yuz_kutuphanesi = cv2.CascadeClassifier(
    r"classifier/haarcascade_frontalface_default.xml")
#haarcascade_frontalface_default.xml kütüphanesi yüzü bulur
#haarcascade_eye_tree_eyeglasses.xml kütüphanesi gözleri bulur
#okuyacağı resimin yolunu tanımlıyoruz
img = cv2.imread(r"fotograflar/selin.jpg")
#renk ayarları
gri = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

yuzler = yuz_kutuphanesi.detectMultiScale(gri,1.1,4)

#x ve y koordinatlarına bakıp sonrada yükseklik ve genişliğine bakıp istediğimiz resmi seçiyor
for(x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),3)

#fotoğrafı tanımlama kodu
cv2.imshow('img',img)
#seçilen resmi gösterip hemen kapanmaması için resmi bekletiyoruz.
cv2.waitKey(0)