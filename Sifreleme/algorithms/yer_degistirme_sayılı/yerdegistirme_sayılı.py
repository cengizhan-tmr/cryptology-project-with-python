def sifrele(metin, key):
    metin=turkish_upper(metin)  # Metni büyük harfe çevir ve boşlukları kaldır
    # Metin uzunluğunu keye bölelim ve satır sayısını hesaplayalım
    satir_sayisi = (len(metin) + key - 1) // key  # Yukarı yuvarlama
    
    # Matris boyutunu hesapla
    toplam_karakter = satir_sayisi * key
    
    # Eksik karakterleri 'X' ile doldur
    dolgu_karakteri = 'X'
    if len(metin) < toplam_karakter:
        metin += dolgu_karakteri * (toplam_karakter - len(metin))
    
    # Metni matrise yerleştir (satır x sütun)
    matris = []
    for i in range(satir_sayisi):
        satir = metin[i*key:(i+1)*key]
        matris.append(satir)
    
    # Matrisi görselleştir
    print("Matris:")
    for satir in matris:
        print(satir)
    
    # Şifrelenmiş metni oluştur (1,1), (2,1), (3,1), (1,2), (2,2), ... şeklinde oku
    sifreli_metin = ""
    for j in range(key):  # Sütunlar
        for i in range(satir_sayisi):  # Satırlar
            if j < len(matris[i]):  # Eğer indeks varsa
                sifreli_metin += matris[i][j]
    print(f"Şifrelenmiş metin: {sifreli_metin}")
    
    return sifreli_metin


def turkish_upper(text):
    """
    Metni Türkçe karakter dönüşüm kurallarına uygun şekilde büyük harfe çevirir.
    Örneğin: 'i' -> 'İ', 'ı' -> 'I', 'ç' -> 'Ç', 'ğ' -> 'Ğ', 'ö' -> 'Ö', 'ü' -> 'Ü', 'ş' -> 'Ş'
    """
    mapping = {
        'i': 'İ',
        'ı': 'I',
        'ç': 'Ç',
        'ğ': 'Ğ',
        'ö': 'Ö',
        'ü': 'Ü',
        'ş': 'Ş'
    }
    result = ""
    for char in text:
        # Eğer karakter küçük harf ve dönüşüm tanımlıysa, dönüştürüyoruz
        if char in mapping:
            result += mapping[char]
        else:
            result += char.upper()
    return result

# Test edelim
if __name__ == "__main__":
    metin = input("Şifrelenecek metni girin: ")
    key = int(input("Anahtar (sütun sayısı) girin: "))
    
    sifreli = sifrele(metin, key)
    print(f"Şifrelenmiş metin: {sifreli}")