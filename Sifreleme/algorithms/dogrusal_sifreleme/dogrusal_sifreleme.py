# Türk alfabesi (29 harf) tanımı:
ALFABE = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def turkish_upper(text):
    """
    Türkçe karakterleri doğru şekilde büyük harfe çevirir.
    Örneğin 'i' harfini 'İ' yapar.
    """
    mapping = {'i': 'İ', 'ı': 'I', 'ş': 'Ş', 'ğ': 'Ğ', 'ü': 'Ü', 'ö': 'Ö', 'ç': 'Ç'}
    result = ""
    for c in text:
        result += mapping.get(c, c.upper())
    return result

def is_coprime_with_29(a):
    from math import gcd
    return gcd(a, 29) == 1

def get_valid_input(prompt, check_coprime=False):
    while True:
        try:
            value = int(input(prompt))
            if check_coprime:
                original_value = value
                value = value % 29
                if not is_coprime_with_29(value):
                    print(f"Hata: {original_value} değeri 29 ile aralarında asal olmalı. Tekrar deneyin.")
                    continue
            return value
        except ValueError:
            print("Hata: Lütfen bir sayı girin!")

def get_valid_text(prompt):
    while True:
        text = input(prompt).replace(" ", "")
        text_upper = turkish_upper(text)
        if len(text_upper) == 0:
            print("Hata: Metin boş olamaz.")
            continue
        if not all(char in ALFABE for char in text_upper):
            print("Hata: Metin yalnızca Türk alfabesindeki harfleri içermeli.")
            continue
        return text_upper

def encrypt(plaintext, a, b):
    encrypted = []
    plaintext = turkish_upper(plaintext)  # Gelen metni önce büyük harfe çevir
    for char in plaintext:
        if char not in ALFABE:
            print(f"Hata: '{char}' harfi Türk alfabesinde yok. Atlaniyor...")
            continue  # Gerekirse bu satır kaldırılabilir
        x = ALFABE.index(char)
        y = (a * x + b) % len(ALFABE)
        encrypted_char = ALFABE[y]
        encrypted.append(encrypted_char)

    print(f"Şifrelenmiş metin: {''.join(encrypted)}")
    return ''.join(encrypted)


if __name__ == "__main__":
    print("Doğrusal Şifreleme (ax+b) - Türk Alfabesi")
    a = get_valid_input("a (29 ile aralarında asal): ", check_coprime=True)
    b = get_valid_input("b: ") % 29
    plaintext = get_valid_text("Şifrelenecek metin (sadece Türk alfabesi harfleri): ")
    ciphertext = encrypt(plaintext, a, b)
