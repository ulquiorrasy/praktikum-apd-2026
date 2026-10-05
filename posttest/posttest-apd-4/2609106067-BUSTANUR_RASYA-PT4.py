USERNAME_BENAR = "Bustanur Jesse Rasya Pinkman"
PASSWORD_BENAR = "067"
 
percobaan = 0
login_berhasil = False
 
while percobaan < 3 and login_berhasil == False:
    username = input("Username: ")
    password = input("Password: ")
 
    if username.lower() == USERNAME_BENAR.lower() and password == PASSWORD_BENAR:
        login_berhasil = True
    else:
        percobaan += 1
        print("Login gagal!")
 
if login_berhasil == False:
    print("Login telah gagal 3 kali. Program dihentikan.")
else:
    print("Login berhasil")
 
    jalan = True
    while jalan:
        print("")
        print("SILAHKAN PILIH PAKET YANG ANDA INGINKAN")
        print("1. Paket Reguler (1 porsi)")
        print("2. Paket Anak (1 porsi)")
        print("3. Paket Keluarga (4 porsi)")
        print("4. Keluar")
 
        pilihan = input("Pilih menu: ")
 
        while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4":
            print("Opsi tidak valid")
            pilihan = input("Pilih menu: ")
 
        if pilihan == "4":
            jalan = False
            print("Terima kasih!")
        else:
            if pilihan == "1":
                jenis_paket = "Paket Reguler"
                porsi_per_paket = 1
            elif pilihan == "2":
                jenis_paket = "Paket Anak"
                porsi_per_paket = 1
            else:
                jenis_paket = "Paket Keluarga"
                porsi_per_paket = 4
 
            jumlah_paket = int(input("Jumlah paket: "))
 
            total_porsi = 0
            for i in range(jumlah_paket):
                total_porsi += porsi_per_paket
 
            if total_porsi >= 20:
                bonus = "5 paket buah"
            elif total_porsi >= 10:
                bonus = "3 botol susu"
            elif total_porsi >= 5:
                bonus = "1 paket vitamin"
            else:
                bonus = "Tidak ada bonus"
 
            print("")
            print("Jenis paket       :", jenis_paket)
            print("Jumlah paket      :", jumlah_paket)
            print("Total porsi       :", total_porsi, "porsi")
            print("Penerima manfaat  :", total_porsi, "orang")
            print("Bonus             :", bonus)
 