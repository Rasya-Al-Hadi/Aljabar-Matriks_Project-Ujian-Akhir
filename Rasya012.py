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
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil


def determinan_3x3(M):
    det = (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )
    return det