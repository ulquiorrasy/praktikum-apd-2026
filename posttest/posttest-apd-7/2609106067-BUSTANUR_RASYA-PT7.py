import os

cls = 'cls' if os.name == 'nt' else 'clear'

users = {
    "Rasya Karlsefni": {"password": "067", "role": "admin"},
    "Askeladd": {"password": "760", "role": "user"},
}

penduduk = {
    1: {"nama": "Thorfinn", "asal": "Islandia", "tugas": "Bertani", "status": "Aktif"},
    2: {"nama": "Gudrid", "asal": "Islandia", "tugas": "Navigator", "status": "Aktif"},
    3: {"nama": "Leif", "asal": "Greenland", "tugas": "Berdagang", "status": "Sakit"},
    4: {"nama": "Einar", "asal": "Inggris", "tugas": "Bertani", "status": "Aktif"},
    5: {"nama": "Hild", "asal": "Norwegia", "tugas": "Berburu", "status": "Aktif"},
    6: {"nama": "Bug Eyes", "asal": "Yunani", "tugas": "Berdagang", "status": "Aktif"},
    7: {"nama": "Cordelia", "asal": "Inggris", "tugas": "Penjaga", "status": "Aktif"},
    8: {"nama": "Ivar", "asal": "Islandia", "tugas": "Penjaga", "status": "Aktif"},
    9: {"nama": "Styrk", "asal": "Islandia", "tugas": "Penjaga", "status": "Aktif"},
}

id_berikutnya = 10

daftar_tugas = {1: "Bertani", 2: "Berburu", 3: "Berdagang", 4: "Penjaga", 5: "Navigator"}
daftar_status = {1: "Aktif", 2: "Sakit"}


def buat_id_baru():
    global id_berikutnya
    id_baru = id_berikutnya
    id_berikutnya += 1
    return id_baru


def hitung_aktif():
    jumlah = 0
    for data in penduduk.values():
        if data["status"] == "Aktif":
            jumlah += 1
    return jumlah


def validasi_teks(teks):
    bersih = teks.replace(" ", "")
    return bersih.isalpha()


def nama_sudah_ada(nama):
    for data in penduduk.values():
        if data["nama"].lower() == nama.lower():
            return True
    return False


def cek_login(username, password):
    try:
        akun = users[username]
    except KeyError:
        return None
    if akun["password"] == password:
        return akun["role"]
    return None


def minta_angka(pesan):
    try:
        nilai = int(input(pesan).strip())
        return nilai
    except ValueError:
        print("Input harus berupa angka!")
        return minta_angka(pesan)


def cetak_header(judul):
    os.system(cls)
    print("=" * 50)
    print(f"   {judul}")
    print("=" * 50)


def jeda():
    input("\nTekan Enter untuk kembali...")


def tampilkan_tabel():
    if len(penduduk) == 0:
        print("Belum ada data penduduk.")
    else:
        print(f"{'ID':<5}{'Nama':<15}{'Asal':<15}{'Tugas':<14}{'Status':<8}")
        print("-" * 58)
        for id_p, data in penduduk.items():
            print(f"{id_p:<5}{data['nama']:<15}{data['asal']:<15}{data['tugas']:<14}{data['status']:<8}")
        print("-" * 58)
        print(f"Total penduduk: {len(penduduk)} orang (Aktif: {hitung_aktif()} orang)")


def tampilkan_ringkasan():
    ringkasan = {}
    for t in daftar_tugas.values():
        ringkasan[t] = 0
    for data in penduduk.values():
        if data["tugas"] in ringkasan:
            ringkasan[data["tugas"]] += 1
    for t, jumlah in ringkasan.items():
        print(f"{t}: {jumlah} orang")
    print(f"\nTotal penduduk: {len(penduduk)} orang")


