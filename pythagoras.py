# Rumus pytagoras

import math # memanggil fungsi matematika

awal = str(input("masukkan nilai yang anda ingin cari: ")) # mau cari nilai apa

if awal == "a": # kalo pilih a
    b = float(input("masukkan nilai b: ")) # berapa nilai b nya?
    c = float(input("masukkan nilai c: ")) # berapa nilai c nya?

    hasil = f"nilai a adalah: {math.sqrt(pow(c,2) - pow(b,2))}" # nilai b dam c diitung masukkan kedalam variable hasil
elif awal == "b": # kalo pilih b
    a = float(input("masukkan nilai a: ")) # berapa nilai a nya?
    c = float(input("masukkan nilai c: ")) # berapa nilai c nya?

    hasil = f"nilai b adalah: {math.sqrt(pow(c,2) - pow(a,2))}" # nilai a dam c diitung masukkan kedalam variable hasil
elif awal == "c":  # kalo pilih b
    a = float(input("masukkan nilai a: ")) # berapa nilai a nya?
    b = float(input("masukkan nilai b: ")) # berapa nilai b nya?

    hasil = math.sqrt(pow(b,2) + pow(a,2)) # nilai b dam a diitung masukkan kedalam variable hasil
else:
    hasil = "nilai yang ada cari tidak valid" # kalo bukan antara a, b, c tampilin ini

print(hasil) # tampilin variable hasil
