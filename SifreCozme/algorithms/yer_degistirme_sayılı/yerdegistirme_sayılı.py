def coz(sifreli_metin, key):
    satir_sayisi = len(sifreli_metin) // key
    if len(sifreli_metin) % key != 0:
        satir_sayisi += 1
        
    # Boş matris oluştur
    matris = [['X'] * key for _ in range(satir_sayisi)]
    
    index = 0
    for j in range(key):  
        for i in range(satir_sayisi): 
            if index < len(sifreli_metin):
                matris[i][j] = sifreli_metin[index]
                index += 1
    
    cozulmus_metin = ""
    for satir in matris:
        cozulmus_metin += ''.join(satir)
    
    dolgu_karakteri = 'X'
    cozulmus_metin = cozulmus_metin.rstrip(dolgu_karakteri)
    
    return cozulmus_metin

if __name__ == "__main__":
    sifreli_metin = input("Çözülecek şifreli metni girin: ")
    key = int(input("Anahtar (sütun sayısı) girin: "))
    
    cozulmus = coz(sifreli_metin, key)
    print(f"Çözülmüş metin: {cozulmus}")


    