# Catatan AI Agent untuk Mitos Kebiasaan Journey

Tanggal pembuatan: 2026-05-06T01:10:37.886Z

Ide utama: gabungan tema Kebiasaan, Mitos, Eko.
Bahasa utama: Go.

## Fokus eksperimen
- Aplikasi ini sekarang menjadi prototype CLI Go untuk kebiasaan dan ritual lingkungan.
- Data tersimpan di `habits.json` ketika kamu menjalankan `go run main.go`.
- Fokus utamanya adalah membuat kebiasaan kecil terasa seperti ritual mitos.

## Rekomendasi selanjutnya
1. Jalankan `go run main.go` untuk melihat daftar kebiasaan dan menandai kegiatan harian.
2. Tambahkan lebih banyak ritual kebiasaan dengan menekan menu "Tambah kebiasaan baru".
3. Jika ingin memperluas, buat antarmuka web atau mobile untuk menampilkan kabar mitos dalam tampilan visual.

## Perubahan teknis yang dibuat
- Menambahkan `main.go` dengan logika CLI, data persistence, dan menu interaktif.
- `habits.json` akan dibuat otomatis di folder proyek saat pertama kali dijalankan.
- Contoh kebiasaan awal meliputi: minum air cukup, bawa tas kain, tanam tanaman kecil.

## Ide pengembangan lanjutan
- Tambahkan mode harian dengan statistik dan progress streak.
- Buat versi web sederhana menggunakan HTML/CSS/JS untuk menyajikan ritual mitos secara visual.
- Tautkan kebiasaan ke dampak eko dengan poin atau skor hijau.
