import math     #Library untuk operasi matematika

# Lambda function untuk menghitung luas lingkaran
# r: jari-jari lingkaran
luas_lingkaran = lambda r: math.pi * r*r

#contoh penggunaanya
jari_jari = 7   # Mengatur nilai jari-jari lingkaran
area = luas_lingkaran(jari_jari)    # Menghitung luas lingkaran menggunakan jari-jari
print(f"Luas Lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")