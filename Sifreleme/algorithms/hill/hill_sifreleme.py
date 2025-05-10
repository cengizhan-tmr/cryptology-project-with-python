# hill_encryption_advanced.py
# Geliştirilmiş Hill Şifreleme Algoritması (nxn matrisler için)
import numpy as np
from sympy import Matrix, mod_inverse

def gcd(a, b):
    """En büyük ortak böleni hesaplar."""
    while b:
        a, b = b, a % b
    return abs(a)

def determinant_mod(matris, mod):
    """Matrisin mod içindeki determinantını hesaplar."""
    matris_sympy = Matrix(matris)
    return int(matris_sympy.det()) % mod

def matris_tersi_kontrol(matris, mod):
    """
    Matrisin mod içinde tersinin olup olmadığını kontrol eder.
    Eğer ters varsa True, yoksa False döner.
    """
    det = determinant_mod(matris, mod)
    return det != 0 and gcd(det, mod) == 1

def hill_sifreleme(n, anahtar_matrisi, metin):
    """Hill şifreleme algoritması (nxn matrisler için)."""
    # Türkçe alfabe (29 karakter)
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    alfabe_sozluk = {harf: ind for ind, harf in enumerate(alfabe)}
        
    try:
        
        # Metindeki Türkçe alfabe dışındaki karakterleri temizle
        temiz_metin = ''.join(harf for harf in metin if harf in alfabe)
        if temiz_metin != metin:
            print("Uyarı: Bazı karakterler Türkçe alfabede olmadığı için kaldırıldı.")
            metin = temiz_metin
        
        if len(metin) == 0:
            print("Hata: Geçerli karakterlerden oluşan bir metin girilmelidir.")
            return None, None
        
        # Metin uzunluğunu anahtar boyutunun katı olacak şekilde dolgu yap
        if len(metin) % n != 0:
            dolgu_sayisi = n - (len(metin) % n)
            metin += "A" * dolgu_sayisi
            print(f"Not: Metin uzunluğunu {n}'nin katı yapmak için {dolgu_sayisi} adet 'A' eklendi.")
        
        print(f"\nİşlenecek metin: {metin}")
        
        # Şifreleme işlemi
        sifreli_metin = ""
        for i in range(0, len(metin), n):
            blok = metin[i:i+n]
            # Bloğu sayısal vektöre dönüştür
            P = np.array([alfabe_sozluk[harf] for harf in blok])
            
            # Şifreleme: C = K * P mod 29
            C = np.dot(anahtar_matrisi, P) % 29
            
            # Sayısal sonuçları harflere dönüştür
            sifreli_blok = ''.join(alfabe[c] for c in C)
            sifreli_metin += sifreli_blok
        
        print("\nŞifreleme sonucu:")
        print(f"Şifreli metin: {sifreli_metin}")
        
        return sifreli_metin
    
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        import traceback
        traceback.print_exc()
        return None, None

if __name__ == "__main__":
    print("Hill Şifreleme Algoritması (Mod 29)")
    print("-----------------------------------")
# Anahtar boyutunu al
    n = int(input("Anahtar matrisin boyutunu giriniz (n): "))
    if n < 2:
        print("Hata: Matris boyutu en az 2 olmalıdır.")
    
    # Anahtar matrisi al
    print(f"\n{n}x{n} anahtar matrisini giriniz (her satır için {n} değer):")
    anahtar_matrisi = []
    for i in range(n):
        satir_str = input(f"Satır {i+1}: ").strip()
        try:
            satir = list(map(int, satir_str.split()))
            if len(satir) != n:
                print(f"Hata: Satır {i+1} tam olarak {n} değer içermelidir.")

            anahtar_matrisi.append(satir)
        except ValueError:
            print("Hata: Sadece sayısal değerler girilmelidir.")


    anahtar_matrisi = np.array(anahtar_matrisi)
    
    # Determinantı hesapla ve kontrol et
    det = determinant_mod(anahtar_matrisi, 29)
    if not matris_tersi_kontrol(anahtar_matrisi, 29):
        print(f"Hata: Anahtar matrisin determinantı mod 29'da tersi olmalıdır!")
        print(f"Determinant mod 29: {det}")
    
    # Şifrelenecek metni al
    metin = input("\nŞifrelenecek metni giriniz: ").upper()

    hill_sifreleme(n, anahtar_matrisi, metin)