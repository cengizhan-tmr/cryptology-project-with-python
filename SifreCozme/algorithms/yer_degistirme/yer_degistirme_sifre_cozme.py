import json
import argparse
import os

def turkish_upper(text):
    """Türkçe karakterleri doğru şekilde büyük harfe çevirir."""
    mapping = {'i': 'İ', 'ı': 'I', 'ş': 'Ş', 'ğ': 'Ğ', 'ü': 'Ü', 'ö': 'Ö', 'ç': 'Ç'}
    return ''.join(mapping.get(c, c.upper()) for c in text)

def get_script_dir():
    """Komut dosyasının dizinini döndürür."""
    return os.path.dirname(os.path.abspath(__file__))

def is_valid_key(key):
    """Anahtarın geçerli olup olmadığını kontrol eder (Türk alfabesi için)."""
    expected = set("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ")
    return (
        isinstance(key, dict) and
        set(key.keys()) == expected and
        set(key.values()) == expected and
        len(key) == len(expected)
    )

def get_valid_text(prompt):
    """Geçerli bir metin girdisi alır."""
    while True:
        text = turkish_upper(input(prompt).replace(" ", ""))
        if not text:
            print("Hata: Metin boş olamaz!")
            continue
        if not text.isalpha():
            print("Hata: Metin sadece harfler içermeli!")
        else:
            return text

def decrypt(text, key):
    """Yer değiştirme şifresini çözer."""
    reverse_key = {v: k for k, v in key.items()}
    return ''.join([reverse_key.get(char, char) for char in text])

def main():
    parser = argparse.ArgumentParser(description="Yer Değiştirme Şifre Çözme")
    parser.add_argument("-k", "--key", default="key.json", help="Anahtar dosyası (varsayılan: key.json)")
    args = parser.parse_args()

    # Dosya yolunu oluştur
    script_dir = get_script_dir()
    key_path = os.path.join(script_dir, args.key) if os.path.dirname(args.key) == "" else args.key

    try:
        with open(key_path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        if not is_valid_key(key):
            print(f"Hata: '{key_path}' geçersiz anahtar formatı!")
            return
    except FileNotFoundError:
        print(f"Hata: '{key_path}' dosyası bulunamadı!")
        return
    except json.JSONDecodeError:
        print(f"Hata: '{key_path}' geçersiz JSON formatı!")
        return

    ciphertext = get_valid_text("Şifrelenmiş metin: ")
    plaintext = decrypt(ciphertext, key)
    print(f"Çözülmüş metin: {plaintext}")

if __name__ == "__main__":
    main()