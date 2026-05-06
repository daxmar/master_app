# Mitos Kebiasaan Journey

Aplikasi ini adalah prototype CLI Go yang membantu melacak kebiasaan sehari-hari dengan sentuhan tema mitos dan ekologi.

## Deskripsi
Mitos Kebiasaan Journey menggabungkan kebiasaan hidup ramah lingkungan, ritual mitos alam, dan pelacakan tindakan sederhana. Aplikasi ini menyimpan kebiasaan harian dalam `habits.json`, kemudian memungkinkan kamu menandai aktivitas sebagai selesai dan menambahkan kebiasaan baru.

## Fitur
- Menampilkan daftar kebiasaan dengan status harian
- Menandai kebiasaan selesai untuk hari ini
- Menambahkan kebiasaan baru
- Menampilkan petuah mitos sebagai inspirasi
- Menyimpan data kebiasaan dalam file `habits.json`

## Persyaratan
- Go 1.20+ terpasang

## Cara Menjalankan
1. Buka terminal dalam folder `20260506_mitos-kebiasaan-journey`
2. Jalankan:
   ```sh
   go run main.go
   ```
3. Ikuti instruksi menu untuk melihat, menandai, atau menambah kebiasaan.

## File Proyek
- `main.go` - kode aplikasi utama
- `habits.json` - file data yang akan dibuat otomatis setelah pertama dijalankan
- `README.md` - dokumentasi aplikasi
- `project.json` - metadata proyek
- `ai_notes.md` - catatan AI Agent
- `web/index.html` - UI web lokal untuk melihat prosedur run dan preview proyek
