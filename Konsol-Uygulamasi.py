from consolemenu import SelectionMenu


# 1. Sorumuz k'nıncı en küçük elemanı bulma
def k_kucuk(k, liste):
    liste.sort()
    return liste[k - 1]


# 2. Sorumuz En Yakın Çifti Bulma
def en_yakin_cift(hedef, liste):
    liste.sort()
    en_yakin_cift = None
    min_fark = float('inf')
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(hedef - toplam)
            if fark < min_fark:
                min_fark = fark
                en_yakin_cift = (liste[i], liste[j])
    return en_yakin_cift


# 3. Sorumuz Bir Listenin Tekrar Eden Elemanlarını Bulma
def tekrar_eden_elemanlar(liste):
    return [x for x in set(liste) if liste.count(x) > 1]


# 4. Sorumuz Matris Çarpımı
def matris_carpimi(a, b):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*b)] for row in a]


# 5. Sorumuz Bir Metin Dosyasındaki Kelimelerin Frekansını Bulma
def kelime_frekansi(dosya_yolu):
    with open(dosya_yolu, 'r') as dosya:
        kelimeler = dosya.read().split()
    frekans = {kelime: kelimeler.count(kelime) for kelime in set(kelimeler)}
    return frekans


# 6. Sorumuz Liste İçinde En Küçük Değeri Bulma
def en_kucuk_deger(liste, n=0, kucuk=None):
    if n == len(liste):
        return kucuk
    elem = liste[n]
    if kucuk is None:
        return en_kucuk_deger(liste, n + 1, elem)
    elif elem < kucuk:
        return en_kucuk_deger(liste, n + 1, elem)
    else:
        return en_kucuk_deger(liste, n + 1, kucuk)


# 7. Sorumuz Karekök Fonksiyonu
def karekok(n, x0=1, tol=1e-10, maxiter=500, iter_count=0):
    hata = abs(x0 ** 2 - n)
    if hata < tol or iter_count >= maxiter:
        return x0
    else:
        x = 0.5 * (x0 + n / x0)
        return karekok(n, x, tol, maxiter,iter_count+1)

# 8. Sorumuz En Büyük Ortak Bölen Bulma
def eb_ortak_bolen(a, b):
    if b == 0:
        return a
    return eb_ortak_bolen(b, a % b)


# 9. Sorumuz Asal Veya Değil olup olmadığını bulma
def asal_veya_degil(n, bolen=2):
    if n < 2:
        return "Asal Değil"
    if bolen * bolen > n:
        return "Asal"
    if n % bolen == 0:
        return "Asal Değil"
    return asal_veya_degil(n, bolen + 1)


# 10. Sorumuz Daha Hızlı Fibonacci Hesabı
def hizlandirici(n, k, fibk, fibk1):
    if k == n:
        return fibk
    return hizlandirici(n, k + 1, fibk + fibk1, fibk)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return hizlandirici(n, 2, 1, 0)


# Kullandığım Menü
def ana_menu():
    while True:
        menu = SelectionMenu([
            "k’nıncı En Küçük Elemanı Bulma",
            "En Yakın Çifti Bulma",
            "Bir Listenin Tekrar Eden Elemanlarını Bulma",
            "Matris Çarpımı",
            "Bir Text Dosyasındaki Kelimelerin Frekansını Bulma",
            "Liste İçinde En Küçük Değeri Bulma",
            "Karekök Fonksiyonu",
            "En Büyük Ortak Bölen",
            "Asal Veya Değil",
            "Daha Hızlı Fibonacci Hesabı"
        ], "Hangi işlemi yapmak istersiniz?")
        menu.show()

        secilen_soru = menu.selected_option

        if secilen_soru == len(menu.items) - 1:  # Kullanıcı "Çıkış"ı seçtiyse programı sonlandır
            break

        if secilen_soru == 0:
            k = int(input("k değerini giriniz: "))
            liste = list(map(int, input("Listeyi boşluklarla ayırarak giriniz: ").split()))
            sonuc = k_kucuk(k, liste)
            print(f"{k}. en küçük eleman: {sonuc}")
        elif secilen_soru == 1:
            hedef = int(input("Hedef sayıyı giriniz: "))
            liste = list(map(int, input("Listeyi boşluklarla ayırarak giriniz: ").split()))
            sonuc = en_yakin_cift(hedef, liste)
            print(f"En yakın çift: {sonuc}")
        elif secilen_soru == 2:
            liste = list(map(int, input("Listeyi boşluklarla ayırarak giriniz: ").split()))
            sonuc = tekrar_eden_elemanlar(liste)
            print(f"Tekrar eden elemanlar: {sonuc}")
        elif secilen_soru == 3:
            a = eval(input("İlk matrisi giriniz: "))
            b = eval(input("İkinci matrisi giriniz: "))
            sonuc = matris_carpimi(a, b)
            print(f"Matris çarpımı: {sonuc}")
        elif secilen_soru == 4:
            # Kullanıcıdan aldığımız dosya yolunda eğer varsa tırnak işaretlerini kaldırır yoksa bir işlem yapmaz
            denetlenmemis_dosya_yolu = input("Text dosyasının dosya yolunu giriniz: ")

            def duzeltilen_dosya_yolu(denetlenmemis_dosya_yolu):
                if denetlenmemis_dosya_yolu.startswith('"') and denetlenmemis_dosya_yolu.endswith('"'):
                    return denetlenmemis_dosya_yolu[1:-1]
                else:
                    return denetlenmemis_dosya_yolu

            dosya_yolu = duzeltilen_dosya_yolu(denetlenmemis_dosya_yolu)
            sonuc = kelime_frekansi(dosya_yolu)
            print(f"Kelimelerin frekansı: {sonuc}")
        elif secilen_soru == 5:
            liste = list(map(int, input("Listeyi boşluklarla ayırarak giriniz: ").split()))
            sonuc = en_kucuk_deger(liste)
            print(f"En küçük değer: {sonuc}")
        elif secilen_soru == 6:
            n = float(input("Karekökü alınacak sayıyı giriniz: "))
            sonuc = karekok(n)
            print(f"Karekök: {sonuc}")
        elif secilen_soru == 7:
            a = int(input("Birinci sayıyı giriniz: "))
            b = int(input("İkinci sayıyı giriniz: "))
            sonuc = eb_ortak_bolen(a, b)
            print(f"En büyük ortak bölen: {sonuc}")
        elif secilen_soru == 8:
            n = int(input("Sayıyı giriniz: "))
            sonuc = asal_veya_degil(n)
            print(f"Asal sayı mı: {sonuc}")
        elif secilen_soru == 9:
            n = int(input("Fibonacci sayısının sırasını giriniz: "))
            sonuc = fibonacci(n)
            print(f"{n}. Fibonacci sayısı: {sonuc}")

        input("\nDevam etmek için Enter tuşuna basın...")  # Enter ile ana ekrana dönüş


if __name__ == "__main__":
    ana_menu()
