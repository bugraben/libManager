# Digital library management system by Bugra, Ozgur, Talip, Yakup and Samet
# Project for Computer Programming Lab Lecture

def get_item(table, id=None, query=None):
    '''
    :param table: Table to search in
    :param id:  Item to search for
    :param query: Query for searching in book informations. Returns all items including that query. id param will be
    ignored if set.
    '''
    if query:
        print(f'{query} icin arama sonuclari listeleniyor:')
        for id in table.keys():
            for info in table[id].keys():
                try:
                    table[id][info].index(query)
                    print('-------')
                    get_item(id)
                    print('-------')
                except ValueError:
                    continue
            print('Sorgu tamamlandi')
    else:
        try:
            print('ID:', id)
            for info in table[id].keys():
                print(f'{info}: {table[id][info]}')
        except KeyError:
            print('Girdi mevcut degil.')


def add_item(table):
    '''
    :param table: Table to add item
    '''
    try:
        id = int(input('ID: '))
    except ValueError:
        print('ID bilgisi yalniz rakamlardan olusmalidir')
        return

    if table.get(id):
        print('Bu ID zaten kayitli.')
        print()
        get_item(kitaplar, id)
        print()
    else:
        table[id] = {}
        i = 0
        while i < len(table[0]):
            info = table[0][i]
            inp = input(f'{info}: ')
            if inp:
                table[id][info] = inp
                i += 1
            else:
                print('Bilgi bos gecilemez')
        print('Girdi eklendi.')


# Borrow and Return functions


def borrow_book(book_id):
    """Function to borrow a book from the library using its ISBN id.
    Args:
        book_id(int): Book's ISBN id.
    Returns: Strings with information about book's borrow status.
    """

    if book_id in table_library.keys() and table_library[book_id][1]:
        table_library[book_id][1] = False
        return f" {book_id} ISBN'li kitap iade edilmistir."
    else:
        return "Bu kitap mevcut değil veya ödünç alinmistir."


def return_book(book_id):
    """Function to return a borrowed book to the library by using ISBN id.
    Args:
        book_id(int): Book's ISBN id.
    Returns: Strings with information about book's borrow and return status.
    """
    if book_id in table_library.keys() and not table_library[book_id][1]:
        table_library[book_id][1] = True
        return f"{book_id} ISBN'li kitap iade edilmistir."
    else:
        return "Bu kitap kütüphanemizde değil ya da ödünç alınmadı."


# Boş bir sözlük oluştur
table_member = {}

# örnek veriler
table_member['Buğra'] = {'soyisim': 'Işıkdemir', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}
table_member['Yakup Efe'] = {'soyisim': 'Sarıkaya', 'üniversite_bölüm': 'Bilgisayar Bilimleri'}

# Tüm verileri ekrana yazdır
print("Tüm veriler:")
for isim, bilgiler in table_member.items():
    print(f"İsim: {isim} Soyisim: {bilgiler['ssoyisim']}, Üniversite Bölümü: {bilgiler['üniversite_bölüm']}")

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
