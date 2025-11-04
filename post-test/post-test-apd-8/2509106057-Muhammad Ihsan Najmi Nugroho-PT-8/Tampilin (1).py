from Clearscreen import data_sinergi, clear_screen
from prettytable import PrettyTable

#Tampilkan Data
def tampilkan_data():
    clear_screen()
    print("=== Daftar Sinergi Magic Chess ===")

    if not data_sinergi:
        print("Belum ada data sinergi.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Tipe", "Efek", "Jumlah"]
        for id, s in data_sinergi.items():
            tabel.add_row([id, s['nama'], s['tipe'], s['efek'], s['jumlah']])
        print(tabel)

    input("\nTekan Enter untuk kembali...")