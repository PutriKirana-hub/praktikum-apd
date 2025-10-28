import os

#Variabel

data_sinergi = {}
akun = {"Admin": "Mie Ayam", "User": "123"}
login_user = ""

#Clear Layar
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Tampilkan Data
def tampilkan_data():
    clear_screen()
    print("=== Daftar Sinergi Magic Chess ===")
    if not data_sinergi:
        print("Belum ada data sinergi.")
    else:
        for id, s in data_sinergi.items():
            print(f"ID: {id} | Nama: {s['nama']} | Tipe: {s['tipe']} | Efek: {s['efek']} | Jumlah: {s['jumlah']}")
    input("\nTekan Enter untuk kembali...")


def menu_utama():
    clear_screen()
    print(f"=== Menu Utama ({login_user}) ===")
    print("1. Tambah Sinergi")
    print("2. Lihat Sinergi")
    print("3. Ubah Sinergi")
    print("4. Hapus Sinergi")
    print("5. Logout")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_sinergi()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        ubah_sinergi()
    elif pilih == "4":
        hapus_sinergi()
    elif pilih == "5":
        return
    else:
        print("Input tidak valid!")

    #Rekursif — kembali ke menu
    menu_utama()

#Tambah sinergi
def tambah_sinergi():
    clear_screen()
    global data_sinergi
    nama = input("Nama Sinergi: ")
    tipe = input("Tipe Sinergi: ")
    efek = input("Efek Sinergi: ")
    jumlah = input("Jumlah Hero yang dibutuhkan: ")

    
    if not jumlah.isdigit():
        print("Jumlah harus berupa angka!")
        input("Enter untuk kembali...")
        return

    id_baru = max(data_sinergi.keys()) + 1 if data_sinergi else 1
    data_sinergi[id_baru] = {
        "nama": nama,
        "tipe": tipe,
        "efek": efek,
        "jumlah": int(jumlah)
    }

    print("Data berhasil ditambahkan!")
    input("Enter untuk kembali...")

#Ubah sinergi
def ubah_sinergi():
    clear_screen()
    if not data_sinergi:
        print("Tidak ada data untuk diubah.")
        input("Enter untuk kembali...")
        return

    id_edit = input("Masukkan ID sinergi yang ingin diubah: ")
    if not id_edit.isdigit() or int(id_edit) not in data_sinergi:
        print("ID tidak ditemukan!")
        input("Enter untuk kembali...")
        return

    id_edit = int(id_edit)
    s = data_sinergi[id_edit]

   
    nama_baru = input(f"Nama baru ({s['nama']}): ")
    tipe_baru = input(f"Tipe baru ({s['tipe']}): ")
    efek_baru = input(f"Efek baru ({s['efek']}): ")
    jumlah_baru = input(f"Jumlah baru ({s['jumlah']}): ")

    if nama_baru != "": s["nama"] = nama_baru
    if tipe_baru != "": s["tipe"] = tipe_baru
    if efek_baru != "": s["efek"] = efek_baru
    if jumlah_baru.isdigit(): s["jumlah"] = int(jumlah_baru)

    print("Data berhasil diubah!")
    input("Enter untuk kembali...")

#Hapus sinergi
def hapus_sinergi():
    clear_screen()
    if not data_sinergi:
        print("Tidak ada data untuk dihapus.")
        input("Enter untuk kembali...")
        return

    id_hapus = input("Masukkan ID sinergi yang ingin dihapus: ")
    if id_hapus.isdigit() and int(id_hapus) in data_sinergi:
        del data_sinergi[int(id_hapus)]
        print("Data berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")
    input("Enter untuk kembali...")

#Login User
def login(username, password):
    if username in akun and akun[username] == password:
        return True
    else:
        return False

#Register
def register():
    clear_screen()
    global akun
    print("=== Register Akun ===")
    user_baru = input("Masukkan username baru: ")
    pass_baru = input("Masukkan password: ")

    if user_baru in akun:
        print("Username sudah digunakan!")
    else:
        akun[user_baru] = pass_baru
        print("Registrasi berhasil!")

    input("Enter untuk kembali...")

#Login
def menu_login():
    clear_screen()
    global login_user
    print("=== Login ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = input("Username: ")
        pw = input("Password: ")
        if login(user, pw):
            login_user = user
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
menu_login()