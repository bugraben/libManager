# Boş bir sözlük oluştur
table_member = {}

# Örnek veriler
table_member['Buğra'] = {'soyisim': 'Işıkdemir', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}
table_member['Yakup Efe'] = {'soyisim': 'Sarıkaya', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}

# Verileri bir dosyada saklamak için dosya adı
dosya_adi = 'veri_tabani.txt'

# Verileri dosyadan okuma
try:
    with open(dosya_adi, 'r') as dosya:
        for satir in dosya:
            isim, soyisim, bolum = satir.strip().split(',')
            table_member[isim.lower()] = {'soyisim': soyisim, 'üniversite_bölüm': bolum}
except FileNotFoundError:
    print(f"'{dosya_adi}' adlı dosya bulunamadı. Yeni bir dosya oluşturulacak.")

# Veritabanındaki mevcut isimleri, soyisimleri ve üniversite bölümlerini göster
print("\nMevcut Veri Tabanı:")
for isim, bilgiler in table_member.items():
    print(f"İsim: {isim.capitalize()}, Soyisim: {bilgiler['soyisim']}, Üniversite Bölümü: {bilgiler['üniversite_bölüm']}")

# Kullanıcıdan veri eklemesini isteyelim
while True:
    print("\nVeri Ekleme Arayüzü")
    print("--------------------")
    isim = input("İsim: ").lower()
    if not isim:
        print("İsim alanı boş bırakılamaz. Lütfen bir isim girin.")
        continue

    # İsim zaten mevcutsa uyarı verelim
    if isim in table_member:
        print(f"{isim.capitalize()} zaten mevcut.")
        continue

    soyisim = input("Soyisim: ")
    if not soyisim:
        print("Soyisim alanı boş bırakılamaz. Lütfen bir soyisim girin.")
        continue

    bolum = input("Üniversite Bölümü: ")
    if not bolum:
        print("Üniversite Bölümü alanı boş bırakılamaz. Lütfen bir bölüm girin.")
        continue

    # Yeni veriyi sözlüğe ekle
    table_member[isim] = {'soyisim': soyisim, 'üniversite_bölüm': bolum}

    while True:
        devam = input("Yeni veri eklemek istiyor musunuz? (Evet ise E, Hayır ise H tuşuna basınız.): ")
        if devam.lower() == 'e':
            break
        elif devam.lower() == 'h':
            break
        else:
            print("Lütfen 'E' veya 'H' tuşlarından birine basın.")

    if devam.lower() != 'e':
        break

# Verileri dosyaya yazma
with open(dosya_adi, 'w') as dosya:
    for isim, bilgiler in table_member.items():
        dosya.write(f"{isim},{bilgiler['soyisim']},{bilgiler['üniversite_bölüm']}\n")

print("\nGüncellenmiş veri tabanı:")
for isim, bilgiler in table_member.items():
    print(f"İsim: {isim.capitalize()}, Soyisim: {bilgiler['soyisim']}, Üniversite Bölümü: {bilgiler['üniversite_bölüm']}")
