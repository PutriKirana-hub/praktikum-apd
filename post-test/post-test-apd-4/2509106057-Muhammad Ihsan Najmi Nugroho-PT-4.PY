# LOGIN 
while True:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password (3 digit terakhir NIM): ")

    if username == "Ihsan" and password == "057":
        print("Login berhasil!\n")
        break
    else:
        print("Username atau Password salah. Coba lagi!\n")

# Variabel untuk masing-masing golongan darah
A_positif = 0
A_negatif = 0
B_positif = 0
B_negatif = 0
AB_positif = 0
AB_negatif = 0
O_positif = 0
O_negatif = 0

# Loop input data darah
while True:
    golongan = input("Masukkan golongan darah (A, B, AB, O): ").upper()

    if golongan == "A":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            A_positif += jumlah * 500
        elif rhesus == "-":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            A_negatif += jumlah * 500
        else:
            print("Rhesus tidak valid.")
            continue

    elif golongan == "B":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            B_positif += jumlah * 500
        elif rhesus == "-":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            B_negatif += jumlah * 500
        else:
            print("Rhesus tidak valid.")
            continue

    elif golongan == "AB":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            AB_positif += jumlah * 500
        elif rhesus == "-":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            AB_negatif += jumlah * 500
        else:
            print("Rhesus tidak valid.")
            continue

    elif golongan == "O":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            O_positif += jumlah * 500
        elif rhesus == "-":
            jumlah = int(input("Masukkan jumlah kantong darah: "))
            O_negatif += jumlah * 500
        else:
            print("Rhesus tidak valid.")
            continue
    else:
        print("Golongan darah tidak valid.")
        continue

    ulang = input("Apakah Anda ingin input lagi? (Y/T): ").upper()
    if ulang == "T":
        break

# OUTPUT RINGKASAN
print("\n=== RINGKASAN DATA DARAH (ml) ===")
if A_positif > 0:
    print(f"A+ : {A_positif} ml")
if A_negatif > 0:
    print(f"A- : {A_negatif} ml")
if B_positif > 0:
    print(f"B+ : {B_positif} ml")
if B_negatif > 0:
    print(f"B- : {B_negatif} ml")
if AB_positif > 0:
    print(f"AB+ : {AB_positif} ml")
if AB_negatif > 0:
    print(f"AB- : {AB_negatif} ml")
if O_positif > 0:
    print(f"O+ : {O_positif} ml")
if O_negatif > 0:
    print(f"O- : {O_negatif} ml")