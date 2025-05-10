import sys

TURKISH_ALPHABET = [
    'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H',
    'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z'
]
FILLERS = ['X', 'W', 'Q']  # Dolgu karakterleri

def fix_input_text(text):
    """
    Girilen metindeki harfleri Türkçe büyük harf kurallarına göre dönüştürür.
    Küçük 'i' -> 'İ', küçük 'ı' -> 'I' yapılır,
    diğer harfler ise standart .upper() uygulanır.
    """
    fixed = ""
    for ch in text:
        if ch == "i":
            fixed += "İ"
        elif ch == "ı":
            fixed += "I"
        else:
            fixed += ch.upper()
    return fixed

def create_standard_matrix(columns):
    """Standart alfabe matrisi oluşturur (1. ve 4. matris)."""
    chars = TURKISH_ALPHABET.copy()
    total_cells = columns * ((len(chars) + columns - 1) // columns)
    chars += FILLERS * ((total_cells - len(chars)) // len(FILLERS) + 1)
    chars = chars[:total_cells]
    matrix = [chars[i * columns : (i + 1) * columns] for i in range(len(chars) // columns)]
    return matrix

def create_reversed_matrix(columns):
    """Alfabenin tersiyle matris oluşturur (2. matris)."""
    reversed_chars = TURKISH_ALPHABET[::-1].copy()
    total_cells = columns * ((len(reversed_chars) + columns - 1) // columns)
    reversed_chars += FILLERS * ((total_cells - len(reversed_chars)) // len(FILLERS) + 1)
    reversed_chars = reversed_chars[:total_cells]
    matrix = [reversed_chars[i * columns : (i + 1) * columns] for i in range(len(reversed_chars) // columns)]
    return matrix

def create_shifted_matrix(columns):
    """Alfabeyi kaydırarak matris oluşturur (3. matris)."""
    shifted_chars = TURKISH_ALPHABET[5:] + TURKISH_ALPHABET[:5]  # 5 karakter kaydırma
    total_cells = columns * ((len(shifted_chars) + columns - 1) // columns)
    shifted_chars += FILLERS * ((total_cells - len(shifted_chars)) // len(FILLERS) + 1)
    shifted_chars = shifted_chars[:total_cells]
    matrix = [shifted_chars[i * columns : (i + 1) * columns] for i in range(len(shifted_chars) // columns)]
    return matrix

def get_position(matrix, char):
    """Karakterin matristeki konumunu (satır, sütun) döndürür."""
    for row_idx, row in enumerate(matrix):
        if char in row:
            return (row_idx, row.index(char))
    raise ValueError(f"'{char}' matriste bulunamadı!")

def encrypt(plaintext, columns):
    try:
        # Hata kontrolleri
        if not plaintext.isalpha():
            raise ValueError("Metin sadece harfler içermeli!")
        if columns <= 0:
            raise ValueError("Sütun sayısı pozitif olmalı!")

        # Matrisleri oluştur
        matrix1 = create_standard_matrix(columns)   # Sol üst (standart)
        matrix2 = create_reversed_matrix(columns)     # Sağ üst (ters alfabe)
        matrix3 = create_shifted_matrix(columns)      # Sol alt (kaydırılmış)
        matrix4 = create_standard_matrix(columns)     # Sağ alt (standart)

        # Metni çiftlere ayır ve şifrele
        if len(plaintext) % 2 != 0:
            plaintext += FILLERS[0]
        ciphertext = []
        for i in range(0, len(plaintext), 2):
            char1, char2 = plaintext[i], plaintext[i + 1]

            # 1. ve 4. matriste konum bul
            row1, col1 = get_position(matrix1, char1)
            row4, col4 = get_position(matrix4, char2)

            # 2. ve 3. matristen karakter al ve 'I' yerine zorla 'İ' kullan
            letter1 = matrix2[row1][col4]
            letter2 = matrix3[row4][col1]
            if letter1 == "I":
                letter1 = "İ"
            if letter2 == "I":
                letter2 = "İ"
            ciphertext.append(letter1)
            ciphertext.append(letter2)

        result = "".join(ciphertext)
        print("Şifrelenmiş metin:", result)
        return result

    except Exception as e:
        print("Hata:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    # Kullanıcı girdilerini al ve boşlukları kaldır.
    raw_text = input("Şifrelenecek metin: ").replace(" ", "")
    # Türkçe büyük harf dönüşümü için özel düzeltme uygulanıyor.
    plaintext = fix_input_text(raw_text)
    columns = int(input("Sütun sayısı: "))

    encrypt(plaintext, columns)
