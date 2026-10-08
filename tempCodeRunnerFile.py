class Rectangle:
    # Konstruktor dengan properti panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Fungsi untuk menghitung keliling
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    # Fungsi untuk menghitung luas
    def luas(self):
        return self.panjang * self.lebar

    # Fungsi __str__ untuk menampilkan objek sebagai string
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


# Pemanggilan fungsi dari kelas Rectangle
# Membuat objek persegi panjang dengan panjang 3 cm dan lebar 2 cm
rect = Rectangle(3, 2)

# Menampilkan objek sebagai string
print(rect)

# Menampilkan keliling
print("Keliling:", rect.keliling(), "cm")

# Menampilkan luas
print("Luas:", rect.luas(), "cm²")