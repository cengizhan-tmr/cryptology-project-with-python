def dogrusal_cozme(ciphertext, a, b):
    """
    Linear encryption decryption function that works with the GUI.
    
    Args:
        ciphertext (str): The encrypted text to decrypt
        a (int): The 'a' key (must be coprime with 29)
        b (int): The 'b' key (any integer)
    
    Returns:
        str: The decrypted plaintext
    """
    a = a % 29
    if not is_coprime_with_29(a):
        return "Hata: 'a' değeri (29) ile aralarında asal olmalı!"
    
    a_inv = pow(a, -1, 29)
    
    turkish_alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    char_to_num = {char: idx for idx, char in enumerate(turkish_alphabet)}
    num_to_char = {idx: char for idx, char in enumerate(turkish_alphabet)}
    
    decrypted = []
    for char in ciphertext.upper():
        if char in char_to_num:
            y = char_to_num[char]
            x = (a_inv * (y - b)) % 29
            decrypted_char = num_to_char[x]
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

def is_coprime_with_29(a):
    from math import gcd
    return gcd(a, 29) == 1


if __name__ == "__main__":
    print("Doğrusal Şifreleme Çözücü")
    ciphertext = input("Şifrelenmiş metni girin: ").strip().upper()
    a = int(input("a anahtarını girin: "))
    b = int(input("b anahtarını girin: "))
    
    try:
        plaintext = dogrusal_cozme(ciphertext, a, b)
        print(f"Çözülmüş metin: {plaintext}")
    except Exception as e:
        print(f"Hata: {str(e)}")