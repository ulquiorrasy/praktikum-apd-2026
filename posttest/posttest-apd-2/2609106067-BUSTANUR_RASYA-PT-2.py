skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000
ongkos_kirim = 12000

total_pengeluaran = (skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkos_kirim)

data_harga = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]
rata_rata = total_pengeluaran / len(data_harga)

nim = 67

bolean = nim < rata_rata

print("Harga skincare_1  :", skincare_1)
print("Harga skincare_2  :", skincare_2)
print("Harga skincare_3  :", skincare_3)
print("Harga skincare_4  :", skincare_4)
print("Harga skincare_5  :", skincare_5)
print("Harga skincare_6  :", skincare_6)
print("Ongkos kirim      :", ongkos_kirim)
print("Total pengeluaran :", total_pengeluaran)
print("Rata-rata         :", rata_rata)
print("NIM (2 digit)     :", nim)
print("Boolean (nim < rata_rata) :", bolean)