NAMA = "Hal Jordan"
NIM = "67"  

print("Green Lantern Corps")
nama = input("Masukkan nama\t: ").strip()
nim = input("Masukkan NIM\t: ").strip()

nim_2digit = nim[-2:] if len(nim) >= 2 else nim

nama_benar = True if nama == NAMA else False
nim_benar = True if nim == NIM else False

if nama_benar and nim_benar:
    login_berhasil = True
    print(f"\nLogin berhasil. Selamat datang, {nama}!\n")
elif not nama_benar and nim_benar:
    login_berhasil = False
    print("\nLogin gagal. Nama yang dimasukkan salah.")
elif nama_benar and not nim_benar:
    login_berhasil = False
    print("\nLogin gagal. NIM yang dimasukkan salah.")
else:
    login_berhasil = False
    print("\nLogin gagal. Nama dan NIM yang dimasukkan salah.")

if login_berhasil:
    reward_dasar = 1000 
    print("pilih misi yang ingin anda jalankan:")
    print("1. Misi Standar          (bonus 2%)")
    print("2. Misi Sulit            (bonus 5%)")
    print("3. Misi Kritis           (bonus 8%)")
    print("4. Misi Penyelamatan Bumi (bonus 12%)")

    pilihan = input("Masukkan nomor pilihan misi: ").strip()

    if pilihan == "1":
        nama_misi = "Misi Standar"
        persentase_bonus = 0.02
    elif pilihan == "2":
        nama_misi = "Misi Sulit"
        persentase_bonus = 0.05
    elif pilihan == "3":
        nama_misi = "Misi Kritis"
        persentase_bonus = 0.08
    elif pilihan == "4":
        nama_misi = "Misi Penyelamatan Bumi"
        persentase_bonus = 0.12
    else:
        nama_misi = ""
        persentase_bonus = -1 

    if persentase_bonus == -1:
        print("\nPilihan misi tidak tersedia. Silakan masukkan nomor misi yang valid.")
    else:
        reward_bonus = reward_dasar * persentase_bonus
        reward_akhir = reward_dasar + reward_bonus

        print(f"\nHASIL MISI: {nama_misi}")
        print(f"Reward dasar\t: {reward_dasar:.0f} poin energi")
        print(f"Bonus\t\t: {int(persentase_bonus * 100)}%")
        print(f"Reward bonus\t: {reward_bonus:.0f} poin energi")
        print(f"Reward akhir\t: {reward_akhir:.0f} poin energi")
else:
    print("apakah anda beneran anggota Green Lantern Corps? o_o.")