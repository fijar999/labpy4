# Program input data mahasiswa dengan validasi ketat
data_mahasiswa = []

def input_nama():
    while True:
        nama = input("Masukkan Nama         : ").strip()
        if nama == "":
            print("⚠ Nama tidak boleh kosong. Silakan isi dengan benar.")
            continue
        # cek ada angka di nama?
        if any(ch.isdigit() for ch in nama):
            print("⚠ Nama tidak boleh mengandung angka. Silakan isi nama dengan benar.")
            continue
        return nama

def input_nim():
    while True:
        nim = input("Masukkan NIM          : ").strip()
        if nim == "":
            print("⚠ NIM tidak boleh kosong. Silakan isi dengan benar.")
            continue
        if not nim.isdigit():
            print("⚠ NIM hanya boleh berisi angka (tanpa huruf/spasi). Silakan ulangi.")
            continue
        return nim

def input_nilai(label):
    while True:
        val = input(f"Masukkan Nilai {label} : ").strip()
        try:
            num = float(val)
        except ValueError:
            print(f"⚠ Nilai {label} harus berupa angka. Contoh: 85 atau 87.5")
            continue
        if not (0 <= num <= 100):
            print(f"⚠ Nilai {label} harus di antara 0 sampai 100.")
            continue
        return num

# Loop input data
while True:
    print("\n=== INPUT DATA MAHASISWA ===")
    nama = input_nama()
    nim = input_nim()
    tugas = input_nilai("Tugas")
    uts = input_nilai("UTS")
    uas = input_nilai("UAS")

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append([nama, nim, tugas, uts, uas, round(nilai_akhir, 2)])

    lagi = input("Tambah data lagi? (ya/tidak): ").strip().lower()
    if lagi != "ya":
        break

# Tampilkan tabel (box drawing). Jika tidak ada data, tampilkan pesan.
if not data_mahasiswa:
    print("\nTidak ada data mahasiswa untuk ditampilkan.")
else:
    header = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"]
    table = []
    for i, row in enumerate(data_mahasiswa, start=1):
        table.append([str(i)] + [str(x) for x in row])

    # Hitung lebar kolom (perhatikan header jika lebih panjang)
    col_count = len(header)
    col_widths = []
    for c in range(col_count):
        max_len = len(header[c])
        for r in table:
            if c < len(r):
                max_len = max(max_len, len(str(r[c])))
        col_widths.append(max_len)

    # Fungsi garis box-drawing
    def garis_atas():
        s = "┌"
        for i, w in enumerate(col_widths):
            s += "─" * (w + 2)
            s += "┬" if i < len(col_widths) - 1 else "┐"
        print(s)

    def garis_tengah():
        s = "├"
        for i, w in enumerate(col_widths):
            s += "─" * (w + 2)
            s += "┼" if i < len(col_widths) - 1 else "┤"
        print(s)

    def garis_bawah():
        s = "└"
        for i, w in enumerate(col_widths):
            s += "─" * (w + 2)
            s += "┴" if i < len(col_widths) - 1 else "┘"
        print(s)

    def cetak_baris(row):
        s = "│"
        for i, col in enumerate(row):
            s += " " + col.ljust(col_widths[i]) + " │"
        print(s)

    # Cetak tabel
    print("\n=========== DATA NILAI MAHASISWA ===========\n")
    garis_atas()
    cetak_baris(header)
    garis_tengah()
    for row in table:
        cetak_baris(row)
    garis_bawah()
