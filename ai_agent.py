from datetime import datetime
from pathlib import Path
import random


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

    @staticmethod
    def generate_basic_code(metadata: dict) -> str:
        language_key = metadata["language"]["key"]
        title = metadata["title"]
        themes = metadata["themes"]

        if language_key == "python":
            return f"""# {title}
# Prototype aplikasi dengan tema: {', '.join(themes)}

def main():
    print(f"Running {title}")
    print(f"Tema: {', '.join(themes)}")
    # Tambahkan logika dasar aplikasi di sini

if __name__ == "__main__":
    main()
"""
        elif language_key == "javascript":
            return f"""// {title}
// Prototype aplikasi dengan tema: {', '.join(themes)}

console.log(`Running {title}`);
console.log(`Tema: {', '.join(themes)}`);
// Tambahkan logika dasar aplikasi di sini
"""
        elif language_key == "go":
            return f"""package main

import "fmt"

// {title}
// Prototype aplikasi dengan tema: {', '.join(themes)}

func main() {{
    fmt.Println("Running {title}")
    fmt.Println("Tema: {', '.join(themes)}")
    // Tambahkan logika dasar aplikasi di sini
}}
"""
        elif language_key == "html":
            return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>Tema: {', '.join(themes)}</p>
    <p>Prototype aplikasi HTML dasar.</p>
</body>
</html>
"""
        elif language_key == "rust":
            return f"""fn main() {{
    println!("Running {title}");
    println!("Tema: {{}}", "{', '.join(themes)}");
    // Tambahkan logika dasar aplikasi di sini
}}
"""
        else:
            return f"# {title}\n# Prototype aplikasi dengan tema: {', '.join(themes)}\n# Tambahkan kode dasar di sini"

    @staticmethod
    def generate_full_features(metadata: dict) -> str:
        language_key = metadata["language"]["key"]
        title = metadata["title"]
        themes = metadata["themes"]

        # Simulasi fitur lengkap berdasarkan tema
        features = []
        if "Kesehatan" in themes:
            features.append("Pelacakan kesehatan harian")
        if "Produktivitas" in themes:
            features.append("Manajemen tugas")
        if "IoT" in themes:
            features.append("Koneksi perangkat IoT")
        if "AI" in themes:
            features.append("Rekomendasi AI")
        if "Musik" in themes:
            features.append("Pemutar musik")
        if "Game" in themes:
            features.append("Mini game")
        if not features:
            features = ["Fitur dasar aplikasi", "Pengaturan pengguna", "Dashboard sederhana"]

        if language_key == "python":
            code = f"""# {title}
# Aplikasi lengkap dengan fitur: {', '.join(features)}

import json
import os

class {title.replace(' ', '')}App:
    def __init__(self):
        self.title = "{title}"
        self.themes = {themes}
        self.features = {features}
        self.data_file = "app_data.json"

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {{}}

    def save_data(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def run_feature(self, feature_name):
        print(f"Menjalankan fitur: {{feature_name}}")
        # Implementasi fitur di sini

    def main_menu(self):
        while True:
            print(f"\\n=== {{self.title}} ===")
            print("Fitur tersedia:")
            for i, feature in enumerate(self.features, 1):
                print(f"{{i}}. {{feature}}")
            print("0. Keluar")
            choice = input("Pilih fitur: ")
            if choice == "0":
                break
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.features):
                    self.run_feature(self.features[idx])
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan angka.")

if __name__ == "__main__":
    app = {title.replace(' ', '')}App()
    app.main_menu()
"""
            return code

        elif language_key == "javascript":
            code = f"""// {title}
// Aplikasi lengkap dengan fitur: {', '.join(features)}

class {title.replace(' ', '')}App {{
    constructor() {{
        this.title = "{title}";
        this.themes = {themes};
        this.features = {features};
        this.dataFile = "app_data.json";
    }}

    loadData() {{
        try {{
            const data = localStorage.getItem(this.dataFile);
            return data ? JSON.parse(data) : {{}};
        }} catch (e) {{
            return {{}};
        }}
    }}

    saveData(data) {{
        localStorage.setItem(this.dataFile, JSON.stringify(data));
    }}

    runFeature(featureName) {{
        console.log(`Menjalankan fitur: ${{featureName}}`);
        // Implementasi fitur di sini
    }}

    mainMenu() {{
        while (true) {{
            console.log(`\\n=== ${{this.title}} ===`);
            console.log("Fitur tersedia:");
            this.features.forEach((feature, i) => {{
                console.log(`${{i + 1}}. ${{feature}}`);
            }});
            console.log("0. Keluar");
            const choice = prompt("Pilih fitur: ");
            if (choice === "0") break;
            const idx = parseInt(choice) - 1;
            if (idx >= 0 && idx < this.features.length) {{
                this.runFeature(this.features[idx]);
            }} else {{
                console.log("Pilihan tidak valid.");
            }}
        }}
    }}
}}

