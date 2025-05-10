TURKISH_ALPHABET = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 
                    'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
                    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']

def turkish_upper(text):
    mapping = {'i': 'İ', 'ı': 'I'}
    return ''.join(mapping.get(c, c.upper()) for c in text)

def char_to_num(char):
    if char not in TURKISH_ALPHABET:
        raise ValueError(f"Geçersiz karakter: '{char}'")
    return TURKISH_ALPHABET.index(char)

def num_to_char(num):
    return TURKISH_ALPHABET[num % 29]

def validate_ciphertext(ciphertext):
    ciphertext = turkish_upper(ciphertext.replace(" ", ""))
    for char in ciphertext:
        if char not in TURKISH_ALPHABET:
            raise ValueError(f"Geçersiz karakter: '{char}'")
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    try:
        ciphertext = validate_ciphertext(ciphertext)
        key = validate_ciphertext(key)
        if not key:
            raise ValueError("Anahtar boş olamaz!")
        key_nums = [char_to_num(c) for c in key]
        plaintext = []
        for i, char in enumerate(ciphertext):
            key_index = i % len(key_nums)
            decrypted_num = (char_to_num(char) - key_nums[key_index]) % 29
            plaintext.append(num_to_char(decrypted_num))
        return ''.join(plaintext)
    except ValueError as e:
        print(f"Hata: {str(e)}")
        return None

if __name__ == "__main__":
    ciphertext = input("Şifrelenmiş metin: ").strip()
    key = input("Anahtar kelime: ").strip()
    
    decrypted = vigenere_decrypt(ciphertext, key)
    if decrypted:
        print(f"Çözülmüş metin: {decrypted}")