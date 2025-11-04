from Clearscreen import akun, clear_screen, login_user
from sinergi import menu_utama

#Login
def login(username, password):
    if username in akun and akun[username] == password:
        return True
    return False

#Regus
def register():
    clear_screen()
    print("=== Register Akun ===")
    user_baru = input("Masukkan username baru: ")
    pass_baru = input("Masukkan password: ")

    if user_baru in akun:
        print("Username sudah digunakan!")
    else:
        akun[user_baru] = pass_baru
        print("Registrasi berhasil!")

    input("Enter untuk kembali...")

# Rekursig
def menu_login():
    from utils import login_user
    clear_screen()
    print("=== LOGIN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = input("Username: ")
        pw = input("Password: ")
        if login(user, pw):
            from utils import login_user
            globals()['login_user'] = user
            menu_utama()
        else:
            print("Username atau password salah!")
            input("Enter untuk kembali...")
            menu_login()
    elif pilih == "2":
        register()
        menu_login()
    elif pilih == "3":
        exit()
    else:
        print("Pilihan tidak valid!")
        input("Enter untuk kembali...")
        menu_login()