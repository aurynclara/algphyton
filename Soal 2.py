"""
Buat program untuk menghitung biaya total pembelian oli motor di perusahaan bengkel motor
UD. Matahari
1. set variabel merk, harga, totbayar
2. input merk oli
3. jika merk oli = Duration SW20 1L, hargaoli=53000, selain itu
jika merk oli = Castrol Magnetec 1L, hargaoli = 50000, selain itu
jika merk oli = Federal Supreme XX 1L, harga oli= 54000, selain itu
jika merk oli = Yamalube 1L, harga oli=45000, selain itu
jika merk oli = Shell 1L, harga oli=46000
4. tampilkan merk oli, harga oli
"""
print("TRANSAKSI PEMBELIAN OLI DI BENGKEL MOTOR UD. MATAHARI")
print("=====================================================")
print(" Kode = A. Duratiaon SW20 1L")
print(" Kode = B. Castrol Magnetec 1L")
print(" Kode = C. Federal Supreme XX 1L")
print(" Kode = D. Yamalube 1L")
print(" Kode = E. Shell 1L")
print("=====================================================")

kode = ['a','b','c','d','e']
merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
harga = [53000,50000,54000,45000,46000]

pilihan = input(">> Masukkan Kode Merk Oli = ")
#identifikasi pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
elif pilihan=="c":
    idx = 2
elif pilihan=="d":
    idx = 3
elif pilihan=="e":
    idx = 4

print(">>> Pilihan Merk Oli = " + merk[idx])
print(">>> Harga Oli = Rp. " + str(harga[idx]))