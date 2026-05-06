# Master APP Planning

## 1. Tujuan Proyek
Master APP adalah sistem generator proyek aplikasi yang:
- Memilih ide unik atau abstrak secara otomatis.
- Menghasilkan aplikasi baru setiap hari.
- Mengemas hasil dalam folder baru setiap kali dijalankan.
- Menggunakan berbagai bahasa pemrograman untuk setiap aplikasi.
- Memiliki tema-tema yang saling silang dan bisa dicampur.
- Mencakup AI Agent sebagai pembantu perencanaan dan eksekusi.

## 2. Konsep Utama
1. **Generator Ide**
   - Menghasilkan ide aplikasi berdasarkan kombinasi tema, gaya, fungsi, dan abstraksi.
   - Ide dapat berupa aplikasi utilitas, hiburan, pendidikan, sosial, atau eksperimen kreatif.

2. **Multi-Bahasa**
   - Setiap proyek baru dapat menggunakan satu atau beberapa bahasa pemrograman.
   - Target bahasa mencakup bahasa populer, bahasa scripting, dan bahasa untuk prototyping.

3. **Tema Silang**
   - Tema dibangun agar bisa saling berinteraksi.
   - Contoh: "Kebugaran + Horor + IoT" atau "Jurnal + AI + Musik".

4. **AI Agent Pendamping**
   - Agent membantu memilih ide, membuat struktur folder, menulis README, dan memberi saran teknis.
   - Agent juga bisa menjadi asisten progres harian atau saran pengembangan.

## 3. Daftar Bahasa Pemrograman
1. JavaScript / TypeScript
2. Python
3. Go
4. Rust
5. Kotlin
6. Dart
7. Swift
8. Java
9. Ruby
10. PHP
11. C#
12. C++
13. Lua
14. Haskell
15. R
16. HTML/CSS (frontend / static)
17. Shell scripting (bash / PowerShell)
18. SQL
19. Solidity
20. Julia

> Prioritas implementasi awal: JavaScript/TypeScript, Python, Go, Rust, Dart, dan HTML/CSS.

## 4. Daftar Tema Aplikasi
Tema-tema berikut dibangun agar mudah dikombinasikan:

### 4.1 Tema Inti
- Produktivitas
- Edukasi
- Hiburan
- Kesehatan
- Sosial
- Kreativitas
- Keuangan
- Musik
- Seni
- Game
- Data
- Komunikasi
- IoT
- Alam
- Kebiasaan
- Waktu
- Keamanan
- Kebudayaan
- Bahasa
- Eksperimen

### 4.2 Tema Tambahan / Abstrak
- Alam bawah sadar
- Mimpi
- Horor
- Retro
- Minimalis
- Futuristik
- Steampunk
- Fantasi
- Cyberpunk
- Meditasi
- Sains
- Komedi
- Paradox
- Makhluk
- Urban
- Kosmik
- Ritual
- Mitos
- Fragmented
- Koneksi

### 4.3 Contoh Kombinasi Tema
- `Produktivitas + Horor + AI`
- `Edukasi + Musik + Retro`
- `Kesehatan + IoT + Minimalis`
- `Seni + Data + Futuristik`
- `Game + Kebiasaan + Cyberpunk`
- `Komunikasi + Meditasi + Paradox`
- `Kreativitas + Alam bawah sadar + AR`

## 5. Arsitektur Master APP

### 5.1 Komponen Utama
1. `master-app-core`
   - Penyusun ide
   - Algoritma pemilihan bahasa
   - Generator struktur folder
   - Template README / dokumentasi

2. `theme-engine`
   - Penyimpanan tema dan aturan silang
   - Generator kombinasi tema unik

3. `language-selector`
   - Memilih bahasa terbaik berdasarkan ide tema dan jenis aplikasi
   - Mendukung multi-bahasa dalam satu proyek

4. `app-generator`
   - Membuat folder baru dengan nama proyek
   - Menghasilkan file awal (README, manifest, contoh kode, placeholder)
   - Menyertakan konfigurasi build / dependency

5. `ai-assistant`
   - Agent untuk diskusi ide
   - Menyediakan ringkasan proyek
   - Memberi rekomendasi teknologi dan arsitektur

6. `scheduler`
   - Menjalankan generator secara harian atau on-demand
   - Dapat di-trigger manual setiap kali ingin membuat proyek baru

### 5.2 Struktur Folder Proyek Master APP
```
master_app/
  ├─ src/
  │   ├─ core/
  │   ├─ themes/
  │   ├─ languages/
  │   ├─ generator/
  │   ├─ ai_agent/
  │   └─ scheduler/
  ├─ templates/
  │   ├─ js/
  │   ├─ python/
  │   ├─ go/
  │   ├─ rust/
  │   └─ common/
  ├─ output/            # folder hasil proyek harian
  ├─ data/
  │   ├─ themes.json
  │   ├─ language_profiles.json
  │   ├─ idea_patterns.json
  │   └─ app_types.json
  ├─ README.md
  ├─ config.json
  └─ run_generator.(js|py)
```

### 5.3 Alur Eksekusi
1. `run_generator` memanggil `scheduler` atau mode manual.
2. `theme-engine` menghasilkan kombinasi tema.
3. `core` menyusun judul dan deskripsi aplikasi.
4. `language-selector` menentukan bahasa/bahasa yang cocok.
5. `app-generator` membuat folder baru di `output/`.
6. `ai-assistant` menghasilkan README, fitur utama, dan daftar todo.
7. Proyek siap dikembangkan atau diuji.

## 6. Mekanisme Folder Harian

