# Digital library management system by Bugra, Ozgur, Talip, Yakup and Samet
# Project for Computer Programming Lab Lecture


def ödünç_ver(kitap_adı, okur_id): 
#okur_id  okurun üyelik numarasını temsil ediyor
#ödünç_ver kütüphanenin okura verdiğini ifade ediyor
    if kitap_adı in kitaplar:
        if kitaplar[kitap_adı]["durum"] == "mevcut":
            kitaplar[kitap_adı]["durum"] = "ödünç alındı"
            kitaplar[kitap_adı]["ödünç_alan"] = okur_id
            if okur_id in ödünç_alınan_kitaplar:
                ödünç_alınan_kitaplar[okur_id].append(kitap_adı)
            else:
                ödünç_alınan_kitaplar[okur_id] = [kitap_adı]
            print(f"{kitap_adı} kitabı {okur_id} tarafından ödünç alındı.")
        else:
            print("Bu kitap zaten ödünç alınmış.")
    else:
        print("Bu kitap kütüphanede mevcut değil.")

def ödünç_alınan_kitapları_listele(okur_id):
    if okur_id in ödünç_alınan_kitaplar:
        print(f"{okur_id} tarafından ödünç alınan kitaplar:")
        for kitap_adı in ödünç_alınan_kitaplar[okur_id]:
            print(f"{kitap_adı} - {kitaplar[kitap_adı]['yazar']}")
    else:
        print(f"{okur_id} tarafından ödünç alınan kitap bulunmamaktadır.")
