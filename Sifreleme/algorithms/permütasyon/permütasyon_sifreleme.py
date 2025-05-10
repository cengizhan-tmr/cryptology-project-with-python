def turkish_upper(text):
    """
    Türkçe karakter dönüşümü yaparak metni büyük harfe çevirir.
    'i' yerine 'İ' ve diğer bazı harfleri uygun şekilde çevirir.
    """
    mapping = {'i': 'İ', 'ş': 'Ş', 'ğ': 'Ğ', 'ü': 'Ü', 'ö': 'Ö', 'ç': 'Ç'}
    result = ""
    for c in text:
        # Eğer karakter mapping'te varsa özel dönüşümü uygula, yoksa standart upper() kullan.
        if c in mapping:
            result += mapping[c]
        else:
            result += c.upper()
    return result

def encrypt(text, m, key):
    text = turkish_upper(text)
    # Metni, m uzunluğunda parçalara bölüyoruz; metnin sonu eksikse 'X' ile dolduruyoruz.
    text_len = len(text)
    padded_len = m * ((text_len + m - 1) // m)
    padded_text = text.ljust(padded_len, 'X')
    parts = [padded_text[i*m : (i+1)*m] for i in range(padded_len // m)]
    
    # Parçaları verilen anahtar sırasına göre permüte edip birleştir.
    encrypted = []
    for part in parts:
        encrypted_part = ''.join([part[i-1] for i in key])
        encrypted.append(encrypted_part)
    
    print(f"Şifrelenmiş metin: {''.join(encrypted)}")
    return ''.join(encrypted)

if __name__ == "__main__":
    # Kullanıcıdan metni al, boşluklar kaldırılır ve turkish_upper() fonksiyonu ile Türkçe karakter duyarlı büyük harfe çevrilir.
    text = input("Şifrelenecek metin: ").replace(" ", "")
    
    
    if not text.isalpha():
        print("Hata: Metin sadece harfler içermeli!")
        exit()
    
    # Parça uzunluğu (m) al
    while True:
        m = input("Parça uzunluğu (m): ")
        if not m.isdigit() or int(m) <= 0:
            print("Hata: m pozitif tam sayı olmalı!")
        else:
            m = int(m)
            break

    # Anahtar doğrulaması: m adet sayı içermeli, 1'den m'e kadar tüm sayılar bulunmalı.
    while True:
        key_input = input(f"{m} adet permütasyon anahtarı girin (örnek: 2 4 1 3): ").split()
        if len(key_input) != m or not all(k.isdigit() for k in key_input):
            print(f"Hata: Anahtar {m} adet sayı içermeli!")
        else:
            key = list(map(int, key_input))
            if sorted(key) != list(range(1, m+1)):
                print(f"Hata: Anahtar 1'den {m}'e kadar tüm sayıları içermeli!")
            else:
                break

    encrypt(text, m, key)
