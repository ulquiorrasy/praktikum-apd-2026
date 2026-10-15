# kartu = {"merah", "merah", "biru", "hijau"}

# # kartu.add("hytam")

# # kartu.remove("hijau")

# kartu.discard("red")

# print(kartu)

# matkul = ["apd", "orsikom", "apd", "kalkulus"]

# sks = set(matkul)
# print(sks)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# aslab1 = {"fina", "shasha", "risma", "attar"}
# aslab2 = {"larry", "attar", "haekal"}

# aslab3 = {"rafi", "rendy", "Yoga"}
# gabung = aslab1.union(aslab2)

# gabunganlengkap = gabung.union(aslab3)
# print(gabunganlengkap)

# irisan_aslab1_aslab2 = aslab2.difference(aslab1)
# print(irisan_aslab1_aslab2)

# Matkul = {
# "Matkul_ganjil" : "kalkulus",
# "Matkul_genap" : "statistik"
# }

# print(Matkul["Matkul_ganjil"])

# print(Matkul.get("Matkul_genap", "Key tidak ada"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# print(len(game))

# game_copy = game.copy()

# del game_copy["valorant"]
# del game_copy["mobile legend"]

# print(game_copy)
# for i in game.values():
#     print(i)

# for key,value in game.items():
#     print(key,value)

# game["resident evil"] = "horror"

# game.update({"minecraft" : "horror"})

# del game["valorant"]

# item_dihapus = game.pop("minecraft")

# for key,value in game.items():
#      print(key,value)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)

# print(menu)

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
for kategori in j:
    print(kategori)
print(menu)