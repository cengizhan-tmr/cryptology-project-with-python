def zigzag_decrypt(ciphertext, rows):
    
    if rows == 1:
        print(f"Çözülmüş metin: {ciphertext}")
        return ciphertext

    n = len(ciphertext)
    zigzag = [[''] * n for _ in range(rows)]

    # Harflerin yerleşeceği yerleri işaretle
    current_row, step = 0, 1
    pattern = [[] for _ in range(rows)]
    
    for i in range(n):
        pattern[current_row].append(i)
        if current_row == 0:
            step = 1
        elif current_row == rows - 1:
            step = -1
        current_row += step

    # Metni doğru sırayla matrise doldur
    index = 0
    for r in range(rows):
        for col in pattern[r]:
            zigzag[r][col] = ciphertext[index]
            index += 1

    # Orijinal metni zigzag ile oku
    decrypted = []
    current_row, step = 0, 1
    for i in range(n):
        decrypted.append(zigzag[current_row][i])
        if current_row == 0:
            step = 1
        elif current_row == rows - 1:
            step = -1
        current_row += step

    print(f"Çözülmüş metin: {''.join(decrypted)}")
    return ''.join(decrypted)

if __name__ == "__main__":

    ciphertext = input("Şifrelenmiş metin: ").replace(" ", "").upper()
    if not ciphertext.isalpha():
        print("Hata: Metin sadece harfler içermeli!")
        

    while True:
        try:
            rows = int(input("Satır sayısı (pozitif tam sayı): "))
            if rows <= 0:
                print("Hata: Satır sayısı pozitif olmalı!")
                continue
            break
        except ValueError:
            print("Hata: Geçersiz sayı!")

    zigzag_decrypt(ciphertext, rows)
