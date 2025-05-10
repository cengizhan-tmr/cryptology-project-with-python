from gui import create_main_window

if __name__ == "__main__":
    # Algoritma modüllerini düzenle
    import sys
    import os
    
    # Algoritma dizinini ekle
    current_dir = os.path.dirname(os.path.abspath(__file__))
    algorithms_dir = os.path.join(current_dir, "algorithms")
    
    # algorithms dizini yoksa oluştur
    if not os.path.exists(algorithms_dir):
        os.makedirs(algorithms_dir)
    
    sys.path.append(algorithms_dir)
    
    # Ana pencereyi oluştur ve başlat
    root = create_main_window()
    root.mainloop()
    