# membuat judul program
print("="*50)
print("""
    SELAMAT DATANG DI PROGRAM MENGHITUNG 
        RUMUS SEGITIGA PYTHAGORAS 
""")
print("="*50)

# memasukkan data berupa Nama, NIM, dan password
print("silahkan masukkan data anda")
while True :
    nama_1 = input("masukkan nama: ")
    nim_1 = input("masukkan nim: ")
    password_1 = input("masukkan password: ")
    print("data telah tersimpan!")

# login menggunakan data yang telah di inputkan
    print("="*20)
    print("       LOGIN")
    print("="*20)

    nama_2 = input("nama: ")
    nim_2 = input("NIM: ")
    password_2 = input("password: ")

    if  nama_2 == nama_1 and nim_2 == nim_1 and password_2 == password_1 :
        print("login berhasil!")
        break
    else : 
        print("Nama, NIM, atau Password salah. Silakan coba lagi.")

# pilihan yang bisa dipilih user
while True:
    print(20*"=")
    print("      PILIHAN  ")
    print(20*"=")
    print("1. Mencari sisi miring")
    print("2. Mencari sisi tegak")
    print("3. Mencari alas")
    print("4. Keluar ")

# mengambil pilihan dari user
    pilihan = int(input("Masukkan Pilihan anda (1/2/3/4): "))

# mencari sisi miring segitiga
    if pilihan == 1 :
        a = float(input("inputkan panjang sisi tegak = "))
        b = float(input("inputkan panjang alas       = "))
        c = float((a**2 + b**2)**0.5)
        print("sisi miring segitiga       =", c)

# mencari sisi tegak segitiga
    elif pilihan == 2 :
        a = float(input("inputkan panjang sisi miring = "))
        b = float(input("inputkan panjang alas    = "))
        c = float((c**2 - b**2)**0.5)
        print("sisi tegak segitiga           =", a)

# mencari alas segitiga
    elif pilihan == 3 :
        a = float(input("inputkan panjang sisi miring = "))
        b = float(input("inputkan panjang tegak    = "))
        c = float((c**2 - a**2)**0.5)
        print("alas segitiga          =", b)

# keluar dari program
    elif pilihan == 4:
        keluar = input("Keluar? (ya/tidak): ")
        if keluar == "ya" :
            print("Terima kasih telah menggunakan program ini")
            break
        elif keluar == "tidak" :
            continue
        else:
            print("Silakan masukkan 'ya' untuk keluar atau 'tidak' untuk kembali ke menu.")