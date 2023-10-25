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