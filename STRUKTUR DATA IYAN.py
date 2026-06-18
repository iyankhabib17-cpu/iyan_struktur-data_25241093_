# ==========================================================
# TUGAS: APLIKASI MANAJEMEN NILAI MAHASISWA
# Nama : Dwi Yan Sahadi
# NIM  : 25241093
# ==========================================================

# List awal data mahasiswa sesuai contoh struktur data tugas
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

while True:
    # Menampilkan Menu Utama
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    
    pilihan = input("Pilih menu 1-8: ")
    print("====================================")

    # 1. TAMPILKAN DATA
    if pilihan == "1":
        print("\n--- DAFTAR DATA MAHASISWA ---")
        if not data_mahasiswa:
            print("Data mahasiswa masih kosong!")
        else:
            print(f"{'No':<5}{'Nama Mahasiswa':<20}{'Nilai':<5}")
            print("-" * 30)
            for i, mhs in enumerate(data_mahasiswa, 1):
                print(f"{i:<5}{mhs[0]:<20}{mhs[1]:<5}")

    # 2. TAMBAH DATA
    elif pilihan == "2":
        print("\n--- TAMBAH DATA MAHASISWA ---")
        nama = input("Masukkan nama mahasiswa: ")
        # Validasi input nilai agar berupa angka
        try:
            nilai = float(input("Masukkan nilai mahasiswa: "))
            data_mahasiswa.append([nama, nilai])
            print(f"Data {nama} berhasil ditambahkan!")
        except ValueError:
            print("Gagal! Nilai harus berupa angka.")

    # 3. UBAH DATA
    elif pilihan == "3":
        print("\n--- UBAH DATA MAHASISWA ---")
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ")
        ditemukan = False
        
        for mhs in data_mahasiswa:
            # Menggunakan .lower() agar pencarian tidak sensitif huruf besar/kecil
            if mhs[0].lower() == nama_cari.lower():
                print(f"Data lama ditemukan: {mhs[0]} - Nilai: {mhs[1]}")
                nama_baru = input("Masukkan nama baru: ")
                try:
                    nilai_baru = float(input("Masukkan nilai baru: "))
                    mhs[0] = nama_baru
                    mhs[1] = nilai_baru
                    print("Data mahasiswa berhasil diperbarui!")
                except ValueError:
                    print("Gagal! Nilai harus berupa angka.")
                ditemukan = True
                break
        
        if not ditemukan:
            print(f"Data dengan nama '{nama_cari}' tidak ditemukan.")

    # 4. HAPUS DATA
    elif pilihan == "4":
        print("\n--- HAPUS DATA MAHASISWA ---")
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        ditemukan = False
        
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_hapus.lower():
                data_mahasiswa.remove(mhs)
                print(f"Data mahasiswa atas nama '{nama_hapus}' berhasil dihapus.")
                ditemukan = True
                break
                
        if not ditemukan:
            print(f"Data dengan nama '{nama_hapus}' tidak ditemukan.")

    # 5. CARI DATA
    elif pilihan == "5":
        print("\n--- CARI DATA MAHASISWA ---")
        keyword = input("Masukkan nama yang ingin dicari: ")
        ditemukan = False
        
        print(f"\nHasil pencarian untuk '{keyword}':")
        print(f"{'No':<5}{'Nama Mahasiswa':<20}{'Nilai':<5}")
        print("-" * 30)
        
        no = 1
        for mhs in data_mahasiswa:
            # Menggunakan keyword in mhs[0] agar pencarian bersifat fleksibel (substring)
            if keyword.lower() in mhs[0].lower():
                print(f"{no:<5}{mhs[0]:<20}{mhs[1]:<5}")
                no += 1
                ditemukan = True
                
        if not ditemukan:
            print("Data tidak ditemukan.")

    # 6. URUTKAN DATA BERDASARKAN NILAI (TERTINGGI)
    elif pilihan == "6":
        print("\n--- URUTKAN DATA (NILAI TERTINGGI) ---")
        if not data_mahasiswa:
            print("Data kosong, tidak bisa mengurutkan.")
        else:
            # key=lambda x: x[1] digunakan untuk mengambil elemen nilai (indeks 1) sebagai acuan shorting
            # reverse=True digunakan untuk mengurutkan dari besar ke kecil (descending)
            data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
            print("Data berhasil diurutkan berdasarkan nilai tertinggi!")
            # Otomatis menampilkan data setelah diurutkan
            print(f"\n{'No':<5}{'Nama Mahasiswa':<20}{'Nilai':<5}")
            print("-" * 30)
            for i, mhs in enumerate(data_mahasiswa, 1):
                print(f"{i:<5}{mhs[0]:<20}{mhs[1]:<5}")

    # 7. HITUNG RATA-RATA NILAI
    elif pilihan == "7":
        print("\n--- HITUNG RATA-RATA NILAI ---")
        if not data_mahasiswa:
            print("Data kosong, rata-rata adalah 0.")
        else:
            total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
            rata_rata = total_nilai / len(data_mahasiswa)
            print(f"Jumlah Mahasiswa : {len(data_mahasiswa)}")
            print(f"Total Nilai      : {total_nilai}")
            print(f"Rata-rata Nilai  : {rata_rata:.2f}")

    # 8. KELUAR
    elif pilihan == "8":
        print("\nTerima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
        break

    # ANTISIPASI PILIHAN DI LUAR MENU 1-8
    else:
        print("\nPilihan tidak valid! Silakan masukkan angka menu 1 sampai 8.")
        