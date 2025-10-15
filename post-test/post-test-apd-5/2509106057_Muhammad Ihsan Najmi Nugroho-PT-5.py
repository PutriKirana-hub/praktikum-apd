import os

users = {
    "admin": {"password": "admin"},
    "user": {"password": "user"}
}

data_sinergi = []

while True:
    os.system("cls")  # bersihkan layar (untuk Windows)
    print("="*40)
    print(" PROGRAM DATA SINERGI MAGIC CHESS ".center(40))
    print("="*40)
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("Username sudah ada!")
        else:
            users[username] = {"password": password}
            print(f"Berhasil mendaftar sebagai {username}!")
        input("Tekan Enter untuk lanjut...")

    elif pilihan == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            print(f"Selamat datang, {username}!")
            input("Tekan Enter untuk masuk...")
            os.system("cls")

            if username == "admin":
                while True:
                    print("="*40)
                    print(" MENU ADMIN - SINERGI MAGIC CHESS ".center(40))
                    print("="*40)
                    print("1. Tambah Sinergi")
                    print("2. Lihat Sinergi")
                    print("3. Ubah Sinergi")
                    print("4. Hapus Sinergi")
                    print("5. Logout")
                    pilih = input("Pilih: ")

                    if pilih == '1':
                        nama = input("Nama Sinergi: ")
                        tipe = input("Tipe (Mage/Pysical?): ")
                        efek = input("Efek Sinergi: ")
                        jumlah = input("Jumlah Hero untuk Aktif: ")
                        data_sinergi.append([nama, tipe, efek, jumlah])
                        print("Sinergi berhasil ditambahkan!")

                    elif pilih == '2':
                        if len(data_sinergi) == 0:
                            print("Belum ada data sinergi.")
                        else:
                            for i in range(len(data_sinergi)):
                                print(f"\n[{i+1}] {data_sinergi[i][0]}")
                                print(f"   Tipe   : {data_sinergi[i][1]}")
                                print(f"   Efek   : {data_sinergi[i][2]}")
                                print(f"   Jumlah : {data_sinergi[i][3]} hero")

                    elif pilih == '3':
                        nama = input("Masukkan nama sinergi yang ingin diubah: ")
                        ditemukan = False
                        for i in range(len(data_sinergi)):
                            if data_sinergi[i][0] == nama:
                                ditemukan = True
                                nama_baru = input("Nama baru: ")
                                tipe_baru = input("Tipe baru: ")
                                efek_baru = input("Efek baru: ")
                                jumlah_baru = input("Jumlah hero baru: ")
                                data_sinergi[i] = [nama_baru, tipe_baru, efek_baru, jumlah_baru]
                                print("Data sinergi berhasil diubah.")
                                break
                        if not ditemukan:
                            print("Sinergi tidak ditemukan.")

                    elif pilih == '4':
                        nama = input("Masukkan nama sinergi yang ingin dihapus: ")
                        ditemukan = False
                        for i in range(len(data_sinergi)):
                            if data_sinergi[i][0] == nama:
                                del data_sinergi[i]
                                print(f"Sinergi {nama} berhasil dihapus.")
                                ditemukan = True
                                break
                        if not ditemukan:
                            print("Sinergi tidak ditemukan.")

                    elif pilih == '5':
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")

                    input("Tekan Enter untuk lanjut...")
                    os.system("cls")

            else:
                while True:
                    print("="*40)
                    print(" MENU USER - LIHAT SINERGI ".center(40))
                    print("="*40)
                    print("1. Lihat Daftar Sinergi")
                    print("2. Logout")
                    pilih = input("Pilih: ")

                    if pilih == '1':
                        if len(data_sinergi) == 0:
                            print("Belum ada data sinergi yang tersedia.")
                        else:
                            for i in range(len(data_sinergi)):
                                print(f"\n[{i+1}] {data_sinergi[i][0]}")
                                print(f"   Tipe   : {data_sinergi[i][1]}")
                                print(f"   Efek   : {data_sinergi[i][2]}")
                                print(f"   Jumlah : {data_sinergi[i][3]} hero")

                    elif pilih == '2':
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid!")

                    input("Tekan Enter untuk lanjut...")
                    os.system("cls")
        else:
            print("Login gagal, username atau password salah.")
            input("Tekan Enter untuk lanjut...")

    elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
