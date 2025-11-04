import os

#Variabelk
data_sinergi = {}
akun = {"admin": "123", "user": "abc"}
login_user = ""

#Clearlayar
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
