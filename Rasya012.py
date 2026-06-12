def tambah_matriks(A, B):
    """
    Fungsi untuk menjumlahkan dua matriks dengan ordo yang sama.
    """

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Ukuran matriks harus sama untuk penjumlahan.")
    
    baris = len(A)
    kolom = len(A[0])

    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] + B[i][j]
            
    return hasil


def kurang_matriks(A, B):
    """
    Fungsi untuk mengurangkan dua matriks dengan ordo yang sama.
    """

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Ukuran matriks harus sama untuk pengurangan.")
    
    baris = len(A)
    kolom = len(A[0])

    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] - B[i][j]
            
    return hasil


def kali_matriks(A, B):
    """
    Fungsi untuk mengalikan dua matriks (Ordo m x n dikali n x p).
    """

    if len(A[0]) != len(B):
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
        
    baris_A = len(A)
    kolom_A = len(A[0])
    kolom_B = len(B[0])

    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]
    
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
                
    return hasil


def determinan_3x3(M):
    """
    Fungsi untuk menghitung determinan matriks 3x3 menggunakan Metode Sarrus.
    """
    if len(M) != 3 or len(M[0]) != 3:
        raise ValueError("Fungsi ini khusus untuk matriks berordo 3x3.")

    pos = (M[0][0]*M[1][1]*M[2][2]) + (M[0][1]*M[1][2]*M[2][0]) + (M[0][2]*M[1][0]*M[2][1])
    neg = (M[0][2]*M[1][1]*M[2][0]) + (M[0][0]*M[1][2]*M[2][1]) + (M[0][1]*M[1][0]*M[2][2])
    
    return pos - neg