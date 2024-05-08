def geri_al(kitap_adı, okur_id):
#geri_al= kitabın okur tarafından teslim edildiğini temsil ediyor
    if kitap_adı in kitaplar:
        if kitaplar[kitap_adı]["durum"] == "ödünç alındı" and kitaplar[kitap_adı]["ödünç_alan"] == okur_id:
            kitaplar[kitap_adı]["durum"] = "mevcut"
            kitaplar[kitap_adı]["ödünç_alan"] = None

            # Kullanıcının ödünç aldığı kitaplar listesinden çıkar
            if okur_id in ödünç_alınan_kitaplar and kitap_adı in ödünç_alınan_kitaplar[okur_id]:
                ödünç_alınan_kitaplar[okur_id].remove(kitap_adı)
                print(f"{kitap_adı} kitabı {okur_id} tarafından geri getirildi.")
        else:
            print("Bu kitap zaten mevcut veya başka bir kullanıcı tarafından ödünç alınmış.")
    else:
        print("Bu kitap kütüphanede mevcut değil.")