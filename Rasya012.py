def tambah_matriks(A, B):
    hasil = []
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def kurang_matriks(A, B):
    hasil = []
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def kali_matriks(A, B):
    hasil = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] = hasil[i][j] + (A[i][k] * B[k][j])
    return hasil

def determinan_sarrus(matriks):
    a, b, c = matriks[0]
    d, e, f = matriks[1]
    g, h, i = matriks[2]

    d1 = a * e * i
    d2 = b * f * g
    d3 = c * d * h

    s1 = c * e * g
    s2 = b * d * i
    s3 = a * f * h

    determinan = (d1 + d2 + d3) - (s1 + s2 + s3)

    print("Diagonal utama  :", d1, "+", d2, "+", d3, "=", d1 + d2 + d3)
    print("Diagonal sekunder:", s1, "+", s2, "+", s3, "=", s1 + s2 + s3)

    return determinan