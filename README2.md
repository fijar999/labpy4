# Program Input Data Mahasiswa

Program ini digunakan untuk memasukkan data mahasiswa berupa Nama, NIM, dan nilai (Tugas, UTS, UAS) dengan validasi ketat. Setiap nilai akhir akan dihitung secara otomatis berdasarkan persentase:

* Tugas: **30%**
* UTS: **35%**
* UAS: **35%**

Data yang berhasil dimasukkan akan ditampilkan dalam bentuk tabel menggunakan karakter box-drawing sehingga menyerupai tampilan kolom data.

## Fitur Utama

* Validasi **Nama** (tidak boleh kosong dan tidak boleh mengandung angka)
* Validasi **NIM** (wajib angka)
* Validasi nilai **Tugas/UTS/UAS** (0–100 dan wajib angka)
* Perhitungan nilai akhir otomatis
* Tampilan tabel rapi tanpa warna dengan karakter border

## Cara Menjalankan

1. Jalankan program Python pada terminal atau editor.
2. Masukkan data mahasiswa sesuai instruksi.
3. Pilih untuk menambah data atau menyelesaikan input.
4. Program menampilkan tabel data mahasiswa secara otomatis.

## Output

Program menghasilkan tabel seperti berikut:

```
┌────┬──────────────┬────────┬────────┬───────┬──────┬────────┐
│ No │ Nama         │ NIM    │ Tugas  │ UTS   │ UAS  │ Akhir  │
├────┼──────────────┼────────┼────────┼───────┼──────┼────────┤
│ 1  │ Contoh Nama  │ 123456 │ 80     │ 75    │ 90   │ 82.75  │
└────┴──────────────┴────────┴────────┴───────┴──────┴────────┘
```

## Catatan

Program ini dapat dikembangkan lebih lanjut dengan menambahkan fitur seperti:

* Edit dan hapus data
* Simpan data ke file CSV atau Excel
* Sorting data berdasarkan kolom tertentu
