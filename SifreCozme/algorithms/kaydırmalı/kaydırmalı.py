alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def caesar_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    decrypted = []
    for ch in ciphertext:
        if ch in alphabet:
            idx = (alphabet.index(ch) - key) % len(alphabet)
            decrypted.append(alphabet[idx])
        else:
            decrypted.append(ch)
    result = ''.join(decrypted)
    print("Çözülmüş metin:", result)
    return result

if __name__ == "__main__":
   

    metin = input("İşlem yapılacak metni girin: ")
    
    while True:
        key_str = input("Anahtar (0-28 arası tam sayı): ")
        if not key_str.isdigit():
            print("Hata: Anahtar bir sayı olmalı!")
            continue
        key = int(key_str)
        if not (0 <= key < len(alphabet)):
            print(f"Hata: Anahtar 0 ile {len(alphabet)-1} arasında olmalı!")
            continue
        break
    
    caesar_decrypt(metin, key)
