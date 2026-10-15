import os

cls = 'cls' if os.name == 'nt' else 'clear'

users = [
    ["Rasya Karlsefni", "067", "admin"],
    ["Thorkell", "760", "user"],
]

penduduk = [
    ["Thorfinn", "Islandia", "Bertani", "Aktif"],
    ["Gudrid", "Islandia", "Navigator", "Aktif"],
    ["Leif", "Greenland", "Berdagang", "Sakit"],
    ["Einar", "Inggris", "Bertani", "Aktif"],
    ["Hild", "Norwegia", "Berburu", "Aktif"],
    ["Bug Eyes", "Yunani", "Berdagang", "Aktif"],
    ["Cordelia", "Inggris", "Penjaga", "Aktif"],
    ["Ivar", "Islandia", "Penjaga", "Aktif"],
    ["styrk", "Islandia", "Penjaga", "Aktif"],
]

daftar_tugas = ["Bertani", "Berburu", "Berdagang", "Penjaga", "Navigator"]
daftar_status = ["Aktif", "Sakit"]

while True:
    os.system(cls)
    print("=" * 50)
    print("   SISTEM PENCATATAN PENDUDUK DESA VINLAND")
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        os.system(cls)
        print("=== LOGIN ===")
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        user_aktif = None
        for u in users:
            if u[0] == username and u[1] == password:
                user_aktif = u

        if user_aktif is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
        else:
            role = user_aktif[2]

            while True:
                os.system(cls)
                print("=" * 50)
                print(f"Login sebagai: {user_aktif[0]} ({role})")
                print("=" * 50)

                aksi = ""
                if role == "admin":
                    print("1. Tambah Penduduk (Create)")
                    print("2. Lihat Data (Read)")
                    print("3. Ubah Data (Update)")
                    print("4. Hapus Penduduk (Delete)")
                    print("5. Logout")
                    menu = input("Pilih menu: ").strip()
                    if menu == "1":
                        aksi = "create"
                    elif menu == "2":
                        aksi = "read"
                    elif menu == "3":
                        aksi = "update"
                    elif menu == "4":
                        aksi = "delete"
                    elif menu == "5":
                        aksi = "logout"
                else:
                    print("1. Lihat Data (Read)")
                    print("2. Logout")
                    menu = input("Pilih menu: ").strip()
                    if menu == "1":
                        aksi = "read"
                    elif menu == "2":
                        aksi = "logout"

                if aksi == "create":
                    os.system(cls)
                    print("=== TAMBAH PENDUDUK ===")
                    nama = input("Nama  : ").strip()
                    asal = input("Asal  : ").strip()

                    if nama == "" or asal == "":
                        print("Nama dan asal tidak boleh kosong!")
                    elif not nama.replace(" ", "").isalpha():
                        print("Nama hanya boleh berisi huruf!")
                    elif not asal.replace(" ", "").isalpha():
                        print("Asal hanya boleh berisi huruf!")
                    else:
                        duplikat = False
                        for p in penduduk:
                            if p[0].lower() == nama.lower():
                                duplikat = True

                        if duplikat:
                            print("Penduduk dengan nama tersebut sudah ada!")
                        else:
                            print("\nPilih tugas:")
                            for i in range(len(daftar_tugas)):
                                print(f"{i + 1}. {daftar_tugas[i]}")
                            pilih_tugas = input("Nomor tugas: ").strip()

                            if pilih_tugas.isdigit() and 1 <= int(pilih_tugas) <= len(daftar_tugas):
                                tugas = daftar_tugas[int(pilih_tugas) - 1]
                                penduduk.append([nama.title(), asal.title(), tugas, "Aktif"])
                                print(f"\nPenduduk {nama.title()} berhasil ditambahkan!")
                            else:
                                print("Pilihan tugas tidak valid! Data tidak disimpan.")
                    input("\nTekan Enter untuk kembali...")

                elif aksi == "read":
                    os.system(cls)
                    print("=== LIHAT DATA ===")
                    print("1. Tabel semua penduduk")
                    print("2. Ringkasan jumlah per tugas")
                    sub = input("Pilih: ").strip()

                    if sub == "1":
                        os.system(cls)
                        if len(penduduk) == 0:
                            print("Belum ada data penduduk.")
                        else:
                            print("=" * 58)
                            print(f"{'No':<4}{'Nama':<15}{'Asal':<15}{'Tugas':<14}{'Status':<8}")
                            print("-" * 58)
                            for i in range(len(penduduk)):
                                p = penduduk[i]
                                print(f"{i + 1:<4}{p[0]:<15}{p[1]:<15}{p[2]:<14}{p[3]:<8}")
                            print("-" * 58)
                            print(f"Total penduduk: {len(penduduk)} orang")
                    elif sub == "2":
                        os.system(cls)
                        print("=== RINGKASAN PENDUDUK PER TUGAS ===")
                        for t in daftar_tugas:
                            jumlah = 0
                            for p in penduduk:
                                if p[2] == t:
                                    jumlah += 1
                            print(f"{t}: {jumlah} orang")
                        print(f"\nTotal penduduk: {len(penduduk)} orang")
                    else:
                        print("Pilihan tidak valid!")
                    input("\nTekan Enter untuk kembali...")

                elif aksi == "update":
                    os.system(cls)
                    print("=== UBAH DATA PENDUDUK ===")
                    if len(penduduk) == 0:
                        print("Belum ada data penduduk.")
                    else:
                        print(f"{'No':<4}{'Nama':<15}{'Asal':<15}{'Tugas':<14}{'Status':<8}")
                        print("-" * 58)
                        for i in range(len(penduduk)):
                            p = penduduk[i]
                            print(f"{i + 1:<4}{p[0]:<15}{p[1]:<15}{p[2]:<14}{p[3]:<8}")

                        nomor = input("\nNomor penduduk yang diubah: ").strip()
                        if not nomor.isdigit():
                            print("Input harus berupa angka!")
                        elif int(nomor) < 1 or int(nomor) > len(penduduk):
                            print("Nomor tidak ditemukan!")
                        else:
                            idx = int(nomor) - 1
                            print(f"\nData dipilih: {penduduk[idx][0]}")
                            print("1. Ubah tugas")
                            print("2. Ubah status")
                            print("3. Ubah nama")
                            print("4. Ubah asal")
                            sub = input("Pilih: ").strip()

                            if sub == "1":
                                for i in range(len(daftar_tugas)):
                                    print(f"{i + 1}. {daftar_tugas[i]}")
                                baru = input("Nomor tugas baru: ").strip()
                                if baru.isdigit() and 1 <= int(baru) <= len(daftar_tugas):
                                    penduduk[idx][2] = daftar_tugas[int(baru) - 1]
                                    print("Tugas berhasil diubah!")
                                else:
                                    print("Pilihan tugas tidak valid!")
                            elif sub == "2":
                                for i in range(len(daftar_status)):
                                    print(f"{i + 1}. {daftar_status[i]}")
                                baru = input("Nomor status baru: ").strip()
                                if baru.isdigit() and 1 <= int(baru) <= len(daftar_status):
                                    penduduk[idx][3] = daftar_status[int(baru) - 1]
                                    print("Status berhasil diubah!")
                                else:
                                    print("Pilihan status tidak valid!")
                            elif sub == "3":
                                baru = input("Nama baru: ").strip()
                                if baru == "" or not baru.replace(" ", "").isalpha():
                                    print("Nama tidak valid (tidak boleh kosong, hanya huruf)!")
                                else:
                                    penduduk[idx][0] = baru.title()
                                    print("Nama berhasil diubah!")
                            elif sub == "4":
                                baru = input("Asal baru: ").strip()
                                if baru == "" or not baru.replace(" ", "").isalpha():
                                    print("Asal tidak valid (tidak boleh kosong, hanya huruf)!")
                                else:
                                    penduduk[idx][1] = baru.title()
                                    print("Asal berhasil diubah!")
                            else:
                                print("Pilihan tidak valid!")
                    input("\nTekan Enter untuk kembali...")

                elif aksi == "delete":
                    os.system(cls)
                    print("=== HAPUS PENDUDUK ===")
                    if len(penduduk) == 0:
                        print("Belum ada data penduduk.")
                    else:
                        print(f"{'No':<4}{'Nama':<15}{'Asal':<15}{'Tugas':<14}{'Status':<8}")
                        print("-" * 58)
                        for i in range(len(penduduk)):
                            p = penduduk[i]
                            print(f"{i + 1:<4}{p[0]:<15}{p[1]:<15}{p[2]:<14}{p[3]:<8}")

                        nomor = input("\nNomor penduduk yang dihapus: ").strip()
                        if not nomor.isdigit():
                            print("Input harus berupa angka!")
                        elif int(nomor) < 1 or int(nomor) > len(penduduk):
                            print("Nomor tidak ditemukan!")
                        else:
                            idx = int(nomor) - 1
                            konfirmasi = input(f"Yakin hapus {penduduk[idx][0]}? (y/n): ").strip().lower()
                            if konfirmasi == "y":
                                nama_hapus = penduduk[idx][0]
                                penduduk.pop(idx)
                                print(f"Data {nama_hapus} berhasil dihapus!")
                            elif konfirmasi == "n":
                                print("Penghapusan dibatalkan.")
                            else:
                                print("Input harus y atau n! Penghapusan dibatalkan.")
                    input("\nTekan Enter untuk kembali...")

                elif aksi == "logout":
                    break

                else:
                    print("Pilihan menu tidak valid!")
                    input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        os.system(cls)
        print("=== REGISTER (Pengguna Biasa) ===")
        username = input("Username baru : ").strip()

        if username == "" or " " in username:
            print("Username tidak boleh kosong atau mengandung spasi!")
        elif len(username) < 4:
            print("Username minimal 4 karakter!")
        else:
            sudah_ada = False
            for u in users:
                if u[0].lower() == username.lower():
                    sudah_ada = True

            if sudah_ada:
                print("Username sudah dipakai!")
            else:
                password = input("Password baru : ").strip()
                if len(password) < 6:
                    print("Password minimal 6 karakter!")
                else:
                    ulang = input("Ulangi password: ").strip()
                    if ulang != password:
                        print("Password tidak sama!")
                    else:
                        users.append([username, password, "user"])
                        print("Registrasi berhasil! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        os.system(cls)
        print("Terima kasih, sampai jumpa di Vinland!")
        break

    else:
        print("Pilihan menu tidak valid!")
        input("Tekan Enter untuk kembali...")