import tkinter as tk
from encryption import open_cipher_screen

def create_main_window():
    root = tk.Tk()
    root.title("Şifreleme Algoritması Seçimi")
    root.geometry("400x550")
    root.configure(bg="white")

    tk.Label(root, text="Mesajınızı şifrelemek için\naşağıdaki algoritmalardan birini seçiniz:", 
             font=("Arial", 12), bg="white").pack(pady=20)

    algorithms = [
        "ZİGZAG", "DOĞRUSAL ŞİFRELEME", "PERMÜTASYON", 
        "YERDEĞİŞTİRME", "ROTA", "VİGENERE", 
        "DÖRTKARE", "YERDEĞİŞTİRME SAYILI","KAYDIRMALI","HILL"
    ]
    
    colors = [
        "#FFB6C1", "#87CEFA", "#98FB98", "#FFD700","#87CEFA",
        "#DDA0DD", "#FFA07A", "#FFB6C1", "#87CEFA","#DDA0DD",
    ]
    
    for i, alg in enumerate(algorithms):
        btn = tk.Button(root, text=alg, font=("Arial", 12), 
                        command=lambda alg=alg: open_cipher_screen(root, alg), 
                        bg=colors[i % len(colors)])
        btn.pack(pady=5, fill="x", padx=50)

    return root