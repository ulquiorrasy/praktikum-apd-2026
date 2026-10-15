# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1)

# print(formula1[0])

# for index.elemen in enumerate formula1:
#     print(index, elemen)
    
# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)

# sirkuit.append("rasya")
# print(sirkuit)

# sirkuit.extend({"greg", "gonzales"})
# print(sirkuit)

# sirkuit.insert(2, "alfi")
# print(sirkuit)

# sirkuit[3] = "apip"
# print(sirkuit)

# sirkuit[0:1] = ("rizky", "gabriel")
# print(sirkuit)

# del sirkuit[4]
# print(sirkuit)

# sirkuit.remove ("Marina Bay")
# print(sirkuit)

# nama_dihapus = sirkuit.pop(5)
# print(sirkuit)
# print(nama_dihapus)

# print(sirkuit[0:4])

# matkul_1 = ["kalkulus", "logmat", "apd"]
# matkul_2 = ["basis data", "apl", "pbo"]

# matkul_gabungan = matkul_1 + matkul_2
# print(matkul_gabungan)

# matkul_1 = matkul_1 * 5
# print(matkul_1)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# for i in line_up:
#     for j in i:
#         print(j)
# 
# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)

# print(type(listchara))

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)

# listchara.append("askeladd")
# print(listchara)

# del listchara[6]

# listchara.remove("Yukari")
# print(listchara)

chara = ("Yukari", "Yukino", "Odette", "Senku", "aizen", "rukia")
(Persona, Oregairu, Genshin, DrStone, *sisa_chara) = chara
# print(DrStone)
# print(Oregairu)

print(sisa_chara)