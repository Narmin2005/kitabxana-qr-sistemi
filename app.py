import qrcode
from datetime import datetime, timedelta

muellif = input("Müəllifin adı: ") 
ad = input("Oxucunun adı və soyadı: ")
tel = input("Telefon nömrəsi: ")
email = input("E-mail ünvanı: ")
kitab = input("Kitabın adı: ")
bugun = datetime.now()
qaytarma_tarixi = bugun + timedelta(days=15)
bugun_str = bugun.strftime("%d.%m.%Y")
qaytarma_str = qaytarma_tarixi.strftime("%d.%m.%Y")
melumat = (
    f"--- KİTABXANA SİSTEMİ ---\n"
    f"Müəllif: {muellif}\n" 
    f"Oxucu: {ad}\n"
    f"Tel: {tel}\n"
    f"Email: {email}\n"
    f"Kitab: {kitab}\n"
    f"Götürülmə: {bugun_str}\n"
    f"Qaytarılma: {qaytarma_str}"
)

qr_sekli = qrcode.make(melumat)
qr_sekli.save("kitabxana_sistemi.png")

print("-" * 30)
print(f"Uğurlu! Layihənin müəllifi: {muellif}")
print(f"QR kod 'kitabxana_sistemi.png' faylına yazıldı.")