const app = new {title.replace(' ', '')}App();
app.main_menu();
"""
            return code

        elif language_key == "go":
            themes_list = [f'"{t}"' for t in themes]
            features_list = [f'"{f}"' for f in features]
            themes_str = ", ".join(themes_list)
            features_str = ", ".join(features_list)
            code = f"""package main

import (
    "encoding/json"
    "fmt"
    "os"
)

// {title}
// Aplikasi lengkap dengan fitur: {', '.join(features)}

type {title.replace(' ', '')}App struct {{
    Title    string
    Themes   []string
    Features []string
    DataFile string
}}

func New{title.replace(' ', '')}App() *{title.replace(' ', '')}App {{
    return &{title.replace(' ', '')}App{{
        Title:    "{title}",
        Themes:   []string{{{themes_str}}},
        Features: []string{{{features_str}}},
        DataFile: "app_data.json",
    }}
}}

func (app *{title.replace(' ', '')}App) LoadData() map[string]interface{{}} {{
    data := make(map[string]interface{{}})
    if file, err := os.Open(app.DataFile); err == nil {{
        defer file.Close()
        json.NewDecoder(file).Decode(&data)
    }}
    return data
}}

func (app *{title.replace(' ', '')}App) SaveData(data map[string]interface{{}}) {{
    if file, err := os.Create(app.DataFile); err == nil {{
        defer file.Close()
        json.NewEncoder(file).Encode(data)
    }}
}}

func (app *{title.replace(' ', '')}App) RunFeature(featureName string) {{
    fmt.Printf("Menjalankan fitur: %s\\n", featureName)
    // Implementasi fitur di sini
}}

func (app *{title.replace(' ', '')}App) MainMenu() {{
    for {{
        fmt.Printf("\\n=== %s ===\\n", app.Title)
        fmt.Println("Fitur tersedia:")
        for i, feature := range app.Features {{
            fmt.Printf("%d. %s\\n", i+1, feature)
        }}
        fmt.Println("0. Keluar")
        var choice int
        fmt.Print("Pilih fitur: ")
        fmt.Scan(&choice)
        if choice == 0 {{
            break
        }}
        if choice > 0 && choice <= len(app.Features) {{
            app.RunFeature(app.Features[choice-1])
        }} else {{
            fmt.Println("Pilihan tidak valid.")
        }}
    }}
}}

func main() {{
    app := New{title.replace(' ', '')}App()
    app.MainMenu()
}}
"""
            return code

        elif language_key == "rust":
            themes_list = [f'"{t}".to_string()' for t in themes]
            features_list = [f'"{f}".to_string()' for f in features]
            themes_str = ", ".join(themes_list)
            features_str = ", ".join(features_list)
            code = f"""// {title}
// Aplikasi lengkap dengan fitur: {', '.join(features)}

use std::collections::HashMap;
use std::fs;
use serde::{{Deserialize, Serialize}};

#[derive(Serialize, Deserialize)]
struct {title.replace(' ', '')}App {{
    title: String,
    themes: Vec<String>,
    features: Vec<String>,
    data_file: String,
}}

impl {title.replace(' ', '')}App {{
    fn new() -> Self {{
        Self {{
            title: "{title}".to_string(),
            themes: vec![{themes_str}],
            features: vec![{features_str}],
            data_file: "app_data.json".to_string(),
        }}
    }}

    fn load_data(&self) -> HashMap<String, serde_json::Value> {{
        if let Ok(contents) = fs::read_to_string(&self.data_file) {{
            if let Ok(data) = serde_json::from_str(&contents) {{
                data
            }} else {{
                HashMap::new()
            }}
        }} else {{
            HashMap::new()
        }}
    }}

    fn save_data(&self, data: &HashMap<String, serde_json::Value>) {{
        if let Ok(json) = serde_json::to_string_pretty(data) {{
            let _ = fs::write(&self.data_file, json);
        }}
    }}

    fn run_feature(&self, feature_name: &str) {{
        println!("Menjalankan fitur: {{}}", feature_name);
        // Implementasi fitur di sini
    }}

    fn main_menu(&self) {{
        loop {{
            println!("\\n=== {{}} ===", self.title);
            println!("Fitur tersedia:");
            for (i, feature) in self.features.iter().enumerate() {{
                println!("{{}}. {{}}", i + 1, feature);
            }}
            println!("0. Keluar");
            let mut input = String::new();
            std::io::stdin().read_line(&mut input).unwrap();
            let choice: usize = match input.trim().parse() {{
                Ok(num) => num,
                Err(_) => continue,
            }};
            if choice == 0 {{
                break;
            }}
            if choice > 0 && choice <= self.features.len() {{
                self.run_feature(&self.features[choice - 1]);
            }} else {{
                println!("Pilihan tidak valid.");
            }}
        }}
    }}
}}

