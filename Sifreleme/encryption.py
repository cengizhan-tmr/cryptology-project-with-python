# main.py
import json
import os
import tkinter as tk
from tkinter import messagebox

from algorithms.dortkare import dort_kare_sifreleme
from algorithms.Vigenère import Vigenère_sifreleme 
from algorithms.rota import rota_sifreleme
from algorithms.kaydırmalı import kaydirmali_sifreleme
from algorithms.yer_degistirme_sayılı import yerdegistirme_sayılı
from algorithms.yer_degistirme import yer_degistirme_sifreleme
from algorithms.permütasyon import permütasyon_sifreleme
from algorithms.dogrusal_sifreleme import dogrusal_sifreleme
from algorithms.hill import hill_sifreleme
from algorithms.zigzag import zigzag_sifreleme
from email_service import send_email

def open_cipher_screen(root, algorithm):
    cipher_window = tk.Toplevel(root)
    cipher_window.title(f"{algorithm} Algoritması")
    cipher_window.geometry("500x450")
    cipher_window.configure(bg="white")

    tk.Label(cipher_window, text=f"{algorithm} ALGORİTMASI", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    # Şifrelenmiş mesaj girişi
    tk.Label(cipher_window, text="Şifrelenmiş Mesajı Giriniz:", font=("Arial", 12), bg="white").pack()
    message_entry = tk.Entry(cipher_window, width=40, font=("Arial", 12), bg="#D6EAF8")
    message_entry.pack(pady=5)

    # Farklı algoritmalara göre ek girişler için frame
    input_frame = tk.Frame(cipher_window, bg="white")
    input_frame.pack(pady=10)

    # Sonuç alanı
    result_text = tk.Text(cipher_window, height=5, width=40, font=("Arial", 12), bg="#D6EAF8", wrap=tk.WORD)
    result_text.pack(pady=10)

    # Algoritmalara göre özel input alanları ve fonksiyonlar
    if algorithm == "ZİGZAG":
        tk.Label(input_frame, text="Satır Sayısı:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        rows_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        rows_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def process():
            try:
                ciphertext = message_entry.get().strip().replace(" ", "")
                rows = int(rows_entry.get())
                
                if rows <= 0:
                    raise ValueError("Satır sayısı pozitif tam sayı olmalı!")
                
                decrypted_text = zigzag_sifreleme.zigzag_encrypt(ciphertext, rows)
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{decrypted_text}")
                
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")

    if algorithm == "HILL":
        tk.Label(input_frame, text="Matris Boyutu (n):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        n_entry = tk.Entry(input_frame, width=5, font=("Arial", 12), bg="#D6EAF8")
        n_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Matris girişi için alt frame
        matrix_frame = tk.Frame(input_frame, bg="white")
        matrix_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        matrix_entries = []  # Matris giriş kutularını saklayacak liste
        
        def update_matrix_size():
            # Mevcut giriş alanlarını temizle
            for widget in matrix_frame.winfo_children():
                widget.destroy()
            
            matrix_entries.clear()
            
            try:
                n = int(n_entry.get())
                
                
                # n x n matris için giriş alanları oluştur
                tk.Label(matrix_frame, text="Anahtar Matris:", font=("Arial", 12), bg="white").grid(row=0, column=0, columnspan=n, pady=5)
                
                for i in range(n):
                    row_entries = []
                    for j in range(n):
                        entry = tk.Entry(matrix_frame, width=4, font=("Arial", 12), bg="#D6EAF8")
                        entry.grid(row=i+1, column=j, padx=2, pady=2)
                        row_entries.append(entry)
                    matrix_entries.append(row_entries)
            
            except ValueError:
                messagebox.showerror("Hata", "Geçerli bir matris boyutu giriniz.")
        
        # Matris boyutunu güncelleme butonu
        update_button = tk.Button(input_frame, text="Matris Oluştur", font=("Arial", 10),
                                  command=update_matrix_size, bg="#3498DB", fg="white")
        update_button.grid(row=0, column=2, padx=5, pady=5)
        
        def process():
            try:
                # Şifreli metni al
                ciphertext = message_entry.get().strip()
                
                # Matris boyutunu kontrol et
                try:
                    n = int(n_entry.get())
                   
                except ValueError:
                    messagebox.showerror("Hata", "Geçerli bir matris boyutu giriniz.")
                    return
                
                # Anahtar matrisini al
                anahtar_matrisi = []
                for i in range(n):
                    satir = []
                    for j in range(n):
                        try:
                            deger = int(matrix_entries[i][j].get())
                            satir.append(deger)
                        except ValueError:
                            messagebox.showerror("Hata", 
                                f"Matris elemanı ({i+1},{j+1}) geçerli bir sayı değil.")
                            return
                    anahtar_matrisi.append(satir)
                
                # hill_sifre_cozme fonksiyonunu çağır
            
                # Güncellenen fonksiyonu çağır
                decrypted_text = hill_sifreleme.hill_sifreleme(n, anahtar_matrisi, ciphertext)
                
                if decrypted_text:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"{decrypted_text}")
                else:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, "Şifre çözülemedi. Lütfen girişleri kontrol edin.")
                    
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")


    elif algorithm == "YERDEĞİŞTİRME SAYILI":
        tk.Label(input_frame, text="Satır Sayısı:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        key_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        key_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def process():
            try:
                ciphertext = message_entry.get().strip().replace(" ", "")
                key = int(key_entry.get())
                
                if key <= 0:
                    raise ValueError("satır sayısı pozitif tam sayı olmalı!")
                
                decrypted_text = yerdegistirme_sayılı.sifrele(ciphertext, key)
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{decrypted_text}")
                
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")
    
    
    elif algorithm == "DOĞRUSAL ŞİFRELEME":
        tk.Label(input_frame, text="a (Anahtar):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        a_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        a_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="b (Anahtar):", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        b_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        b_entry.grid(row=1, column=1, padx=5, pady=5)
        
        def process():
            try:
                a = int(a_entry.get())
                b = int(b_entry.get())
                ciphertext = message_entry.get().strip()
                
                plaintext = dogrusal_sifreleme.encrypt(ciphertext, a, b)
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{plaintext}")
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")
    
    elif algorithm == "PERMÜTASYON":
        tk.Label(input_frame, text="Parça Uzunluğu (m):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        m_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        m_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Permütasyon Anahtarı:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        key_entry = tk.Entry(input_frame, width=20, font=("Arial", 12), bg="#D6EAF8")
        key_entry.grid(row=1, column=1, padx=5, pady=5)
        
        
        def process():
            try: # Girdileri al ve doğrula
                ciphertext = message_entry.get().replace(" ", "")
                if not ciphertext.isalpha():
                    raise ValueError("Şifrelenmiş metin sadece harfler içermeli!")
            
                m_str = m_entry.get().strip()
                if not m_str.isdigit() or int(m_str) <= 0:
                    raise ValueError("Parça uzunluğu (m) pozitif tam sayı olmalı!")
                m = int(m_str)
            
                key_str = key_entry.get().strip()
                key_list = key_str.split()
                if len(key_list) != m or not all(item.isdigit() for item in key_list):
                    raise ValueError(f"Anahtar, {m} adet sayı içermeli!")
                key = list(map(int, key_list))
                if sorted(key) != list(range(1, m + 1)):
                    raise ValueError(f"Anahtar, 1'den {m}'e kadar tüm sayıları içermeli!")
            
            
                decrypted_text = permütasyon_sifreleme.encrypt(ciphertext, m, key)
            
                result_text.delete("1.0", tk.END)     
                result_text.insert(tk.END, f"{decrypted_text}")

            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")

    elif algorithm == "YERDEĞİŞTİRME":
        # Anahtar girişi artık kaldırıldı, direkt kullanıyor
        def process():

            try:
                key_dict = yer_degistirme_sifreleme.load_key()
            except Exception as e:
                messagebox.showerror("Hata", str(e))
                return

            raw = message_entry.get()
            if not raw.strip():
                messagebox.showwarning("Uyarı", "Lütfen şifrelenecek metni girin.")
                return

            ciphertext = yer_degistirme_sifreleme.turkish_upper(raw.replace(" ", ""))
            if not ciphertext.isalpha():
                messagebox.showerror("Hata", "Metin yalnızca harflerden oluşmalı!")
                return

            try:
                plaintext = yer_degistirme_sifreleme.encrypt(ciphertext, key_dict)
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, plaintext)
            except Exception as e:
                messagebox.showerror("Hata", f"Şifreleme sırasında hata:\n{e}")


    elif algorithm == "KAYDIRMALI":
        tk.Label(input_frame, text="Anahtar (0–28 arası tam sayı):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        key_entry = tk.Entry(input_frame, width=10,font=("Arial", 12), bg="#D6EAF8")
        key_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def process():
        

            ciphertext = message_entry.get().strip()
            key_str = key_entry.get().strip()    

            # 1) Anahtarın sayısal olup olmadığını kontrol et
            if not key_str.isdigit():
                messagebox.showerror("Hata", "Anahtar pozitif tam sayı olmalı!")
                return    

            key = int(key_str)
            # 2) Anahtarın alfabe uzunluğu içinde olup olmadığını kontrol et
            alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
            if not (0 <= key < len(alphabet)):
                messagebox.showerror("Hata",
                    f"Anahtar 0 ile {len(alphabet)-1} arasında olmalı!")
                return    

            # 3) Decrypt işlemini çağır ve sonucu göster
            try:
                decrypted = kaydirmali_sifreleme.encrypt_text(ciphertext, key)
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, f"{decrypted}")
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")
        
    elif algorithm == "ROTA":
        tk.Label(input_frame, text="Anahtar (pozitif tam sayı):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        key_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        key_entry.grid(row=0, column=1, padx=5, pady=5)

        def process():
            try:
                # Metni alırken boşlukları kaldırıyoruz.
                raw_text = message_entry.get().strip().replace(" ", "")
                # Türkçe'ye uygun şekilde büyük harfe çevirme: normal upper() yerine turkish_upper kullanıyoruz.
                text = rota_sifreleme.turkish_upper(raw_text)

                key_str = key_entry.get().strip()

                # Girdi kontrolü
                if not key_str.isdigit():
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, "Hata: Anahtar bir sayı olmalı!")
                    return

                key = int(key_str)
                if key <= 0:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, "Hata: Anahtar pozitif olmalı!")
                    return

                # ROTA algoritmasının encrypt_spiral fonksiyonunu çağırıyoruz.
                encrypted_text = rota_sifreleme.encrypt_spiral(text, key)

                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{encrypted_text}")

            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")


    elif algorithm == "VİGENERE":
        tk.Label(input_frame, text="Anahtar Kelime:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        key_entry = tk.Entry(input_frame, width=20, font=("Arial", 12), bg="#D6EAF8")
        key_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def process():
            try:
                ciphertext = message_entry.get().strip()
                key = key_entry.get().strip()
                
                decrypted = Vigenère_sifreleme.vigenere_encrypt(ciphertext, key)
                if decrypted:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"{decrypted}")
                else:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, "Çözümlenemedi.")
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")
    
    elif algorithm == "DÖRTKARE":
        tk.Label(input_frame, text="Sütun Sayısı:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        columns_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bg="#D6EAF8")
        columns_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def process():
            try:
                # GUI üzerinden girilen metni ve sütun sayısını alıyoruz.
                ciphertext = message_entry.get().strip().upper().replace(" ", "")
                columns = int(columns_entry.get())
                # dortkare_cozme modülündeki decrypt fonksiyonunu çağırıyoruz.
                decrypted_text = dort_kare_sifreleme.encrypt(ciphertext, columns)
            
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{decrypted_text}")
                
                
            except Exception as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Hata: {str(e)}")

    # İşlem ve E-posta gönderme butonları
    # İşlem ve E-posta gönderme butonları
    button_frame = tk.Frame(cipher_window, bg="white")
    button_frame.pack(pady=10)    

    process_button = tk.Button(button_frame, text="SIFRELE", font=("Arial", 12), 
                               command=process, bg="#58D68D", fg="white", width=10)
    process_button.grid(row=0, column=0, padx=10)    

    send_button = tk.Button(cipher_window, text="GÖNDER", font=("Arial", 12),
                            command=lambda: send_encrypted_email(result_text), bg="#3498DB", fg="white")
    send_button.pack(pady=5)

def send_encrypted_email(result_text):
    """E-posta gönderme fonksiyonu"""
    encrypted_text = result_text.get("1.0", "end-1c").replace("Şifreli Mesaj: ", "")
    if not encrypted_text.strip():
        messagebox.showwarning("Uyarı", "Önce bir mesaj şifreleyin!")
        return
    send_email(encrypted_text)