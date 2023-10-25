# hesap_makinesi.exe nin yapım aşaması:
Bu yazıyı okuyon herkese selam! bu projemde python yazılım dilini kullanarak bir uygulama dosyası yaptım, ilk öncelikle şunu bilertmek istiyorum bu uygulmada herhangi bir zararlı yazılım yoktur. uygulamamızın uzantısı exe olduğu için virüs olarak algılanması gayet doğaldır.
o zaman hadi bu dosyayı nasıl yaptığıma bir bakalım.

# ilk önce python kodlarımızı yazabilmemiz için Python adlı uygulamamızı indiriyoruz, uygulamayı ise şu adrese giderek indirebilirsiniz: https://www.python.org/downloads/

eveet uygulamamızı indirdikten sonra kurulum işlemini başlatıyoruz, sonrada .py adında bir uzantılı bir dosya oluşturmamız gerekiyor, örneğin, hesap_makinesi.py yapabilirsiniz ama unutmayın python kodlarımızı yazabilmek için uzantısının .py olması önemlidir!

sonrada bu dosyayı bir code editöründen yada direkt metin belgesindende açabilirsiniz,

# Python kodları

eveet artık paython kodlarımızı yazmaya başlayabiliriz, ilk önce ben size direkt olarak kodu vereceğim ama sizinde uygulama geliştirmeniz için pythonu öğrenmenizi tavsiye ediyorum :)

kodları buraya yazdım bu kodu .py uzantılı dosyamıza bu kodu yazıyoruz

kod:

```Python
 import os
os.system('title hesap makinesi')

def anaislem():
    while True:
        print("lütfen yapmak istediğiniz işlemin numarasını girin.")
        print("(1) toplama")
        print("(2) çıkarma")
        print("(3) çarpma")
        print("(4) bölme")
        print("(5) uygulamayı temizlemek")
        islem = input("işlem numarasını buraya giriniz: ")
        if islem == "1":
           toplamaislem = input("1. toplamak istediğiniz sayıyı giriniz: ")
           toplamaislem1 = input("2. toplamak istediğiniz sayıyı giriniz: ")
           print("sonuç: ",int(toplamaislem)+int(toplamaislem1))
           input("başka işleme geçmek için Enter a basınız.")

        if islem == "2":
           cikarmaislem = input("1. çıkarmak istediğiniz sayıyı giriniz: ")
           cikarmaislem1 = input("2. çıkarmak istediğiniz sayıyı giriniz: ")
           print("sonuç: ",int(cikarmaislem)-int(cikarmaislem1))
           input("başka işleme geçmek için Enter a basınız.")

        if islem == "3":
           carpmaislem = input("1. çarpmak istediğiniz sayıyı giriniz: ")
           carpmaislem1 = input("2. çarpmak istediğiniz sayıyı giriniz: ")
           print("sonuç: ",int(carpmaislem)*int(carpmaislem1))
           input("başka işleme geçmek için Enter a basınız.")

        if islem == "4":
           bolmeislem = input("1. bölmek istediğiniz sayıyı giriniz: ")
           bolmeislem1 = input("2. bölmek istediğiniz sayıyı giriniz: ")
           sonucbolme = int(bolmeislem) / int(bolmeislem1)
           print("sonuç: ",int(sonucbolme))
           input("başka işleme geçmek için Enter a basınız.")
        if islem == "5":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            print("konsol başarıyla temizlendi")
        if islem == "":
            print("lütfen bir değer giriniz.")
        else:
         print(anaislem())

print(anaislem())
```

