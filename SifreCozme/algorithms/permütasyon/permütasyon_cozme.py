def decrypt(ciphertext, m, key):
    # Ters anahtar
    inverse_key = [0] * m
    for idx, pos in enumerate(key):
        inverse_key[pos-1] = idx + 1

    # Parçaları çöz
    part_length = m
    parts = [ciphertext[i*part_length : (i+1)*part_length] for i in range(len(ciphertext) // m)]
    
    decrypted = []
    for part in parts:
        original_part = ''.join([part[inverse_key[i]-1] for i in range(m)])
        decrypted.append(original_part)
    
    # X'leri SİLME (orijinal metni olduğu gibi birleştir)
    plaintext = ''.join(decrypted)
    print(f"Çözülmüş metin: {plaintext}")
    return plaintext

if __name__ == "__main__":

    ciphertext = input("Şifrelenmiş metin: ").replace(" ", "").upper()
    if not ciphertext.isalpha():
        print("Hata: Metin sadece harfler içermeli!")

    # Parça uzunluğu (m) al
    while True:
        m = input("Parça uzunluğu (m): ")
        if not m.isdigit() or int(m) <= 0:
            print("Hata: m pozitif tam sayı olmalı!")
        else:
            m = int(m)
            break

    # Anahtar kontrolü
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
    decrypt(ciphertext, m, key)