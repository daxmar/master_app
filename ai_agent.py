from datetime import datetime
from pathlib import Path


def _join_list(items: list[str]) -> str:
    if len(items) == 0:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " dan " + items[-1]


class AIWriter:
    @staticmethod
    def build_notes(metadata: dict) -> str:
        theme_list = _join_list(metadata["themes"])
        sample_file = metadata['files'][0] if metadata['files'] else 'src/'
        lines = [
            f"# Catatan AI Agent untuk {metadata['title']}",
            "",
            f"Tanggal pembuatan: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC",
            "",
            f"Ide utama: gabungan tema {theme_list}.",
            f"Bahasa utama: {metadata['language']['name']}.",
            "",
            "## Fokus eksperimen",
            "- Eksplorasi ide prototipe dengan struktur ringkas.",
            "- Pastikan output bisa dimodifikasi menjadi aplikasi nyata.",
            "- Tetap sederhana agar mudah dikembangkan besok.",
            "",
            "## Rekomendasi selanjutnya",
            f"1. Evaluasi apakah ide ini mendukung pengalaman pengguna praktis.",
            f"2. Tambahkan dokumentasi tambahan jika kamu ingin mengubahnya menjadi produk.",
            f"3. Jika memilih {metadata['language']['name']}, mulai dari file `{sample_file}`.",
            "",
            "## Catatan teknis",
            f"- Tema gabungan ini cocok untuk prototype kreatif atau eksperimen UI/UX.",
            f"- Jika ingin membuat antarmuka, tambahkan front-end HTML/CSS/JS terpisah.",
            "",
            "## Ide pengembangan lanjutan",
            "- Tambahkan dashboard kecil untuk mengendalikan fitur utama.",
            "- Integrasikan data sederhana untuk memberi makna pada fitur.",
            "- Buat versi mobile atau CLI apabila sesuai.",
        ]
        return "\n".join(lines)

    @staticmethod
    def suggest_stack(metadata: dict) -> str:
        language = metadata["language"]["name"]
        if language.lower() == "python":
            return "Gunakan virtual environment, requests untuk API, dan streamlit atau tkinter untuk prototipe UI."
        if language.lower() == "javascript":
            return "Gunakan Node.js untuk backend atau browser JS dengan HTML/CSS untuk prototipe frontend."
        if language.lower() == "go":
            return "Gunakan Go untuk utilitas CLI atau server ringan."
        return "Gunakan bahasa ini untuk membuat prototype sederhana sebelum memperluas menjadi produk."