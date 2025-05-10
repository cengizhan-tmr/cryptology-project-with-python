def turkish_upper(text):
    """Türkçe karakterler için doğru büyük harf dönüşümü yapar."""
    mapping = {'i': 'İ', 'ş': 'Ş', 'ğ': 'Ğ', 'ü': 'Ü', 'ö': 'Ö', 'ç': 'Ç', 'ı': 'I'}
    result = ""
    for ch in text:
        # Eğer özel dönüşüm tanımlıysa onu, yoksa standart upper dönüşümü uygula
        result += mapping.get(ch, ch.upper())
    return result

def zigzag_encrypt(text, rows):
    text=turkish_upper(text)
    # Tek satır ise direkt dön
    if rows == 1:
        print(f"Şifrelenmiş metin: {text}")
        return text

    # Zigzag matris oluştur
    zigzag = [[] for _ in range(rows)]
    row, step = 0, 1
    for char in text:
        zigzag[row].append(char)
        if row == 0:
            step = 1
        elif row == rows - 1:
            step = -1
        row += step

    # Satırları birleştir
    encrypted = ''.join(''.join(r) for r in zigzag)
    print(f"Şifrelenmiş metin: {encrypted}")
    return ''.join(encrypted)
if __name__ == "__main__":
    # Metni al ve temizle
    raw_text = input("Şifrelenecek metin: ").replace(" ", "")
    # Hata kontrolü: sadece harf içermeli
    if not raw_text.isalpha():
        print("Hata: Metin sadece harfler içermeli!")
        exit(1)
    
    # Türkçe'ye uygun büyük harf dönüşümü yap
    text = turkish_upper(raw_text)

    # Satır sayısı kontrolü
    while True:
        try:
            rows = int(input("Satır sayısı (pozitif tam sayı): "))
            if rows <= 0:
                print("Hata: Satır sayısı pozitif olmalı!")
                continue
            break
        except ValueError:
            print("Hata: Geçersiz sayı!")
    
    zigzag_encrypt(text, rows)
