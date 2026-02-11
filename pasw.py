password = "riand"
max_attemp = 3
attemp = 0

while max_attemp > attemp:
    pw = input("Masukkan Password: ")
    attemp += 1
    if password == pw:
        print("Anda berhasil login")
        break               
    else:
        sisa = max_attemp - attemp
        if sisa > 0:
            print("Maaf password salah.")
        else:
            print("Anda telah mencoba 3x. Akses anda ditolak.")