def decrypt_spiral(ciphertext, key):
   
    # Matris boyutunu hesapla
    total_chars = len(ciphertext)
    rows = (total_chars + key - 1) // key
    matrix = [[None for _ in range(key)] for _ in range(rows)]
    
    # Spiral yaz
    top, bottom, left, right = 0, rows-1, 0, key-1
    index = 0
    while top <= bottom and left <= right and index < total_chars:
        # Sol sütunu aşağıdan yukarı
        for i in range(bottom, top-1, -1):
            if index >= total_chars:
                break
            matrix[i][left] = ciphertext[index]
            index += 1
        left += 1
        if left > right or index >= total_chars:
            break
        # Üst satırı soldan sağa
        for j in range(left, right+1):
            if index >= total_chars:
                break
            matrix[top][j] = ciphertext[index]
            index += 1
        top += 1
        # Sağ sütunu yukarıdan aşağı
        for i in range(top, bottom+1):
            if index >= total_chars:
                break
            matrix[i][right] = ciphertext[index]
            index += 1
        right -= 1
        # Alt satırı sağdan sola
        if top <= bottom:
            for j in range(right, left-1, -1):
                if index >= total_chars:
                    break
                matrix[bottom][j] = ciphertext[index]
                index += 1
            bottom -= 1
    
    # Matrisi satır satır oku
    decrypted = []
    for row in matrix:
        decrypted.extend(row)
    decrypted_text = ''.join(decrypted).rstrip('x')
    print(f"Çözülmüş metin: {decrypted_text}")
    return decrypted_text

if __name__ == "__main__":

     # Kullanıcıdan şifreli metin ve anahtar al
    ciphertext = input("Şifrelenmiş metin: ").lower().replace(" ", "")
    if not ciphertext.isalpha():
        print("Hata: Metin sadece harf içermeli!")
        
    
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
    decrypt_spiral(ciphertext, key)