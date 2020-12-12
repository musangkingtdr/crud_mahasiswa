import mysql.connector
import os
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mahasiswa"
)

def tambah():
    cursor = db.cursor()
    os.system('cls')
    nama = input('Masukkan Nama: ')
    nim = input('Masukkan Nim (6 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        Data.tambah()
        quit()
    prodi = input('Masukkan Program Studi: ')
    j_kel = input('Pilih Jenis Kelamin (l/p): ')
    if j_kel == 'l':
        j_kel = 'Laki-laki'
    elif j_kel == 'p':
        j_kel = 'Perempuan'
    else:
        print('pilihan salah')
        Data.tambah()
        quit()
    alamat = input('Masukkan alamat: ')
    sql = "insert into data(nama,nim,prodi,j_kel,alamat) values(%s,%s,%s,%s,%s)"
    val = (nama,nim,prodi,j_kel,alamat)
    cursor.execute(sql,val)
    db.commit()
    print("Data berhasil ditambahkan")

def ubah():
    cursor = db.cursor()
    update = input('Pilih data mahasiswa yang akan diubah (berdasarkan id): ')
    os.system('cls')
    nama = input('Masukkan Nama baru: ')
    nim = input('Masukkan Nim baru (6 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        Data.tambah()
        quit()
    prodi = input('Masukkan Program Studi baru: ')
    j_kel = input('Pilih Jenis Kelamin (l/p): ')
    if j_kel == 'l':
        j_kel = 'Laki-laki'
    elif j_kel == 'p':
        j_kel = 'Perempuan'
    else:
        print('pilihan salah')
        Data.tambah()
        quit()
    alamat = input('Masukkan alamat baru: ')
    sql = "UPDATE data SET nama=%s,nim=%s,prodi=%s,j_kel=%s,alamat=%s WHERE id=%s"
    val = (nama,nim,prodi,j_kel,alamat,update)
    cursor.execute(sql,val)
    db.commit()
    print("Data berhasil diubah")

def hapus():
    cursor = db.cursor()
    delete = input('Masukkan ID Mahasiswa yang akan dihapus: ')
    sql = "DELETE FROM data WHERE id=%s" %delete
    cursor.execute(sql)
    db.commit()
    print('Data berhasil dihapus')

def menu():
    cursor = db.cursor()
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    hasil = cursor.fetchall()
    os.system('cls')
    print('======================DATA MAHASISWA==========================')
    print('ID   NAMA    NIM        PROGRAM_STUDI   JENIS_KELAMIN   ALAMAT')
    if cursor.rowcount < 0:
        print('Tidak ada data')
    else:
        for data in hasil:
            print(data)  
    print('==============================================================')
    print('DAFTAR PERINTAH')
    print('1.Tambah Data')
    print('2.Ubah Data')
    print('3.Hapus Data')
    print('0.Keluar')
    menu = input('Pilih Menu(1/2/3/0): ')

    if menu == '1':
        tambah()
    if menu == '2':
        ubah()
    if menu == '3':
        hapus()
    elif menu == '0':
        os.system('cls')
        quit()

if __name__ == "__main__":
    while(True):
        menu()
