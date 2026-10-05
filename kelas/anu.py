anggota = ["Alfi","Suheku","Rasya","Hafiz","Isna","Olivia","Yatha","Cinta","Gabriel","Maul","Khairil","Uwais","Rafif"]
bindam = ["Mba Ayana", "Bang Akbar"]

def show_menu():
    print("\nPilih menu: ")
    print("1. Tampilkan Anggota")
    print("2. Tampilkan Bindam")
    print("3. Tambahkan Anggota")
    print("4. Hapus Anggota")
    print("5. Profil Kelompok")
    print("6. Exit")

def add_member():
    nama_baru = input("Masukkan nama anggota baru: ")
    anggota.append(nama_baru)
    print(f"{nama_baru} berhasil ditambahkan ke daftar anggota.")

def show_member():
    print("\n")
    for i, member in enumerate(anggota):
        print(f"{i+1}. {member}")
    print(f"Jumlah anggota: {len(anggota)}")

def show_bindam():
    for i, nama in enumerate(bindam):
        print(f"{i+1}. {nama}")

def delete_member():
    show_member()
    index = int(input("Masukkan nomor anggota yang ingin dihapus: ")) - 1
    if 0 <= index < len(anggota):
        removed_member = anggota.pop(index)
        print(f"{removed_member} berhasil dihapus dari daftar anggota.")
    else:
        print("Nomor anggota tidak valid.")

def show_profil_kelompok():
    print("\nNama = Cloud Computing")
    print("Makna dan Filosofi logo")
    print("1. Warna biru navy = Kreatifitas dan loyalitas")
    print("2. Cloud membentuk awan = Identitas kelompok yang kreatif, kompak, dan semangat untuk berkembang")
    print("3. Jaringan di bawah awan = Kerja sama, hubungan, komunikasi antar anggota yang saling mendukung")

while True:
    show_menu()
    choice = input("\nMasukkan pilihan: ")
    try:
        if 0 <= int(choice) < 7:
            if choice == "1":
                show_member()
            if choice == "2":
                show_bindam()
            if choice == "3":
                add_member()
            if choice == "4":
                delete_member()
            if choice == "5":
                show_profil_kelompok()
            if choice == "6":
                exit()
        else:
            print("Menu tidak valid.")
            continue
    except ValueError:
        print("Masukkan angka yang valid.")
        continue