#program membuat promosi dalam sebuah toko


print("Program Bonus Toko")


nilai=int(input("masukan nilai pembelian pelanggan : "))

if nilai >= 1500000 and  nilai <= 5000000 :
    print("Anda mendapatkan TV Bracket.")
elif nilai >= 5000000 :
    print("Anda mendapatkan Sound Bar.")
else:
    print("Tidak Ada Bonus.")
