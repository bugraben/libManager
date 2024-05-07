
table_books = {
# STATUS 0 REPRESENTS THAT THE BOOK IS IN THE LIBRARY, WHILE STATUS 1 REPRESENTS THAT THE BOOK HAS BEEN BORROWED.
# The barcodes are arranged in XYZ order. Where X represents the genre of the book, Y denotes the author, and Z represents the book itself.

    "000": {
        "name": "NAME",
        "author": "AUTHOR",
        "location": "LOCATION",
        "status": 0
    },
#1 is for biography
    "111": {
        "name": "Nutuk",
        "author": "Mustafa Kemal Atatürk",
        "location": "A1",
        "status": 0
    },
    "121": {
    "name": "Steve Jobs",
    "author": "Walter Isaacson",
    "location": "A1",
    "status": 0
    },
    "131": {
    "name": "Elon Musk",
    "author": "Ashlee Vance",
    "location": "A1",
    "status": 0
    },

    "141": {
        "name": "Wizard: The Lİfe and Times of Nikola Tesla : Biography of a Genius",
        "author": "Marc J. Seifer",
        "location": "A1",
        "status": 0
    },
# 2 is for Turkish Literature
    "211": {
        "name": "Kürk Mantolu Madonna",
        "author": "Sabahattin Ali",
        "location": "B1",
        "status": 0
    },

    "212": {
        "name": "İçimizdeki Şeytan",
        "author": "Sabahattin Ali",
        "location": "B1",
        "status": 0
    },
    "213": {
        "name": "Kuyucaklı Yusuf",
        "author": "Sabahattin Ali",
        "location": "B1",
        "status": 0
    },
    "214": {
        "name": "Sırça Köşk",
        "author": "Sabahattin Ali",
        "location": "B1",
        "status": 0
    },
    "215": {
        "name": "Yeni Dünya",
        "author": "Sabahattin Ali",
        "location": "B1",
        "status": 0
    },
    "221": {
        "name": "Tutunamayanlar",
        "author": "Oğuz Atay",
        "location": "B2",
        "status": 0
    },
    "222": {
        "name": "Tehlikeli Oyunlar",
        "author": "Oğuz Atay",
        "location": "B2",
        "status": 0
    },
    "223": {
        "name": "Korkuyu Beklerken",
        "author": "Oğuz Atay",
        "location": "B2",
        "status": 0
    },
    "224": {
        "name": "Bir Bilim Adamının Romanı",
        "author": "Oğuz ATAY",
        "location": "B2",
        "status": 0
    },
    "231": {
        "name": "Yalnız Efe",
        "author": "Ömer Seyfettin",
        "location": "B3",
        "status": 0
    },
    "232": {
        "name": "Kaşağı",
        "author": "Ömer Seyfettin",
        "location": "B3",
        "status": 0
    },
    "233": {
        "name": "Seçme Hikayeler",
        "author": "Ömer Seyfettin",
        "location": "B3",
        "status": 0
    },
    "234": {
        "name": "Perili Köşk",
        "author": "Ömer Seyfettin",
        "location": "B3",
        "status": 0
    },
# 3 for Japanese litarature
    "311": {
        "name": "İnsanlığımı Yitirirken",
        "author": "Osamu Dazai",
        "location": "C1",
        "status": 0
    },
    "312": {
        "name": "Öğrenci Kız",
        "author": "Osamu Dazai",
        "location": "C1",
        "status": 0
    },
    "313": {
        "name": "Pandora'nın Kutusu",
        "author": "Öğrenci Kız",
        "location": "C1",
        "status": 0
    },
    "321": {
        "name": "Raşomon",
        "author": "Ryunosuke Akutagawa",
        "location": "C1",
        "status": 0
    },
    "331": {
        "name": "Sahilde Kafka",
        "author": "Haruki Murakami",
        "location": "C1",
        "status": 0
    },
    "332": {
        "name": "1Q84",
        "author": "Haruki Murakami",
        "location": "C1",
        "status": 0
    },
    "333": {
        "name": "İmkansızın Şarkısı",
        "author": "Haruki Murakami",
        "location": "C2",
        "status": 0
    },
    "341": {
        "name": "Şeytanın Çırağı",
        "author": "Shiro Hamao",
        "location": "C2",
        "status": 0
    },
    "351": {
        "name": "Yaban Kazı",
        "author": "Ogai Mori",
        "location": "C2",
        "status": 0
    },
# 4 for Russian Literature
    "411" : {
        "name" : "Suç ve Ceza",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "412" : {
        "name" : "İnsancıklar",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "413" : {
        "name" : "Yeraltından Notlar",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "414" : {
        "name" : "Karamazov Kardeşler",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "415" : {
        "name" : "Kumarbaz",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "416" : {
        "name" : "Öteki",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "417" : {
        "name" : "Ölüler Evinden Anılar",
        "author" : "Fyodor Dostoyevski",
        "location" : "D1",
        "status": 0
    },
    "421" : {
        "name" : "Savaş ve Barış",
        "author" : "Lev Tolstoy",
        "location" : "D2",
        "status": 0
    },
    "422" : {
        "name" : "Anna Karenina",
        "author" : "Lev Tolstoy",
        "location" : "D2",
        "status": 0
    },
    "423" : {
        "name" : "İnsan Ne ile Yaşar",
        "author" : "Lev Tolstoy",
        "location" : "D2",
        "status": 0
    },
    "424" : {
        "name" : "Hacı Murat",
        "author" : "Lev Tolstoy",
        "location" : "D2",
        "status": 0
    },
    "431" : {
        "name" : "Ölü Canlar",
        "author" : "Nikolay Gogol",
        "location" : "D3",
        "status": 0
    },
    "432" : {
        "name" : "Palto",
        "author" : "Nikolay Gogol",
        "location" : "D3",
        "status": 0
    },
    "433" : {
        "name" : "Burun",
        "author" : "Nikolay Gogol",
        "location" : "D3",
        "status": 0
    },
    "434" : {
        "name" : "Taras Bulba",
        "author" : "Nikolay Gogol",
        "location" : "D3",
        "status": 0
    },
# 5 is for Germanic Literature
    "511" : {
        "name" : "Dönüşüm",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "512" : {
        "name" : "Babaya Mektup",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "513" : {
        "name" : "Şato",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "514" : {
        "name" : "Milena'ya Mektuplar",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "515" : {
        "name" : "Babaya Mektup",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "516" : {
        "name" : "Aforizmalar",
        "author" : "Franz Kafka",
        "location" : "E1",
        "status": 0
    },
    "521" : {
        "name" : "Satranç",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "522" : {
        "name" : "Bilinmeyen Bir Kadının Mektubu",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "523" : {
        "name" : "Amok Koşucusu",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "524" : {
        "name" : "Korku",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "525" : {
        "name" : "Olağanüstü Bir Gece",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "526" : {
        "name" : "Kızıl",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "527" : {
        "name" : "Hayatın Mucizeleri",
        "author" : "Stefan Zweig",
        "location" : "E2",
        "status": 0
    },
    "531" : {
        "name" : "Genç Werther'in Acıları",
        "author" : "Johann Wolfgang Von Goethe",
        "location" : "E3",
        "status": 0
    },
    "541" : {
        "name" : "Böyle Buyurdu Zerdüşt",
        "author" : "Friedrich Nietzche",
        "location" : "E3",
        "status": 0
    },
    "542" : {
        "name" : "İyinin ve Kötünün Ötesinde",
        "author" : "Friedrich Nietzche",
        "location" : "E3",
        "status": 0
    },
    "543" : {
        "name" : "Tregedyanın Doğuşu",
        "author" : "Friedrich Nietzche",
        "location" : "E3",
        "status": 0
    },











}

total_books = len(table_books) - 1

print("Total number of books :", total_books)