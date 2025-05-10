import numpy as np
from sympy import Matrix, mod_inverse

def gcd(a, b):
    """En büyük ortak böleni hesaplar."""
    while b:
        a, b = b, a % b
    return abs(a)

def matris_mod_tersi(matris, mod):
    """
    Verilen matrisin mod içindeki tersini hesaplar.
    Herhangi boyuttaki kare matrisler için çalışır.
    """
    matris = np.array(matris)
    n = matris.shape[0]
    
    matris_sympy = Matrix(matris)
    
    # Determinantı hesapla
    det = int(matris_sympy.det()) % mod
    
    # Determinantın mod içindeki tersi olup olmadığını kontrol et
    if det == 0 or gcd(det, mod) != 1:
        raise ValueError(f"Matrisin determinantının mod {mod}'da tersi yoktur! Det = {det}")
    
    # Determinantın mod içindeki tersi
    det_inverse = mod_inverse(det, mod)
    
    # Adjoint matris hesaplaması ve mod işlemi
    adj = matris_sympy.adjugate() % mod
    
    # Tersi = (1/det * adj) mod m
    matris_tersi = (det_inverse * adj) % mod
    
    return np.array(matris_tersi, dtype=int)

def hill_sifre_cozme(n, anahtar_matrisi, sifreli_metin):
    """Hill şifre çözme algoritması (nxn matrisler için)."""
    # Türkçe alfabe (29 karakter, büyük harf, I-İ sorunu: 
    # deşifre sonucunda hem I hem de İ için kesinlikle İ kullanılacak)
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    alfabe_sozluk = {harf: ind for ind, harf in enumerate(alfabe)}
    
    print("Hill Şifre Çözme Algoritması (Mod 29)")
    print("-----------------------------------")
    
    try:
        # Metindeki Türkçe alfabe dışındaki karakterleri temizle
        temiz_metin = ''.join(harf for harf in sifreli_metin if harf.upper() in alfabe)
        if temiz_metin != sifreli_metin:
            print("Uyarı: Bazı karakterler Türkçe alfabede olmadığı için kaldırıldı.")
            sifreli_metin = temiz_metin
        
        if len(sifreli_metin) == 0:
            print("Hata: Geçerli karakterlerden oluşan bir şifreli metin girilmelidir.")
            return None
        
        # Metin uzunluğunu kontrol et
        if len(sifreli_metin) % n != 0:
            print(f"Hata: Şifreli metin uzunluğu ({len(sifreli_metin)}) matris boyutunun ({n}) katı olmalıdır.")
            return None
        
        print(f"\nİşlenecek şifreli metin: {sifreli_metin}")
        
        # Anahtar matrisinin tersini hesapla (mod 29)
        try:
            ters_matrisi = matris_mod_tersi(anahtar_matrisi, 29)
            print("\nAnahtar matrisinin tersi (mod 29) hesaplandı:")
            print(ters_matrisi)
        except ValueError as e:
            print(f"Hata: {e}")
            return None
        
        # Şifre çözme işlemi
        cozulmus_metin = ""
        for i in range(0, len(sifreli_metin), n):
            blok = sifreli_metin[i:i+n]
            C = []
            harf_case = []  # Her harfin orijinal durumunu (küçük mü, büyük mü) kaydeder.
            
            # Bloğu sayısal vektöre dönüştür (karşılaştırma için harfi büyük alıyoruz)
            for harf in blok:
                harf_case.append(harf.islower())
                C.append(alfabe_sozluk[harf.upper()])
            
            C = np.array(C)
            
            # Şifre çözme: P = (Ters Anahtar Matris) * C mod 29
            P = np.dot(ters_matrisi, C) % 29
            
            # Sayısal sonucu harfe çevirirken; I/İ sorununu düzeltmek için:
            # Eğer elde edilen harf "I" veya "İ" ise kesinlikle "İ" olarak alınacaktır.
            cozulmus_blok = ''
            for p, is_lower in zip(P, harf_case):
                harf = alfabe[p]
                if harf in ["I", "İ"]:
                    harf = "İ"
                if is_lower:
                    harf = harf.lower()
                cozulmus_blok += harf
            cozulmus_metin += cozulmus_blok
        
        print("\nŞifre çözme sonucu:")
        print(f"Çözülmüş metin: {cozulmus_metin}")
        
        return cozulmus_metin
    
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # Anahtar boyutunu al
    n = int(input("Anahtar matrisin boyutunu giriniz (n): "))
    if n < 2:
        print("Hata: Matris boyutu en az 2 olmalıdır.")
        exit()
    
    # Anahtar matrisi al
    print(f"\n{n}x{n} anahtar matrisini giriniz (her satır için {n} değer):")
    anahtar_matrisi = []
    for i in range(n):
        satir_str = input(f"Satır {i+1}: ").strip()
        try:
            satir = list(map(int, satir_str.split()))
            if len(satir) != n:
                print(f"Hata: Satır {i+1} tam olarak {n} değer içermelidir.")
                exit()
            anahtar_matrisi.append(satir)
        except ValueError:
            print("Hata: Sadece sayısal değerler girilmelidir.")
            exit()
    
    anahtar_matrisi = np.array(anahtar_matrisi)
    
    # Çözülecek şifreli metni al (harflerin orijinal durumuna göre korunması sağlanıyor)
    sifreli_metin = input("\nÇözülecek şifreli metni giriniz: ")
    
    hill_sifre_cozme(n, anahtar_matrisi, sifreli_metin)
