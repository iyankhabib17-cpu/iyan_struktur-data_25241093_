# kondisi
# aksi 

nama_anda = "iyan"
input_nama = input("masukan nama anda:")

if input_nama == nama_anda:

    print("jika benar akan lanjut ke program selanjutnya")

    try:
        angka = int(input("masukan angka"))

        for i in range(1,12):
            print(f"{angka} x {i} = {angka* i}")

    except valueError:
        pass
    print("program selesei")
else:
    print("silahkan coba lagi")