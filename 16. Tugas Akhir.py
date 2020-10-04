def cetakData(data):
    for i in data:
        for j in i:
            print(j, end="| ")
        print()
    print()


def urutkanData(data):
    while True:
        print("Metode pengurutan:\n1. Ascending\n2. Descending")
        metode = int(input("Pilih metode: "))
        if not (1 <= metode <= 2):
            print("Metode tersebut tidak ada")
            continue
        print("Urutkan berdasarkan:\n1. Skala Prioritas\n2. Nama Tugas\n3. Tanggal")
        urutan = int(input("Pilihan anda: "))
        if not (1 <= urutan <= 2):
            print("Silahkan pilih yang tersedia.")
            continue
        elif metode == 1:
            for i in range(len(data) - 1, 0, -1):
                for j in range(1, i):
                    if data[j][urutan - 1] > data[j + 1][urutan - 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
            break
        else:
            for i in range(len(data) - 1, 0, -1):
                for j in range(1, i):
                    if data[j][urutan - 1] < data[j + 1][urutan - 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
            break


def tambahkanData(data):
    skala = input("Masukkan skala prioritas(1 paling tinggi): ")
    nama = input("Masukkan nama tugas: ")
    deadline = input("Masukkan deadline tugas dalam bentuk DD/MM/YYYY: ")
    tampung = []
    tampung.append(skala)
    tampung.append(nama)
    tampung.append(deadline)
    data.append(tampung)


def hapusData(data):
    key = input("masukkan nama tugas yang ingin dihapus: ")
    for i in range(len(data)):
        if data[i][1].lower() == key.lower():
            data = data.pop(i)
            print("data berhasil dihapus")
            break


data = [
    ["Skala Prioritas", "Nama Tugas", "Deadline(DD/MM/YYYY)"],
    ["2", "Rangkuman PKn", "22/05/2020"],
    ["1", "Latihan Matematika Diskrit", "13/06/2020"],
]
while True:
    print(
        """
Selamat datang di program Pendataan Tugas
Fitur:
1. Lihat semua data
2. Urutkan data
3. Tambahkan Data
4. Hapus Data
5. Keluar Program
"""
    )
    fitur = int(input("Masukkan fitur: "))
    if fitur == 1:
        cetakData(data)
    elif fitur == 2:
        urutkanData(data)
    elif fitur == 3:
        tambahkanData(data)
    elif fitur == 4:
        hapusData(data)
    elif fitur == 5:
        break
    else:
        print("Fitur tidak tersedia")
