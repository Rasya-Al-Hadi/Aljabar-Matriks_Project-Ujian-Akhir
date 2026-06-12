import Rasya012 as mat

matriks_A = [
    [9, 8, 6],
    [5, 7, 4],
    [2, 1, 3]
]

matriks_B = [
    [7, 3, 2],
    [6, 4, 8],
    [5, 9, 1]
]

print("=== PENGUJIAN MODUL STRUKTUR DATA ===")

print("\n1. Hasil Penjumlahan Matriks A + B:")
hasil_tambah = mat.tambah_matriks(matriks_A, matriks_B)
for baris in hasil_tambah:
    print(baris)

print("\n2. Hasil Pengurangan Matriks A - B:")
hasil_kurang = mat.kurang_matriks(matriks_A, matriks_B)
for baris in hasil_kurang:
    print(baris)

print("\n3. Hasil Perkalian Matriks A x B:")
hasil_kali = mat.kali_matriks(matriks_A, matriks_B)
for baris in hasil_kali:
    print(baris)

print("\n4. Nilai Determinan Matriks A (3x3):")
print(f"Matriks A: {matriks_A}")
print(f"Determinan = {mat.determinan_3x3(matriks_A)}")

print("\n5. Nilai Determinan Matriks B (3x3):")
print(f"Matriks B: {matriks_B}")
print(f"Determinan = {mat.determinan_3x3(matriks_B)}")