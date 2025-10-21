import os

#Data user 
users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "user"}
}

#Data sinergi
data_sinergi = {
    1: {"nama": "Weapon Master", "tipe": "Physical", "efek": "Lifesteal 25%", "jumlah": 3},
    2: {"nama": "Mage", "tipe": "Magic", "efek": "Magic Power +30%", "jumlah": 3}
}

while True:
    os.system("cls")  # bersihkan layar
    print("=" * 40)
    print(" PROGRAM DATA SINERGI MAGIC CHESS ".center(40))
    print("=" * 40)
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    #REGISTER 
    if pilihan == '1':
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("Username sudah ada!")
        else:
            users[username] = {"password": password, "role": "user"}
            print(f"Berhasil mendaftar sebagai {username}!")
        input("Tekan Enter untuk lanjut...")

    #LOGIN
    elif pilihan == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            print(f"Selamat datang, {username}!")
            input("Tekan Enter untuk masuk...")
            os.system("cls")

            #MENU ADMIN
            if users[username]["role"] == "admin":
                while True:
                    print("=" * 40)
                    print(" MENU ADMIN - SINERGI MAGIC CHESS ".center(40))
                    print("=" * 40)
                    print("1. Tambah Sinergi")
                    print("2. Lihat Sinergi")
                    print("3. Ubah Sinergi")
                    print("4. Hapus Sinergi")
                    print("5. Logout")
                    pilih = input("Pilih: ")

                    #TAMBAH DATA
                    if pilih == '1':
                        nama = input("Nama Sinergi: ")
                        tipe = input("Tipe (Mage/Physical): ")
                        efek = input("Efek Sinergi: ")
                        jumlah = input("Jumlah Hero untuk Aktif: ")

                        if jumlah.isdigit():
                            sinergi_baru = max(data_sinergi.keys()) + 1 if data_sinergi else 1
                            data_sinergi[sinergi_baru] = {
                                "nama": nama,
                                "tipe": tipe,
                                "efek": efek,
                                "jumlah": int(jumlah)
                            }
                            print("Sinergi berhasil ditambahkan!")
                        else:
                            print("Jumlah hero harus angka!")

                    #LIHAT DATA
                    elif pilih == '2':
                        if len(data_sinergi) == 0:
                            print("Belum ada data sinergi.")
                        else:
                            for i, s in data_sinergi.items():
                                print(f"\n[{i}] {s['nama']}")
                                print(f"   Tipe   : {s['tipe']}")
                                print(f"   Efek   : {s['efek']}")
                                print(f"   Jumlah : {s['jumlah']} hero")

                    #UBAH DATA
                    elif pilih == '3':
                        id_edit = input("Masukkan sinergi yang ingin diubah: ")
                        if Sinergi_edit.isdigit():
                            Sinergi_edit = int(id_edit)
                            if Sinergi_edit in data_sinergi:
                                s = data_sinergi[Sinergi_edit]
                                print(f"Data saat ini: {s['nama']} ({s['tipe']}) - {s['efek']}")
                                nama_baru = input("Nama baru (kosong=tidak ubah): ")
                                tipe_baru = input("Tipe baru (kosong=tidak ubah): ")
                                efek_baru = input("Efek baru (kosong=tidak ubah): ")
                                jumlah_baru = input("Jumlah hero baru (kosong=tidak ubah): ")

                                if nama_baru != "": s["nama"] = nama_baru
                                if tipe_baru != "": s["tipe"] = tipe_baru
                                if efek_baru != "": s["efek"] = efek_baru
                                if jumlah_baru.isdigit(): s["jumlah"] = int(jumlah_baru)

                                print("Data sinergi berhasil diubah.")
                            else:
                                print("Sinergi tidak ditemukan.")
                        else:
                            print("Sinergi harus berupa angka!")

                    #HAPUS DATA
                    elif pilih == '4':
                        Sinergi_hapus = input("Masukkan Sinergi yang ingin dihapus: ")
                        if Sinergi_hapus.isdigit():
                            Sinergi_hapus = int(Sinergi_hapus)
                            if Sinergi_hapus in data_sinergi:
                                nama = data_sinergi[Sinergi_hapus]["nama"]
                                del data_sinergi[Sinergi_hapus]
                                print(f"Sinergi '{nama}' berhasil dihapus.")
                            else:
                                print("Sinergi tidak ditemukan.")
                        else:
                            print("Sinergi harus angka!")

                    # ===== LOGOUT =====
                    elif pilih == '5':
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")

                    input("Tekan Enter untuk lanjut...")
                    os.system("cls")

            #MENU USER
            else:
                while True:
                    print("=" * 40)
                    print(" MENU USER - LIHAT SINERGI ".center(40))
                    print("=" * 40)
                    print("1. Lihat Daftar Sinergi")
                    print("2. Logout")
                    pilih = input("Pilih: ")

                    if pilih == '1':
                        if len(data_sinergi) == 0:
                            print("Belum ada data sinergi yang tersedia.")
                        else:
                            for i, s in data_sinergi.items():
                                print(f"\n[{i}] {s['nama']}")
                                print(f"   Tipe   : {s['tipe']}")
                                print(f"   Efek   : {s['efek']}")
                                print(f"   Jumlah : {s['jumlah']} hero")

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

    #KELUAR
    elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