### 6.1 Nama Folder
Gunakan pola nama yang unik dan bermakna:
- `YYYYMMDD_<tema_utama>_<kata_kunci>`
- Contoh: `20260506_hiburan_retro_player`
- Atau ide abstrak: `20260506_mimpi_paradox`

### 6.2 Isi Folder
Setiap folder proyek berisi:
- `README.md` dengan deskripsi ide dan instruksi awal.
- `project.json` atau `manifest.yaml` yang mendokumentasikan bahasa, tema, fitur, dan file penting.
- `src/` atau `app/` dengan file awal dari template.
- `assets/` bila diperlukan untuk frontend atau media.
- `scripts/` untuk build, run, atau deploy sederhana.
- `ai_notes.md` yang berisi catatan AI Agent.

### 6.3 Contoh Output Harian
```
output/
  ├─ 20260506_hiburan_retro_player/
  │   ├─ README.md
  │   ├─ project.json
  │   ├─ src/
  │   │   ├─ index.js
  │   │   └─ style.css
  │   └─ ai_notes.md
  ├─ 20260507_kesehatan_iot_meditasi/
  │   ├─ README.md
  │   ├─ project.json
  │   ├─ main.py
  │   └─ ai_notes.md
  └─ ...
```

## 7. Rincian AI Agent

### 7.1 Peran AI Agent
- Membantu memilih ide ketika banyak opsi tersedia.
- Menyusun dokumentasi ide dan feature list.
- Memberikan rekomendasi bahasa dan template.
- Menyajikan ringkasan cepat untuk developer yang ingin melanjutkan.
- Dapat bertindak sebagai asisten obrolan dalam CLI.

### 7.2 Fitur AI Agent
- `generate_idea()` : Buat ide aplikasi dari tema gabungan.
- `explain_project()` : Ringkasan tujuan, fitur, dan cara pakai.
- `suggest_stack()` : Rekomendasi bahasa/framework berdasarkan kebutuhan.
- `write_readme()` : Buat README awal dengan struktur.
- `plan_next_steps()` : Daftar pengembangan atau TODO.

### 7.3 Implementasi Agent
- Bisa berbasis template prompt sederhana.
- Untuk versi lokal: gunakan model open-source (mis. Ollama, local LLM) atau integrasi API.
- Versi lanjutan: agent internal yang mengambil input pengguna dan memberi saran.

## 8. Rencana Fase Pengembangan

### Fase 1: Desain dan Setup Dasar
- Buat struktur folder Master APP.
- Definisikan tema, bahasa, dan pola ide.
- Buat generator folder harian sederhana.
- Siapkan template awal untuk 3 bahasa.

### Fase 2: Generator Ide dan Tema Silang
- Buat engine tema yang menggabungkan 2-3 tema.
- Tambahkan aturan untuk membuat ide abstrak dan menarik.
- Buat daftar template nama proyek dan deskripsi dasar.

### Fase 3: Output Proyek Otomatis
- Implementasikan generator proyek yang membuat folder dan file.
- Pastikan setiap output berisi README, manifest, dan satu entry point.
- Tambahkan mekanisme tanggal dan versi.

### Fase 4: AI Agent
- Bangun modul AI Agent untuk membantu pembuatan ide dan dokumentasi.
- Integrasikan dalam CLI / runner.
- Tambahkan file catatan AI untuk tiap proyek output.

### Fase 5: Penjadwalan dan Eksekusi Harian
- Tambahkan mode `daily` untuk membuat proyek baru setiap hari.
- Pilih opsi `manual` atau `auto`.
- Tambahkan logging hasil dan ringkasan output.

## 9. Contoh Ide Proyek Unik
1. `Aplikasi Jurnal Suara Mimpi` (Python + HTML): rekam teks mimpi dengan UI suara.
2. `Permainan Ritme Kebiasaan` (Dart/Flutter + data): game mobile yang mengubah kebiasaan.
3. `Peringatan IoT Nostalgia` (Go + Rust): notifikasi harian dengan tema retro.
4. `Peta Emosi Kota` (JavaScript + data): visualisasi suasana kota real-time.
5. `Asisten Ritual Meditasi` (Kotlin + AI): reminder meditasi dengan soundtrack.

## 10. Rekomendasi Awal Teknologi
- `Node.js` atau `Python` untuk core Master APP.
- `JSON` / `YAML` untuk konfigurasi tema dan template.
- `Git` untuk melacak output generator bila perlu.
- `CLI sederhana` untuk menjalankan generator: `npm run generate`, `python run_generator.py`.

## 11. Kriteria Sukses
- Setiap kali dijalankan, muncul folder baru berisi aplikasi unik.
- Nama, tema, bahasa, dan deskripsi otomatis tercatat.
- AI Agent menyediakan dokumentasi dan rekomendasi teknis.
- Tema bisa digabung secara silang untuk menghasilkan ide kreatif.
- Proyek bisa digunakan sebagai prototype atau eksperimen nyata.

## 12. Langkah Selanjutnya
1. Putuskan bahasa dasar untuk Master APP (`JavaScript/TypeScript` atau `Python`).
2. Buat file `data/themes.json` dan `data/languages.json`.
3. Buat modul generator ide awal.
4. Buat run script untuk membuat folder `output/YYYYMMDD_*`.
5. Tambahkan AI Agent placeholder untuk README dan catatan.

---

Dengan dokumen ini, proyek Master APP sudah memiliki kerangka lengkap, daftar bahasa, tema, arsitektur, dan strategi agar bisa menghasilkan aplikasi berbeda setiap hari.