fn main() {{
    let app = {title.replace(' ', '')}App::new();
    app.main_menu();
}}
"""
            return code

        elif language_key == "html":
            code = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .feature {{ margin: 10px 0; padding: 10px; border: 1px solid #ccc; }}
        button {{ padding: 10px; margin: 5px; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>Tema: {', '.join(themes)}</p>
    <p>Fitur tersedia:</p>
    <div id="features">
        {''.join(f'<div class="feature"><h3>{feature}</h3><button onclick="runFeature(\'{feature}\')">Jalankan</button></div>' for feature in features)}
    </div>
    <script>
        function runFeature(featureName) {{
            alert(`Menjalankan fitur: ${{featureName}}`);
            // Implementasi fitur di sini
        }}
    </script>
</body>
</html>
"""
            return code

        else:
            return f"# {title}\n# Aplikasi lengkap dengan fitur: {', '.join(features)}\n# Implementasi lengkap di sini"

    @staticmethod
    def generate_ui_prototype(metadata: dict) -> str:
        title = metadata["title"]
        themes = metadata["themes"]
        features = []
        if "Kesehatan" in themes:
            features.append("Pelacakan kesehatan harian")
        if "Produktivitas" in themes:
            features.append("Manajemen tugas")
        if "IoT" in themes:
            features.append("Koneksi perangkat IoT")
        if "AI" in themes:
            features.append("Rekomendasi AI")
        if "Musik" in themes:
            features.append("Pemutar musik")
        if "Game" in themes:
            features.append("Mini game")
        if not features:
            features = ["Fitur dasar aplikasi", "Pengaturan pengguna", "Dashboard sederhana"]

        # Generate HTML UI prototype
        feature_buttons = "".join(
            f'<button onclick="runFeature(\'{feature}\')" class="feature-btn">{feature}</button>'
            for feature in features
        )

        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Prototype UI</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .features {{
            padding: 30px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }}
        .feature-btn {{
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 20px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            font-weight: 500;
        }}
        .feature-btn:hover {{
            background: #007bff;
            color: white;
            border-color: #007bff;
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,123,255,0.3);
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
            min-height: 200px;
        }}
        .output h3 {{
            margin-top: 0;
            color: #495057;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            white-space: pre-wrap;
            font-family: monospace;
        }}
        .footer {{
            background: #343a40;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>Prototype UI - Tema: {', '.join(themes)}</p>
        </div>
        <div class="features">
            {feature_buttons}
        </div>
        <div class="output">
            <h3>Output</h3>
            <div class="output-content" id="outputContent">
                Klik salah satu fitur di atas untuk melihat hasilnya.
            </div>
        </div>
    </div>
    <div class="footer">
        <p>Generated by Master APP AI Agent - {datetime.utcnow().strftime('%Y-%m-%d')}</p>
    </div>

    <script>
        function runFeature(featureName) {{
            const output = document.getElementById('outputContent');
            output.textContent = `Menjalankan fitur: ${{featureName}}\\n\\n`;

            // Simulate feature execution based on name
            if (featureName.includes('kesehatan')) {{
                output.textContent += '📊 Data kesehatan hari ini:\\n- Langkah: 8,432\\n- Kalori: 2,150\\n- Tidur: 7.5 jam\\n\\n💡 Saran: Jaga pola makan!';
            }} else if (featureName.includes('tugas')) {{
                output.textContent += '📝 Daftar tugas:\\n1. Meeting pukul 10:00\\n2. Review kode\\n3. Update dokumentasi\\n\\n✅ Tugas selesai: 2/3';
            }} else if (featureName.includes('IoT')) {{
                output.textContent += '🔗 Status perangkat IoT:\\n- Lampu ruang tamu: ON\\n- AC kamar: 24°C\\n- Kamera depan: Active\\n\\n🔄 Sinkronisasi data...';
            }} else if (featureName.includes('AI')) {{
                output.textContent += '🤖 Rekomendasi AI:\\nBerdasarkan pola penggunaan Anda:\\n- Waktu produktif terbaik: 09:00-11:00\\n- Saran: Istirahat 5 menit setiap jam\\n- Motivasi: "Kecil tapi konsisten!"';
            }} else if (featureName.includes('musik')) {{
                output.textContent += '🎵 Pemutar musik:\\nNow playing: "Ocean Waves" - Nature Sounds\\n⏯️ Status: Playing\\n🔊 Volume: 70%\\n\\n▶️ ▐▐▐▐▐▐▐▐▐▐ 45:30';
            }} else if (featureName.includes('game')) {{
                output.textContent += '🎮 Mini Game - Tebak Angka\\nSaya pikir angka antara 1-100...\\nTebakan Anda: ?\\n\\n💡 Petunjuk: Angka tersebut genap dan > 50';
            }} else {{
                output.textContent += `Fitur "${{featureName}}" berhasil dijalankan!\\n\\nIni adalah simulasi prototype.\\nFitur lengkap akan diimplementasikan dalam versi final.`;
            }}
        }}

        // Auto-run first feature on load
        window.onload = function() {{
            const firstBtn = document.querySelector('.feature-btn');
            if (firstBtn) {{
                firstBtn.click();
            }}
        }};
    </script>
</body>
</html>"""