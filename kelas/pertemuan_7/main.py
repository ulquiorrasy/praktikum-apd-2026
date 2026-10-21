# def sapa ():
#     print("halooo rasy")

# teks_sapaan = sapa()
# print(teks_sapaan)

# def hitung():
#     return 5 * 3

# print(hitung())

# def persegi(sisi):
#     hasil + sisi*sisi
#     return hasil

# persegi(5)

# def sapa(nama="rasya"):
#     return f"Halooo {nama}"

# print(sapa("kuchiki"))

# def menu():
#     print("1. Create")
#     print("2. Read")
#     print("3. Update")
#     print("4. Delete")

#     pilihan = input("Pilih menu: ")

# nama = "Larry"
# prodi = "Informatika"

# def data():
#     nama = "Alfi"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# data()

# print("Nama:", nama)
# print("Prodi:", prodi)

# def sapa():
#     print("Halooo Rukia")
#     sapa()

# sapa()

def faktorial(n):
#Base Case: Kondisi fungsi berhenti
    if n == 0 or n == 1:
        return 1
#Rekursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)
#Memanggil fungsi
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}")
