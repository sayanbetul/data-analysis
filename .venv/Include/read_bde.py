def read_coordinates_from_bde(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        # Dosyanın başındaki başlık satırını atlamak istiyorsanız, ilk satırı okuyabilirsiniz
        header = file.readline()  # Eğer başlık yoksa bu satırı kaldırabilirsiniz
        for line in file:
            # Satırı virgül ile ayırarak x1, x2, y1 ve y2 değerlerini alıyoruz
            values = line.strip().split(',')
            # 4 değer olup olmadığını kontrol et
            if len(values) == 4:
                try:
                    x1, x2, y1, y2 = map(float, values)  # Değerleri float'a çeviriyoruz
                    coordinates.append((x1, x2, y1, y2))  # Koordinatları tuple olarak listeye ekliyoruz
                except ValueError as e:
                    print(f"Hata: {e}. Uygun formatta olmayan satır: {line.strip()}")
            else:
                print(f"Uygun formatta olmayan satır: {line.strip()}")
    return coordinates

# Dosya yolu
file_path = 'c:/Users/Betul/Desktop/PLC/coordinates.bde'

# Koordinatları oku
coords = read_coordinates_from_bde(file_path)
print(coords)
