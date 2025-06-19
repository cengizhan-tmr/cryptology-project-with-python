def encrypt_text(text, key):
    # Önce metindeki tüm boşlukları kaldır
    text = text.replace(" ", "").lower()
    
    # Türkçe alfabeyi tanımla (küçük harfler)
    turkish_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    encrypted = ""

    # Her harfi kaydırarak şifrele
    for char in text:
        if char in turkish_alphabet:
            # Karakterin indeksini al ve kaydır
            old_index = turkish_alphabet.index(char)
            new_index = (old_index + key) % len(turkish_alphabet)
            encrypted += turkish_alphabet[new_index]
        # Alfabe dışı karakterleri atla (eski kodda buraya geldiğinde karakter olduğu gibi ekleniyordu)
    
    print(f"Şifrelenmiş metin: {encrypted.upper()}")
    return encrypted.upper()

if __name__ == "__main__":
    # Metni al ve küçük harfe çevir
    text = input("Şifrelenecek metin: ")
    # Boşluk kontrolü kaldırıldı, çünkü artık boşlukları fonksiyon içinde kaldırıyoruz
    
    if not text.replace(" ", "").isalpha():
        print("Hata: Metin sadece harfler içermeli!")
        exit(1)

    # Anahtar kontrolü
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

    encrypt_text(text, key)