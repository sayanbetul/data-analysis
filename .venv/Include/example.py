import matplotlib.pyplot as plt

def read_coordinates_from_bde(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        # İlk satırı başlık olarak kabul et ve atla
        header = file.readline()
        for line in file:
            # Satırı virgül ile ayırıyoruz
            values = line.strip().split(',')
            # 4 değer olup olmadığını kontrol et
            if len(values) == 4:
                try:
                    x1, x2, y1, y2 = map(float, values)  # Değerleri float'a çeviriyoruz
                    coordinates.append((x1, x2, y1, y2))
                except ValueError as e:
                    print(f"Hata: {e}. Uygun formatta olmayan satır: {line.strip()}")
            else:
                print(f"Uygun formatta olmayan satır: {line.strip()}")
    return coordinates

# Dosya yolu
file_path = 'c:/Users/Betul/Desktop/PLC/coordinates.bde'

# Koordinatları oku
coords = read_coordinates_from_bde(file_path)

# Koordinatları ayrı listelere ayırıyoruz
x1_coords = [coord[0] for coord in coords]
x2_coords = [coord[1] for coord in coords]
y1_coords = [coord[2] for coord in coords]
y2_coords = [coord[3] for coord in coords]

# Grafiği çizdirme
plt.plot(x1_coords, y1_coords, marker='o', label='Seri 1 (x1, y1)')
plt.plot(x2_coords, y2_coords, marker='x', label='Seri 2 (x2, y2)')

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title('Koordinat Grafiği')
plt.grid(True)
plt.legend()  # Grafikteki serileri göstermek için
plt.show()
