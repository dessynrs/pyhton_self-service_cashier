# import 
import pandas as pd
import numpy as np

# ====================================================
# def transaksi
def start():
    "Fungsi inisialisasi program cashier sederhana"

    print("-" * 48)
    print(" ","*" * 7,"SELF-SERVICE CASHIER Register","*" * 7," ")
    print("-" * 48)
    
    print("Feature")
    print("1 - Ya")

    print("\n"* 3)
    print("-" * 48)

    start = int(input("Apakah Anda ingin memulai? (ketik 1 jika ya)\nPilihan : "))
    
    if start == 1:
        self_service_cashier()      
    else:
        print("Silahkan mengetik '1' untuk masuk dalam self-service cashier register.")
        start()


# ====================================================
def self_service_cashier():
    "Fungsi self-service cashier beserta feature-feature yg tersedia di dalamnya."

    print("-" * 48)
    print(" ","*" * 7,"SELF-SERVICE CASHIER Register","*" * 7," ")
    print("-" * 48)

    print("""\nFeature
    1 - Add to cart
    2 - Update item : product name
    3 - Update item : quantity
    4 - Update item : price
    5 - Delete item
    6 - Reset transaction
    7 - Check order
    8 - Check out
    9 - CLOSE
    """)
    
    print("-" * 48)

    feature_menu = int(input("Enter task no : "))

    if feature_menu == 1:
        add_item()

    elif feature_menu == 2:
        update_item_name()
    elif feature_menu == 3:
        update_item_qty()
    elif feature_menu == 4:
        update_item_price()

    elif feature_menu == 5:
        delete_item()
    elif feature_menu == 6:
        reset_transaction()

    elif feature_menu == 7:
        check_order()
    elif feature_menu == 8:
        check_out()

    elif feature_menu == 9:
        pass
    else:
        "Silahkan ulangi proses dan sesuaikan input sesuai kebutuhan."

# ====================================================
def transaction():
    "Fungsi untuk membuat ID transaksi setiap customer, bersifat unik"
    
    import uuid
    import random
    rd = random.Random()
    rd.seed(random.randint(1, 1000))
    
    random_uuid = uuid.UUID(int=rd.getrandbits(128))
    #list_belanjaan = []
    trnsct_123 = random_uuid
    return trnsct_123


# ====================================================
# define nilai awal list_belanjaan
list_belanjaan = []

def add_item():
    "Fungsi inisialisasi menambahkan belanjaan."

    def add_to_cart(jumlah_jenis_belanjaan):
        "Fungsi untuk menambahkan belanjaan."
        for i in range(jumlah_jenis_belanjaan):        
            nama_item = input("Masukkan produk yang ingin dibeli : ")
            jumlah_item = int(input("Masukkan jumlah produk yang ingin dibeli : "))
            harga_per_item = float(input("Masukkan harga per item produk yang ingin dibeli : Rp "))

            add_to_cart = [nama_item, jumlah_item, harga_per_item]
            list_belanjaan.append(add_to_cart)
            
        # display cart
        df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
        df.index = np.arange(1, len(df) + 1)
        df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
        
        
        print("Isi cart :")
        print(df)
        print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")

        return list_belanjaan, self_service_cashier()
    
    # memanggil fungsi 
    jumlah_jenis_belanjaan = int(input("Berapa jumlah jenis produk? "))
    add_to_cart(jumlah_jenis_belanjaan)

    return list_belanjaan
    
    
# ====================================================
def update_item_name():
    "Fungsi inisialisasi update nama produk."

    def update_detail(nama_item, nama_item_baru):
        "Fungsi untuk melakukan perubahan pada nama produk"
        
        for i in range(len(list_belanjaan)):
            nama = list_belanjaan[i][0]
            if nama == nama_item:
                list_belanjaan[i][0] = list_belanjaan[i][0].replace(nama_item, nama_item_baru)
        return list_belanjaan
    
    # memanggil fungsi
    nama_item = input("Masukkan nama produk yg ingin diganti : ")
    nama_item_baru = input("Masukkan nama produk pengganti : ")
    update_detail(nama_item, nama_item_baru)
    
    # display update cart
    df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df.index = np.arange(1, len(df) + 1)
    df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
    
    print("Isi cart (hasil revisi nama) :")
    print(df)
    print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")

    return list_belanjaan, self_service_cashier()


# ====================================================
def update_item_qty():
    "Fungsi inisialisasi update qty produk."

    def update_detail(nama_item, update_jumlah_item):
        "Fungsi untuk melakukan perubahan pada qty produk"
        
        for i in range(len(list_belanjaan)):
            if nama_item == list_belanjaan[i][0]:
                list_belanjaan[i][1] = update_jumlah_item
        return list_belanjaan
    
    # memanggil fungsi
    nama_item = input("Masukkan nama produk yg jumlahnya ingin diganti : ")
    update_jumlah_item = int(input("Masukkan jumlah produk yg benar : "))
    update_detail(nama_item, update_jumlah_item)
    
    # display update cart
    df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df.index = np.arange(1, len(df) + 1)
    df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
    
    print("Isi cart (hasil revisi qty) :")
    print(df)
    print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")

    return list_belanjaan, self_service_cashier()


