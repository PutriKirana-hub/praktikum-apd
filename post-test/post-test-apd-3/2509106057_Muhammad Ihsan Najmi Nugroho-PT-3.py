# LOGIN 
username_benar = "Ihsan"
password_benar = "057"

print("FORM LOGIN")
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

if username == username_benar and password == password_benar:
    print("Login berhasil!")
else:
    if username != username_benar and password != password_benar:
        print("Login gagal! Username dan Password salah.")
    elif username != username_benar:
        print("Login gagal! Username salah.")
    else:
        print("Login gagal! Password salah.")
    exit()

# KONVERSI PANJANG

print("KONVERSI PANJANG")
feet = float(input("Masukkan panjang (feet): "))
print(str(feet) + "kaki=" + str(feet * 0.3048) + "meter")

km = float(input("Masukkan panjang (kilometer): "))
print(str(km) + "km=" + str(km * 1000) + "meter")

cm = float(input("Masukkan panjang (centimeter): "))
print(str(cm) + "cm=" + str(cm / 100) + "meter")



# KONVERSI MASSA

print("KONVERSI MASSA")
pon = float(input("Masukkan massa (pon):"))
print(str(pon) + "pon=" + str(pon * 0.453592) + " kg")

ton = float(input("Masukkan massa (ton):"))
print(str(ton) + "ton=" + str(ton * 1000) + "kg")

gram = float(input("Masukkan massa (gram):"))
print(str(gram) + "gram=" + str(gram / 1000) + "kg")

ons = float(input("Masukkan massa (ons): "))
print(str(ons) + "ons=" + str(ons * 0.1) + "kg")

mg = float(input("Masukkan massa (mg):"))
print(str(mg) + "mg=" + str(mg / 1000000) + "kg")

# KONVERSI SUHU

print("KONVERSI SUHU")
c = float(input("Masukkan suhu (Celcius):"))
print(str(c) + "Celcius=" + str(c + 273.15) + "K")

f = float(input("Masukkan suhu (Fahrenheit):"))
print(str(f) + "Fahrenheit=" + str((f - 32) * 5/9 + 273.15) + "K")

r = float(input("Masukkan suhu (Reamur):"))
print(str(r) + "Reamur=" + str(r * 5/4 + 273.15) + "K")


# KONVERSI WAKTU

print("KONVERSI WAKTU")
menit = float(input("Masukkan waktu (menit):"))
print(str(menit) + "menit=" + str(menit * 60) + "detik")

jam = float(input("Masukkan waktu (jam):"))
print(str(jam) + "jam=" + str(jam * 3600) + "detik")

# KONVERSI MATA UANG

print("KONVERSI MATA UANG")
rp = float(input("Masukkan Rupiah:"))
print("Rp" + str(rp) + "=$" + str(rp / 16000))

usd = float(input("Masukkan Dollar: "))
print("$" + str(usd) + "=Rp" + str(usd * 16000))