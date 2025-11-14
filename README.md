# Program Input Data Mahasiswa

Program ini digunakan untuk memasukkan data mahasiswa berupa Nama, NIM, dan sekaligus menghitung nilai Tugas, UTS, UAS secara otomatis:

* Tugas: **30%**
* UTS: **35%**
* UAS: **35%**

Hasil akhir perhitungan akan muncul otomatis dan langsung terdaftar dalam kolom  

## Fitur Utama

* Keterangan **Nama** (tidak boleh kosong dan tidak boleh mengandung angka)
* Keterangan **NIM** (wajib angka)
* Keterangan nilai **Tugas/UTS/UAS** (0–100 dan wajib angka)
* Perhitungan nilai akhir otomatis dan langsung masuk kedalam kolom  

## Cara Menjalankan

1. Jalankan program Python pada terminal atau editor.
2. Masukkan data mahasiswa sesuai instruksi.
3. Pilih untuk menambah data atau menyelesaikan input.
4. Program menampilkan tabel data mahasiswa secara otomatis.

## Output

Hasil akhir akan muncul seperti pada tabel berikut:

`=========== DATA NILAI MAHASISWA ===========

┌────┬───────┬───────────┬───────┬──────┬──────┬───────┐
│ No │ Nama  │ NIM       │ Tugas │ UTS  │ UAS  │ Akhir │
├────┼───────┼───────────┼───────┼──────┼──────┼───────┤
│ 1  │ fijar │ 312510227 │ 80.0  │ 85.0 │ 88.0 │ 84.55 │
└────┴───────┴───────────┴───────┴──────┴──────┴───────┘
```

## Catatan

- Bobot Nilai: Tugas 30%, UTS 35%, UAS 35%  
- Data Sementara: Data hanya tersimpan selama program berjalan  
- Range Nilai: Disarankan input 0-100