while True:
    cetak_header("SISTEM PENCATATAN PENDUDUK DESA VINLAND")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        cetak_header("LOGIN")
        username = input("Username : ").strip()
        password = input("Password : ").strip()
        role = cek_login(username, password)

        if role is None:
            print("Username atau password salah!")
            jeda()
        else:
            while True:
                cetak_header(f"Login sebagai: {username} ({role})")

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
                    cetak_header("TAMBAH PENDUDUK")
                    nama = input("Nama  : ").strip()
                    asal = input("Asal  : ").strip()

                    if nama == "" or asal == "":
                        print("Nama dan asal tidak boleh kosong!")
                    elif not validasi_teks(nama):
                        print("Nama hanya boleh berisi huruf!")
                    elif not validasi_teks(asal):
                        print("Asal hanya boleh berisi huruf!")
                    elif nama_sudah_ada(nama):
                        print("Penduduk dengan nama tersebut sudah ada!")
                    else:
                        print("\nPilih tugas:")
                        for kode, nama_tugas in daftar_tugas.items():
                            print(f"{kode}. {nama_tugas}")
                        pilih_tugas = minta_angka("Nomor tugas: ")

                        try:
                            tugas = daftar_tugas[pilih_tugas]
                        except KeyError:
                            print("Pilihan tugas tidak valid! Data tidak disimpan.")
                        else:
                            id_baru = buat_id_baru()
                            penduduk[id_baru] = {
                                "nama": nama.title(),
                                "asal": asal.title(),
                                "tugas": tugas,
                                "status": "Aktif",
                            }
                            print(f"\nPenduduk {nama.title()} berhasil ditambahkan dengan ID {id_baru}!")
                    jeda()

                elif aksi == "read":
                    cetak_header("LIHAT DATA")
                    print("1. Tabel semua penduduk")
                    print("2. Ringkasan jumlah per tugas")
                    sub = input("Pilih: ").strip()

                    if sub == "1":
                        cetak_header("TABEL PENDUDUK")
                        tampilkan_tabel()
                    elif sub == "2":
                        cetak_header("RINGKASAN PENDUDUK PER TUGAS")
                        tampilkan_ringkasan()
                    else:
                        print("Pilihan tidak valid!")
                    jeda()

                elif aksi == "update":
                    cetak_header("UBAH DATA PENDUDUK")
                    if len(penduduk) == 0:
                        print("Belum ada data penduduk.")
                    else:
                        tampilkan_tabel()
                        id_p = minta_angka("\nID penduduk yang diubah: ")

                        try:
                            data = penduduk[id_p]
                        except KeyError:
                            print("ID tidak ditemukan!")
                        else:
                            print(f"\nData dipilih: {data['nama']}")
                            print("1. Ubah tugas")
                            print("2. Ubah status")
                            print("3. Ubah nama")
                            print("4. Ubah asal")
                            sub = input("Pilih: ").strip()

                            if sub == "1":
                                for kode, nama_tugas in daftar_tugas.items():
                                    print(f"{kode}. {nama_tugas}")
                                baru = minta_angka("Nomor tugas baru: ")
                                try:
                                    tugas_baru = daftar_tugas[baru]
                                except KeyError:
                                    print("Pilihan tugas tidak valid!")
                                else:
                                    data["tugas"] = tugas_baru
                                    print("Tugas berhasil diubah!")
                            elif sub == "2":
                                for kode, nama_status in daftar_status.items():
                                    print(f"{kode}. {nama_status}")
                                baru = minta_angka("Nomor status baru: ")
                                try:
                                    status_baru = daftar_status[baru]
                                except KeyError:
                                    print("Pilihan status tidak valid!")
                                else:
                                    data["status"] = status_baru
                                    print("Status berhasil diubah!")
                            elif sub == "3":
                                baru = input("Nama baru: ").strip()
                                if baru == "" or not validasi_teks(baru):
                                    print("Nama tidak valid (tidak boleh kosong, hanya huruf)!")
                                else:
                                    data["nama"] = baru.title()
                                    print("Nama berhasil diubah!")
                            elif sub == "4":
                                baru = input("Asal baru: ").strip()
                                if baru == "" or not validasi_teks(baru):
                                    print("Asal tidak valid (tidak boleh kosong, hanya huruf)!")
                                else:
                                    data["asal"] = baru.title()
                                    print("Asal berhasil diubah!")
                            else:
                                print("Pilihan tidak valid!")
                    jeda()

                elif aksi == "delete":
                    cetak_header("HAPUS PENDUDUK")
                    if len(penduduk) == 0:
                        print("Belum ada data penduduk.")
                    else:
                        tampilkan_tabel()
                        id_p = minta_angka("\nID penduduk yang dihapus: ")

                        try:
                            data = penduduk[id_p]
                        except KeyError:
                            print("ID tidak ditemukan!")
                        else:
                            konfirmasi = input(f"Yakin hapus {data['nama']}? (y/n): ").strip().lower()
                            if konfirmasi == "y":
                                del penduduk[id_p]
                                print(f"Data {data['nama']} berhasil dihapus!")
                            elif konfirmasi == "n":
                                print("Penghapusan dibatalkan.")
                            else:
                                print("Input harus y atau n! Penghapusan dibatalkan.")
                    jeda()

                elif aksi == "logout":
                    break

                else:
                    print("Pilihan menu tidak valid!")
                    jeda()

    elif pilih == "2":
        cetak_header("REGISTER (Pengguna Biasa)")
        username = input("Username baru : ").strip()

        if username == "" or " " in username:
            print("Username tidak boleh kosong atau mengandung spasi!")
        elif len(username) < 4:
            print("Username minimal 4 karakter!")
        else:
            sudah_ada = False
            for u in users:
                if u.lower() == username.lower():
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
                        users[username] = {"password": password, "role": "user"}
                        print("Registrasi berhasil! Silakan login.")
        jeda()

    elif pilih == "3":
        os.system(cls)
        print("Terima kasih, sampai jumpa di Vinland!")
        break

    else:
        print("Pilihan menu tidak valid!")
        jeda()