# ====================================================
def update_item_price():
    "Fungsi inisialisasi update harga produk."
    def update_detail(nama_item, update_harga_per_item):
        "Fungsi untuk melakukan perubahan pada harga produk"
        
        for i in range(len(list_belanjaan)):
            if nama_item == list_belanjaan[i][0]:
                list_belanjaan[i][2] = update_harga_per_item
        return list_belanjaan
    
    # memanggil fungsi
    nama_item = input("Masukkan nama produk yg harganya ingin diganti : ")
    update_harga_per_item = int(input("Masukkan harga produk yg benar : "))
    update_detail(nama_item, update_harga_per_item)
    
    # display update cart
    df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df.index = np.arange(1, len(df) + 1)
    df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
    
    #print(f"No input {transaction()}")
    print("Isi cart (hasil revisi harga) :")
    print(df)
    print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")

    return list_belanjaan, self_service_cashier()


# ====================================================
def delete_item():
    "Fungsi inisialisasi delete."

    def update_detail(item_yg_didelete):
        "Fungsi menghapus salah satu produk dalam keranjang."
        for i in range(len(list_belanjaan)):
            if list_belanjaan[i][0] == item_yg_didelete:
                list_belanjaan.remove(list_belanjaan[i])
                break
        return list_belanjaan
    
    # memanggil fungsi
    item_yg_didelete = input("Masukkan nama produk yang ingin dihapus : ")
    update_detail(item_yg_didelete)
    
    # display update cart
    df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df.index = np.arange(1, len(df) + 1)
    df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
    
    print("Isi cart (setelah proses delete) :")
    print(df)
    print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")

    return list_belanjaan, self_service_cashier()


# ====================================================
def reset_transaction():
    "Fungsi menghapus seluruh produk pada keranjang."

    yakin = input("Apakah Anda yakin akan menghapus semua produk pada keranjang? (ya / tidak) ").lower()
    
    if yakin == "ya":
        list_belanjaan.clear()
        print("Tidak ada produk di dalam keranjang.\nSilahkan melakukan penambahan produk pada menu awal.")
    
    elif yakin == "tidak":
        
        df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
        df.index = np.arange(1, len(df) + 1)
        df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']
        
        print("Isi cart saat ini :")
        print(df)
        print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")
    
    else:
        print("Harap sesuaikan jawaban dg pertanyaan. Silahkan ulangi proses.")

    return list_belanjaan, self_service_cashier()


# ====================================================

def check_order():
    "Fungsi melakukan pengecekan akhir sebelum order diproses check out."

    df = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df.index = np.arange(1, len(df) + 1)
    df['total_belanja'] = df['jumlah_item'] * df['harga_per_item']

    print("Isi cart :")
    print(df)
    print(f"\nTotal belanja Rp {np.sum(df['total_belanja'])}")
    print("-" * 48)
    print("Lakukan check out untuk mengetahui harga akhir yang harus Anda bayarkan.")
    print("Diskon berlaku untuk pembelian lebih dari Rp 200_000 per item.\n")

    print("Apakah pesanan sudah benar? \n")
    print("Feature")
    print("1 - Ya")

    print("\n"* 3)
    print("-" * 48)
    check_order = int(input("Silahkan memilih 1 untuk melanjutkan.\nPilihan : "))
    
    if check_order == 1:
        print("\nPesanan sudah benar.")
        check_out()
    else:
        print("\nSilahkan kembali ke fitur lain untuk melengkapi / mengupdate pesanan Anda")
        self_service_cashier()

    return list_belanjaan


# ====================================================
def delivery():
    "Fungsi menjalankan database customer utk pembelian delivery ke alamat customer."
    
    # melakukan input database jika fungsi delivery dijalankan
    nama = input("Nama customer : ")
    alamat = input("Alamat customer : ")
    kota = input("Kota / Kabupaten : ")
    kode_pos = input("Kode pos : ")
    telepon = input("No telepon : ")
    no_transaksi = str(transaction())

    print("\nSilahkan periksa detail Anda: ")
    print("-" * 48)
    print(f"    Nama customer : {nama}")
    print(f"    Alamat customer : {alamat}")
    print(f"    Kota / Kabupaten : {kota}")
    print(f"    Kode pos: {kode_pos}")
    print(f"    No telepon : {telepon}")
    print(f"    No transaksi : {no_transaksi}")
    print("-" * 48,"\n")

    
    # masukkan dalam database menggunakan sqlite3
    import sqlite3 
    con = sqlite3.connect("order_super_cashier.db")
    cur = con.cursor()

    # sql table = tabel customer delivery
    cur.execute("""CREATE TABLE IF NOT EXISTS customer_super_cashier(
                id_customer INTEGER PRIMARY KEY,
                nama TEXT NOT NULL, 
                alamat TEXT NOT NULL, 
                kota TEXT NOT NULL,
                kode_pos TEXT NOT NULL,
                telepon TEXT NOT NULL,
                no_transaksi TEXT NOT NULL
                )""")
    
    list_customer = [nama, alamat, kota, kode_pos, telepon, no_transaksi]

    # melakukan insert data customer delivery 
    cur.execute(f"""INSERT INTO customer_super_cashier(nama, alamat, kota, kode_pos, telepon, no_transaksi)
                VALUES (?,?,?,?,?,?)""", list_customer)
    con.commit()


