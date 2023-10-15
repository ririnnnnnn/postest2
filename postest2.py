# tema toko furniture

print (50*"=")
print ("                   Mapple Mart")
print (50*"=")
print("hai")
print("silahkan login terlebih dahulu!")
print("1. admin")
print("2. pembeli")
print("3. keluar")
print (50*"=")

login = input("silahkan memilih pilihan login 1/2/3:")

# menu admin
if login == "1":

    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga"]
    table.add_row([1, "Lemari", 350000])
    table.add_row([2, "Sofa", 500000])
    table.add_row([3, "Rak Buku", 270000])
    table.add_row([4, "Meja Makan", 425000])
    table.add_row([5, "Tempat Tidur", 850000])
    print(table)

    # Fungsi Create
    def tambah_barang():
        No = int(input("Masukkan nomor barang: "))
        Nama_Barang = input("Masukkan nama barang: ")
        Harga = int(input("Masukkan harga barang: "))
        table.add_row([No, Nama_Barang, Harga])
        print(table)
        print("Barang telah ditambahkan.")

    # Fungsi Read
    def tampilkan_barang():
        print(table)

    # Fungsi Update
    def edit_barang():
        tampilkan_barang()
        edit_barang = int(input("Masukkan nomor barang yang ingin diperbarui: "))
        for i, row in enumerate(table._rows):
            if int(row[0]) == edit_barang:
                table._rows[i] = [row[0], input("Masukkan nama barang baru: "), int(input("Masukkan Harga baru: "))]
                print("Daftar barang telah diperbarui.")
                return
        print("Data tidak ditemukan.")

    # Fungsi Delete
    def hapus_barang():
        tampilkan_barang()
        hapus_barang = int(input("Masukkan nomor barang yang ingin dihapus: "))
        for i, row in enumerate(table._rows):
            if int(row[0]) == hapus_barang:
                table.del_row(i)
                print("Daftar barang telah dihapus.")
                return
        print("Data tidak ditemukan.")

    while True:
        print("\nMenu:")
        print("1. Tampilkan barang")
        print("2. Tambah barang")
        print("3. Edit barang")
        print("4. Hapus barang")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            tampilkan_barang()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            edit_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if login == "2":

    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga"]
    table.add_row([1, "Lemari", 350000])
    table.add_row([2, "Sofa", 500000])
    table.add_row([3, "Rak Buku", 270000])
    table.add_row([4, "Meja Makan", 425000])
    table.add_row([5, "Tempat Tidur", 850000])
    print(table)

    total = 0
    barang = []
    harga = []

    while True:
        kode = int(input("masukkan kode barang:"))
        if kode == 1:
            barang.append("Lemari")
            harga.append(350000)
            total += 350000

        elif kode == 2:
            barang.append("Sofa")
            harga.append(500000)
            total += 500000
        
        elif kode == 3:
            barang.append("Rak Buku")
            harga.append(270000)
            total += 270000
        
        elif kode == 4:
            barang.append("Meja Makan")
            harga.append(425000)
            total += 425000

        elif kode == 5:
            barang.append("Tempat Tidur")
            harga.append(850000)
            total += 850000

        else:
            print ("kode tidak tersedia")

        lanjut = input ("lanjut belanja (y/t): ")
        if lanjut == "t" :
            print ("")
            break

    print("barang yang anda beli: ", barang)
    print("harga barang yang anda beli: ", harga)
    print("total yang harus anda bayar: ", total, "\n")

    uang = int(input("masukkan nominal uang anda: "))
    if uang > total :
        print("kembalian anda: ", uang - total)

    elif uang == total :
        print ("uang anda pas")

    else:
        print("uang anda kurang: ", total - uang)

if login == 3:
    print ("anda telah keluar dari program")


print (50*"=")
print ("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
print (50*"=")