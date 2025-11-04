from Clearscreen import data_sinergi, clear_screen, login_user
from tampil import tampilkan_data

#Nambah Sinergi
def tambah_sinergi():
    clear_screen()
    global data_sinergi
    nama = input("Nama Sinergi: ")
    tipe = input("Tipe Sinergi: ")
    efek = input("Efek Sinergi: ")
    jumlah = input("Jumlah Hero yang dibutuhkan: ")

    if not jumlah.isdigit():
        print("Jumlah harus angka!")
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

#Ngapus sinergi
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

#Menu Utama
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

    menu_utama()