# ====================================================
def check_out():
    "Fungsi check out dan memasukkan belanjaan ke database."
    
    # total harga
    list_total_harga = []
    for i in range(len(list_belanjaan)):
        total_harga = list_belanjaan[i][1] * list_belanjaan[i][2]
        list_total_harga.append(total_harga)
     
    # rules diskon per item
    DISC_200 = 0.05
    DISC_300 = 0.06
    DISC_500 = 0.07

    list_diskon = []
    for i in range(len(list_total_harga)):
        if list_total_harga[i] > 500_000:
            disc = list_total_harga[i] * DISC_500
        elif list_total_harga[i] > 300_000:
            disc = list_total_harga[i] * DISC_300
        elif list_total_harga[i] > 200_000:
            disc = list_total_harga[i] * DISC_200
        else:
            disc = 0
        list_diskon.append(disc)
    
    # concantenate dataframe  
    df1 = pd.DataFrame(list_belanjaan, columns = ['nama_item', 'jumlah_item', 'harga_per_item'])
    df2 = pd.DataFrame(list_total_harga, columns = ['total_harga'])
    df3 = pd.DataFrame(list_diskon, columns = ['diskon'])
    
    df_checkout = pd.concat([df1, df2, df3], axis = 1)

    df_checkout['harga_setelah_diskon'] = df_checkout['total_harga'] - df_checkout['diskon']
    df_checkout['kode_transaksi'] = str(transaction())
    
    df_checkout.index = np.arange(1, len(df_checkout) + 1)

    # membantasi view dataframe
    df_checkout_copy = df_checkout[['nama_item', 'jumlah_item', 'harga_per_item', 
                                    'total_harga', 'diskon', 'harga_setelah_diskon']]

    # display check order
    no_transaksi = transaction()
    print(f"\nNo input transaksi : {no_transaksi}")

    print("-" * 48)
    print("Isi cart final :")
    print(df_checkout_copy)
    
    print("\n")
    print("-" * 48)
    print(f"Total belanja Rp {round(np.sum(df_checkout['total_harga']),2)}.\nAnda mendapat diskon sebesar Rp {round(np.sum(df_checkout['diskon']),2)}.")
    print(f"Total harga yang harus Anda bayarkan (setelah diskon) sebesar Rp {round(np.sum(df_checkout['harga_setelah_diskon']),2)}.")

    # is_delivery
    print("-" * 48)
    print("Apakah Anda ingin mengirimkan pesanan ini ke alamat Anda?\n")  
    print("0 - Tidak perlu, saya bawa pulang sendiri")
    print("1 - Ya, saya ingin delivery ke alamat saya\n\n")
    print("-" * 48)

    is_delivery = int(input("Silahkan masukkan pilihan (0/1) : "))

    if is_delivery == 0:
        print(f"\nSilahkan melakukan pembayaran. Total belanja Anda setelah diskon Rp {np.sum(df_checkout['harga_setelah_diskon'])}")
        print("-" * 48)
        print("\nTerima kasih telah berbelanja. Tuhan memberkati.")

    elif is_delivery == 1:
        print(f"\nSilahkan melakukan pengisian alamat kirim dan penghitungan ongkos kirim.")
        
        # customer melakukan input data pada fungsi delivery
        delivery()

        print(f"\nSilahkan melakukan pembayaran. Total belanja Anda setelah diskon Rp {np.sum(df_checkout['harga_setelah_diskon'])}")
        print("Pesanan akan dikirimkan setelah anda melakukan pembayaran.")
        print("-" * 48)
        print("\nTerima kasih telah berbelanja. Tuhan memberkati.")

    else:
        print("Silahkan input dengan benar.")
    
    # buat database tabel transaksi & customer
    import sqlite3

    # masukkan dalam database menggunakan sqlite3
    con = sqlite3.connect("order_super_cashier.db")
    cur = con.cursor()
    
    # sql table = tabel transaction
    cur.execute("""CREATE TABLE IF NOT EXISTS transaction_super_cashier(
                nama_item TEXT NOT NULL, 
                jumlah_item REAL NOT NULL, 
                harga_per_item REAL NOT NULL,
                total_harga REAL NOT NULL,
                diskon REAL NOT NULL,
                harga_setelah_diskon REAL NOT NULL,
                kode_transaksi TEXT NOT NULL
                )""")
    
    # melakukan export dataframe transaksi ke bentuk sql
    df_checkout.to_sql('transaction_super_cashier', con, if_exists = 'append', method = None) # if exists = 'append' kalo sdh ok, bisa jg 'replace
    
    # menutup koneksi database
    con.close()