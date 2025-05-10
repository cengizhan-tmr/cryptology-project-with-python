TURKISH_ALPHABET = [
    'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H',
    'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z'
]

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

def char_to_num(char):
    """Harfi sayıya çevirir (0-28 arası)."""
    # Türkçe'ye uygun büyük harfe çeviriyoruz.
    char = turkish_upper(char)
    if char not in TURKISH_ALPHABET:
        raise ValueError(f"Geçersiz karakter: '{char}'")
    return TURKISH_ALPHABET.index(char)

def num_to_char(num):
    """Sayıyı harfe çevirir."""
    char = TURKISH_ALPHABET[num % 29]
    return char

def validate_text(text):
    """Metni kontrol eder (sadece harf ve boşluk)."""
    # Turkish_upper ile metni, boşlukları kaldırarak dönüştürüyoruz.
    text = turkish_upper(text).replace(" ", "")
    for char in text:
        if char not in TURKISH_ALPHABET:
            raise ValueError(f"Geçersiz karakter: '{char}'")
    return text

def vigenere_encrypt(plaintext, key):
    try:
        plaintext = validate_text(plaintext)
        key = validate_text(key)
        
        if not key:
            raise ValueError("Anahtar boş olamaz!")
        
        key_nums = [char_to_num(c) for c in key]
        ciphertext = []
        
        for i, char in enumerate(plaintext):
            key_index = i % len(key_nums)
            encrypted_num = (char_to_num(char) + key_nums[key_index]) % 29
            ciphertext.append(num_to_char(encrypted_num))
        
        return ''.join(ciphertext)
    
    except ValueError as e:
        print(f"Hata: {str(e)}")
        return None

if __name__ == "__main__":
    plaintext = input("Şifrelenecek metin: ").strip()
    key = input("Anahtar kelime: ").strip()
    
    encrypted = vigenere_encrypt(plaintext, key)
    if encrypted:
        print(f"Şifrelenmiş metin: {encrypted}")
