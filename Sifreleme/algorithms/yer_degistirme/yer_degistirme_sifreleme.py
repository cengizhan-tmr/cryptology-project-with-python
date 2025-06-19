import json
import os
import random

TURKISH_ALPHABET = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def turkish_upper(text):
    mapping = {'i': 'İ', 'ı': 'I', 'ş': 'Ş', 'ğ': 'Ğ', 'ü': 'Ü', 'ö': 'Ö', 'ç': 'Ç'}
    return ''.join(mapping.get(c, c.upper()) for c in text)

def encrypt(text, key):
    return ''.join([key.get(char, char) for char in text.upper()])

def is_valid_key(key):
    expected = set(TURKISH_ALPHABET)
    return (
        isinstance(key, dict) and
        set(key.keys()) == expected and
        set(key.values()) == expected
    )

def load_key():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(base_dir, "key.json")

    try:
        with open(key_path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        if not is_valid_key(key):
            raise ValueError("Geçersiz key formatı")
        return key
    except Exception as e:
        raise RuntimeError(f"Anahtar dosyası yüklenemedi: {e}")


if __name__ == "__main__":
    key = load_key()
    text = input("Şifrelenecek metin: ")
    clean_text = turkish_upper(text.replace(" ", ""))
    if not clean_text.isalpha():
        print("Metin yalnızca harflerden oluşmalı!")
    else:
        print("Şifrelenmiş metin:", encrypt(clean_text, key))
