# Boş bir sözlük oluştur
table_member = {}

# örnek veriler
table_member['Buğra'] = {'soyisim': 'Işıkdemir', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}
table_member['Yakup Efe'] = {'soyisim': 'Sarıkaya', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}

# Tüm verileri ekrana yazdır
print("Tüm veriler:")
for isim, bilgiler in table_member.items():
    print(f"İsim: {isim} Soyisim: {bilgiler['soyisim']}, Üniversite Bölümü: {bilgiler['üniversite_bölüm']}")

# Kullanıcıdan veri eklemesini isteyelim
while True:
    isim = input("İsim: ")
    if not isim:
        print("İsim alanı boş bırakılamaz. Lütfen bir isim girin.")
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

print("\nGüncellenmiş veri tabanı:")
for isim, bilgiler in table_member.items():
    print(f"İsim: {isim} Soyisim: {bilgiler['soyisim']}, Üniversite Bölümü: {bilgiler['üniversite_bölüm']}")
