def encrypt_text(text, key):
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
        else:
            # Eğer karakter alfabe içinde yoksa değiştirilmeden ekle
            encrypted += char
    print(f"Şifrelenmiş metin: {encrypted.upper()}")
    return ''.join(encrypted.upper())

if __name__ == "__main__":
    # Metni al, boşlukları kaldır ve küçük harfe çevir
    text = input("Şifrelenecek metin: ").replace(" ", "").lower()
    if not text.isalpha():
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
