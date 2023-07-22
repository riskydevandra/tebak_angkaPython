import random

# Menghasilkan angka acak antara 1 dan 100
angka_rahasia = random.randint(1, 100)

# Menginisialisasi variabel untuk melacak jumlah tebakan
jumlah_tebakan = 0

# Memulai perulangan tebak-meneka
while True:
    # Meminta pengguna untuk memasukkan tebakan mereka
    tebakan = int(input("Tebak angka (antara 1 dan 100): "))
    
    # Menambah jumlah tebakan
    jumlah_tebakan += 1
    
    # Memeriksa apakah tebakan benar
    if tebakan == angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar dalam {jumlah_tebakan} tebakan.")
        break
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil. Coba lagi.")
    else:
        print("Angka terlalu besar. Coba lagi.")
