# Master APP

Sebuah sistem generator aplikasi harian yang menghasilkan ide unik secara otomatis dan membuat proyek baru setiap kali dijalankan.

## Fitur
- Menghasilkan ide aplikasi berdasarkan kombinasi tema dan gaya abstrak
- Memilih bahasa pemrograman secara dinamis
- Membuat folder proyek baru dengan nama tanggal unik
- Menyediakan `README.md`, `project.json`, dan `ai_notes.md` setiap output
- Memiliki modul AI Agent untuk mendokumentasikan dan menyarankan stack

## Menjalankan
1. Pastikan Python 3.10+ terpasang
2. Jalankan:
   ```sh
   python run_generator.py
   ```
   - Generator akan menampilkan ide aplikasi dan meminta persetujuan.
   - Jika kamu setuju, folder akan dibuat otomatis dan file akan dimasukkan ke dalamnya.
3. Untuk mode langsung tanpa konfirmasi:
   ```sh
   python run_generator.py --auto
   ```
4. Untuk mode manual dengan nama khusus:
   ```sh
   python run_generator.py --name "projek-unik"
   ```
5. Output akan dibuat di `output/`

## Struktur Proyek
- `run_generator.py` : entrypoint generator
- `ai_agent.py` : modul bantu AI Agent
- `data/` : tema, bahasa, pola ide
- `output/` : hasil proyek
- `web/` : UI web statis untuk preview generator

## UI Web Statis
Buka `web/index.html` di browser untuk melihat preview ide aplikasi, tema, bahasa, dan generate file README/project.json/ai_notes.md secara langsung.
- Setiap aplikasi yang dibuat juga akan berisi `web/index.html` di folder aplikasinya untuk melihat UI dan prosedur run lokal.

## Tujuan
Master APP harus menjadi basis eksperimen kreatif di mana setiap eksekusi menghasilkan aplikasi baru, ide baru, dan peluang eksplorasi multi-bahasa.
