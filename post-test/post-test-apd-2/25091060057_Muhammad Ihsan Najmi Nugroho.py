suhu_1 = 27
suhu_2 = 33
suhu_3 = 46
suhu_4 = 55
suhu_5 = 67
suhu_6 = 92

suhu = [suhu_1, suhu_2, suhu_3, suhu_4, suhu_5, suhu_6]

# Konversi
# Rumus:
# Fahrenheit = (C * 9/5) + 32
# Kelvin = C + 273
#Reamur = C * 4/5


f1 = (suhu_1 * 9/5) + 32
f2 = (suhu_2 * 9/5) + 32

k3 = suhu_3 + 273
k4 = suhu_4 + 273

r5 = suhu_5 * 4/5
r6 = suhu_6 * 4/5


jumlah = f1 + f2 + k3 + k4 + r5 + r6

rata2 = jumlah / len(suhu)

NIM = 57


Bolean = NIM < rata2

print("Suhu_1 =", suhu_1)
print("Suhu_2 =", suhu_2)
print("Suhu_3 =", suhu_3)
print("Suhu_4=", suhu_4)
print("Suhu_5 =", suhu_5)
print("Suhu_6 =", suhu_6)

print("Fahrenheit suhu_1 =", f1)
print("Fahrenheit suhu_2 =", f2)
print("Kelvin suhu_3 =", k3)
print("Kelvin suhu_4 =", k4)
print("Reamur suhu_5 =", r5)
print("Reamur suhu_6 =", r6)

print("jumlah =", jumlah)
print("rata2 =", rata2)
print("NIM =", NIM)
print("Bolean =", Bolean)

print(suhu[-4:])