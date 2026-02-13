## Menentukan password yang benar
password = "rianda"
## Menentukan batas maksimal percobaan login yaitu 3 kali
max_attemp = 3
## Menginisialisasi jumlah percobaan awal (dimulai dari 0)
attemp = 0

## Perulangan while tetap berjalan selama jumlah percobaan masih kurang dari batas yaitu belum 3 kali
while max_attemp > attemp:
    ## Meminta input password dari user
    pw = input("Masukkan Password: ")
    ## Menambah jumlah percobaan setiap kali user mencoba memasukkan password
    attemp += 1

    ## Mengecek apakah password yang dimasukkan sesuai dengan password yang benar
    if password == pw:
        print("Anda berhasil login")    ## Jika benar, tampilkan pesan berhasil
        break                           ## Keluar dari perulangan karena login berhasil
    ## Jika password salah
    else:
        ## Hitung sisa kesempatan yang tersisa
        sisa = max_attemp - attemp
        ## Jika masih ada sisa kesempatan
        if sisa > 0:
            print("Maaf anda salah memasukkan password.")   ## Tampilkan pesan salah
        ## Jika kesempatan sudah habis (3 kali salah)
        else:
            print("Anda telah mencoba 3 kali. Akses anda ditolak.")   ## Tampilkan pesan gagal