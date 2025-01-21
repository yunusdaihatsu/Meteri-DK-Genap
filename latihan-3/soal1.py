#program membuat peraturan nilai

nilai_tugas=float(input("masukan nilai tugas"))
nilai_uts=float(input("masukan nilai uts"))
nilai_uas=float(input("masukan nilai uas"))

nilai_akhir=30/100* nilai_uts + 50/100 * nilai_uas + 20/100 * nilai_tugas

print("nilai akhir :",nilai_akhir)
