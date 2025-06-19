def turkish_upper(text):
    """
    Türkçe'ye uygun büyük harf dönüşümü yapar.
    Örneğin: 'i' -> 'İ', 'ı' -> 'I', 'ç' -> 'Ç', 'ğ' -> 'Ğ', 'ö' -> 'Ö', 'ü' -> 'Ü', 'ş' -> 'Ş'
    """
    mapping = {
        'i': 'İ',
        'ı': 'I',
        'ç': 'Ç',
        'ğ': 'Ğ',
        'ö': 'Ö',
        'ş': 'Ş'
    }
    result = ""
    for char in text:
        # Eğer karakter mapping'te varsa, onun karşılığını al; yoksa varsayılan upper() kullan.
        if char in mapping:
            result += mapping[char]
        else:
            result += char.upper()
    return result

def encrypt_spiral(text, key):
    # Matrisi oluştur (sütun sayısı = anahtar)
    rows = (len(text) + key - 1) // key  # satır sayısını yuvarlama ile belirle
    matrix = []
    index = 0
    for _ in range(rows):
        row = []
        for _ in range(key):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')  # Eksik kalan yerler için dolgu karakteri (büyük harf)
        matrix.append(row)
    
    # Matrisi spiral olarak oku
    result = []
    top, bottom, left, right = 0, rows - 1, 0, key - 1
    while top <= bottom and left <= right:
        # Sol sütunu aşağıdan yukarı oku
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
        if left > right:
            break
        # Üst satırı soldan sağa oku
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        # Sağ sütunu yukarıdan aşağı oku
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # Alt satırı sağdan sola oku
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
    
    encrypted_text = ''.join(result)
    print(f"Şifrelenmiş metin: {encrypted_text}")
    return encrypted_text

if __name__ == "__main__":
    # Kullanıcıdan metni al, boşlukları kaldır
    raw_text = input("Şifrelenecek metin: ").replace(" ", "")
    # Türkçe'ye uygun şekilde büyük harfe çevir
    text = turkish_upper(raw_text)
    
    if not text.isalpha():
        print("Hata: Metin sadece harf içermeli!")
        exit()
    
    # Anahtar kontrolü: pozitif tam sayı olması gerekiyor.
    while True:
        key = input("Anahtar (pozitif tam sayı): ")
        if not key.isdigit():
            print("Hata: Anahtar bir sayı olmalı!")
            continue
        key = int(key)
        if key <= 0:
            print("Hata: Anahtar pozitif olmalı!")
            continue
        break
    
    encrypt_spiral(text, key)
