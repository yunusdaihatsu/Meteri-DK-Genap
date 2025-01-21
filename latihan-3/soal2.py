#program membuat promosi dalam sebuah toko


print("Program Bonus Toko")


belanja=int(input("masukan nilai pembelian pelanggan : "))

if belanja >= 1500000 and belanja  <= 5000000 :
    print("Anda mendapatkan TV Bracket.")
elif belanja >= 5000000 :
    print("Anda mendapatkan Sound Bar.")
else:
    print("Tidak Ada Bonus.")
