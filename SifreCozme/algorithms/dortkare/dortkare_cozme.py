import sys

TURKISH_ALPHABET = [
    'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H',
    'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z'
]
FILLERS = ['X', 'W', 'Q']  # Dolgu karakterleri

def create_standard_matrix(columns):
    chars = TURKISH_ALPHABET.copy()
    total_cells = columns * ((len(chars) + columns - 1) // columns)
    chars += FILLERS * ((total_cells - len(chars)) // len(FILLERS) + 1)
    chars = chars[:total_cells]
    matrix = [chars[i * columns : (i + 1) * columns] for i in range(len(chars) // columns)]
    return matrix

def create_reversed_matrix(columns):
    reversed_chars = TURKISH_ALPHABET[::-1].copy()
    total_cells = columns * ((len(reversed_chars) + columns - 1) // columns)
    reversed_chars += FILLERS * ((total_cells - len(reversed_chars)) // len(FILLERS) + 1)
    reversed_chars = reversed_chars[:total_cells]
    matrix = [reversed_chars[i * columns : (i + 1) * columns] for i in range(len(reversed_chars) // columns)]
    return matrix

def create_shifted_matrix(columns):
    shifted_chars = TURKISH_ALPHABET[5:] + TURKISH_ALPHABET[:5]  # 5 karakter kaydırma
    total_cells = columns * ((len(shifted_chars) + columns - 1) // columns)
    shifted_chars += FILLERS * ((total_cells - len(shifted_chars)) // len(FILLERS) + 1)
    shifted_chars = shifted_chars[:total_cells]
    matrix = [shifted_chars[i * columns : (i + 1) * columns] for i in range(len(shifted_chars) // columns)]
    return matrix

def get_position(char, matrix):
    """
    Standart arama: Verilen matriste, aranan harfin (satır, sütun) konumunu döndürür.
    """
    for row_idx, row in enumerate(matrix):
        if char in row:
            return (row_idx, row.index(char))
    raise ValueError(f"'{char}' matriste bulunamadı!")

def get_position_decrypt(char, matrix):
    """
    Deşifre işlemi için özel arama.
    Eğer aranan karakter 'İ' ise ve ilgili satırda 'I' varsa,
    o satırdaki 'I'nin koordinatlarını döndürür.
    Böylece, şifrelemede zorla 'I' -> 'İ' dönüşümü yapılmışsa,
    deşifre sırasında orijinal koordinatlar elde edilir.
    """
    for row_idx, row in enumerate(matrix):
        if char == "İ":
            # Eğer satırda 'I' varsa, onu döndür (zorla dönüştürülmüş 'İ' aslında 'I'dir)
            if "I" in row:
                return (row_idx, row.index("I"))
            elif "İ" in row:
                return (row_idx, row.index("İ"))
        else:
            if char in row:
                return (row_idx, row.index(char))
    raise ValueError(f"'{char}' matriste bulunamadı!")

def decrypt(ciphertext, columns):
    try:
        # Hata kontrolleri
        if not ciphertext.isalpha():
            raise ValueError("Metin sadece harfler içermeli!")
        if columns <= 0:
            raise ValueError("Sütun sayısı pozitif olmalı!")

        # Matrisleri oluştur
        matrix1 = create_standard_matrix(columns)   # Sol üst (standart)
        matrix2 = create_reversed_matrix(columns)     # Sağ üst (ters alfabe)
        matrix3 = create_shifted_matrix(columns)      # Sol alt (kaydırılmış)
        matrix4 = create_standard_matrix(columns)     # Sağ alt (standart)

        # Metni çöz
        plaintext = []
        for i in range(0, len(ciphertext), 2):
            c1, c2 = ciphertext[i], ciphertext[i+1]

            # 2. ve 3. matristen koordinatları alırken, get_position_decrypt() kullanıyoruz
            row2, col2 = get_position_decrypt(c1, matrix2)
            row3, col3 = get_position_decrypt(c2, matrix3)

            # 1. ve 4. matristen karakter al (formül: P1 = M1[row2][col3], P2 = M4[row3][col2])
            plain_char1 = matrix1[row2][col3]
            if plain_char1 == "I":
                plain_char1 = "İ"
            plaintext.append(plain_char1)
            
            plain_char2 = matrix4[row3][col2]
            if plain_char2 == "I":
                plain_char2 = "İ"
            plaintext.append(plain_char2)

        # Dolguları sil
        plaintext = ''.join(plaintext).rstrip(''.join(FILLERS))
        print("Çözülmüş metin:", plaintext)
        return plaintext

    except Exception as e:
        print("Hata:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    # Kullanıcı girdilerini al
    ciphertext = input("Şifrelenmiş metin: ").upper().replace(" ", "")
    columns = int(input("Sütun sayısı: "))
    decrypt(ciphertext, columns)
