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

        # Determine UI type based on theme combinations
        ui_type = "generic"
        primary_theme = themes[0] if themes else "Generic"

        # Define specific UI layouts based on theme combinations
        if "Kesehatan" in themes and "Neural" in themes:
            ui_type = "health_neural"
        elif "Game" in themes and "Ritme" in themes:
            ui_type = "rhythm_game"
        elif "Musik" in themes and "AI" in themes:
            ui_type = "ai_music"
        elif "IoT" in themes and "Produktivitas" in themes:
            ui_type = "iot_productivity"
        elif "Kesehatan" in themes:
            ui_type = "health"
        elif "Game" in themes:
            ui_type = "game"
        elif "Musik" in themes:
            ui_type = "music"
        elif "AI" in themes:
            ui_type = "ai"
        elif "IoT" in themes:
            ui_type = "iot"

        # Generate specific UI content based on type
        if ui_type == "health_neural":
            return AIWriter._generate_health_neural_ui(title, themes)
        elif ui_type == "rhythm_game":
            return AIWriter._generate_rhythm_game_ui(title, themes)
        elif ui_type == "ai_music":
            return AIWriter._generate_ai_music_ui(title, themes)
        elif ui_type == "iot_productivity":
            return AIWriter._generate_iot_productivity_ui(title, themes)
        elif ui_type == "health":
            return AIWriter._generate_health_ui(title, themes)
        elif ui_type == "game":
            return AIWriter._generate_game_ui(title, themes)
        elif ui_type == "music":
            return AIWriter._generate_music_ui(title, themes)
        elif ui_type == "ai":
            return AIWriter._generate_ai_ui(title, themes)
        elif ui_type == "iot":
            return AIWriter._generate_iot_ui(title, themes)
        else:
            return AIWriter._generate_generic_ui(title, themes)

    @staticmethod
    def _generate_generic_ui(title: str, themes: list) -> str:
        features = ["Fitur dasar aplikasi", "Pengaturan pengguna", "Dashboard sederhana"]
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
            output.textContent = `Menjalankan fitur: ${{featureName}}\\n\\nIni adalah simulasi prototype.\\nFitur lengkap akan diimplementasikan dalam versi final.`;
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_health_neural_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Neural Health Tracker</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .metric-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border: 2px solid #e9ecef;
        }}
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            color: #007bff;
        }}
        .brain-wave {{
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
        }}
        .controls {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        button {{
            background: #28a745;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #218838;
            transform: translateY(-2px);
        }}
        .output {{
            padding: 30px;
            background: white;
        }}
        .output-content {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 {title}</h1>
            <p>Neural Health & Wellness Tracker - Tema: {', '.join(themes)}</p>
        </div>

        <div class="dashboard">
            <div class="metric-card">
                <h3>Stress Level</h3>
                <div class="metric-value" id="stressLevel">45%</div>
                <p>Normal range</p>
            </div>
            <div class="metric-card">
                <h3>Focus Score</h3>
                <div class="metric-value" id="focusScore">78%</div>
                <p>Good concentration</p>
            </div>
            <div class="metric-card">
                <h3>Sleep Quality</h3>
                <div class="metric-value" id="sleepQuality">8.2h</div>
                <p>Excellent rest</p>
            </div>
            <div class="metric-card">
                <h3>Mood Index</h3>
                <div class="metric-value" id="moodIndex">85%</div>
                <p>Positive state</p>
            </div>
        </div>

        <div class="brain-wave">
            <h3>🧠 Real-time Neural Activity</h3>
            <div id="brainActivity">Monitoring brain waves... Alpha: 12Hz | Beta: 18Hz | Theta: 6Hz</div>
        </div>

        <div class="controls">
            <button onclick="startMeditation()">🧘 Start Meditation</button>
            <button onclick="runBreathing()">🫁 Breathing Exercise</button>
            <button onclick="checkMood()">😊 Mood Check</button>
            <button onclick="generateReport()">📊 Generate Report</button>
        </div>

        <div class="output">
            <h3>Activity Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to Neural Health Tracker! Click any button above to begin.
            </div>
        </div>
    </div>

    <script>
        let meditationTimer = null;
        let breathingCycle = 0;

        function startMeditation() {{
            const output = document.getElementById('outputContent');
            output.textContent = '🧘 Starting meditation session...\\n\\n';
            let timeLeft = 300; // 5 minutes
            meditationTimer = setInterval(() => {{
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                output.textContent = `🧘 Meditation in progress...\\nTime remaining: ${{minutes}}:${{seconds.toString().padStart(2, '0')}}\\n\\nFocus on your breath. Neural activity stabilizing...`;
                timeLeft--;
                if (timeLeft < 0) {{
                    clearInterval(meditationTimer);
                    output.textContent += '\\n\\n✅ Meditation complete! Stress level decreased by 15%.';
                    updateMetrics();
                }}
            }}, 1000);
        }}

        function runBreathing() {{
            const output = document.getElementById('outputContent');
            breathingCycle++;
            output.textContent = `🫁 Breathing Exercise #${{breathingCycle}}\\n\\n`;
            output.textContent += 'Inhale deeply... (4 seconds)\\nHold... (4 seconds)\\nExhale slowly... (6 seconds)\\n\\n💡 Neural feedback: Heart rate synchronized with breathing pattern.';
        }}

        function checkMood() {{
            const output = document.getElementById('outputContent');
            const moods = ['Happy 😊', 'Calm 😌', 'Focused 🎯', 'Energetic ⚡', 'Relaxed 🧘'];
            const randomMood = moods[Math.floor(Math.random() * moods.length)];
            output.textContent = `😊 Current Mood Assessment\\n\\nBased on neural patterns: ${{randomMood}}\\n\\nAI Recommendation: Continue with positive activities to maintain this state.`;
        }}

        function generateReport() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📊 Daily Neural Health Report\\n\\n`;
            output.textContent += `Date: ${{new Date().toLocaleDateString()}}\\n`;
            output.textContent += `Average Stress Level: 42% (↓8% from yesterday)\\n`;
            output.textContent += `Focus Sessions: 3 completed\\n`;
            output.textContent += `Sleep Quality: Excellent\\n`;
            output.textContent += `Neural Patterns: Balanced brain activity\\n\\n`;
            output.textContent += `💡 AI Insight: Your neural health is improving! Keep up the good work.`;
        }}

        function updateMetrics() {{
            const stress = Math.max(30, parseInt(document.getElementById('stressLevel').textContent) - Math.floor(Math.random() * 10));
            const focus = Math.min(95, parseInt(document.getElementById('focusScore').textContent) + Math.floor(Math.random() * 5));
            document.getElementById('stressLevel').textContent = stress + '%';
            document.getElementById('focusScore').textContent = focus + '%';
        }}

        // Simulate real-time updates
        setInterval(() => {{
            const activity = document.getElementById('brainActivity');
            const alpha = (10 + Math.random() * 5).toFixed(1);
            const beta = (15 + Math.random() * 10).toFixed(1);
            const theta = (4 + Math.random() * 4).toFixed(1);
            activity.textContent = `Monitoring brain waves... Alpha: ${{alpha}}Hz | Beta: ${{beta}}Hz | Theta: ${{theta}}Hz`;
        }}, 3000);
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_rhythm_game_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Rhythm Game</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .game-area {{
            padding: 30px;
            text-align: center;
        }}
        .rhythm-buttons {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
        }}
        .rhythm-btn {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            border: none;
            font-size: 2em;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .rhythm-btn:active {{
            transform: scale(0.95);
        }}
        .red {{ background: #ff4757; }}
        .blue {{ background: #3742fa; }}
        .green {{ background: #2ed573; }}
        .yellow {{ background: #ffa502; }}
        .score-display {{
            font-size: 2em;
            margin: 20px 0;
            font-weight: bold;
        }}
        .controls {{
            padding: 20px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        button {{
            background: #007bff;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #0056b3;
            transform: translateY(-2px);
        }}
        .output {{
            padding: 30px;
            background: white;
        }}
        .output-content {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎵 {title}</h1>
            <p>Rhythm Game Experience - Tema: {', '.join(themes)}</p>
        </div>

        <div class="game-area">
            <div class="score-display">
                Score: <span id="score">0</span> | Combo: <span id="combo">0</span>
            </div>

            <div class="rhythm-buttons">
                <button class="rhythm-btn red" onclick="hitButton('red')">🔴</button>
                <button class="rhythm-btn blue" onclick="hitButton('blue')">🔵</button>
                <button class="rhythm-btn green" onclick="hitButton('green')">🟢</button>
                <button class="rhythm-btn yellow" onclick="hitButton('yellow')">🟡</button>
            </div>

            <div id="rhythmSequence"></div>
        </div>

        <div class="controls">
            <button onclick="startGame()">🎮 Start Game</button>
            <button onclick="stopGame()">⏹️ Stop</button>
            <button onclick="changeDifficulty()">⚙️ Difficulty</button>
            <button onclick="showStats()">📊 Stats</button>
        </div>

        <div class="output">
            <h3>Game Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to Rhythm Game! Click "Start Game" to begin your musical journey.
            </div>
        </div>
    </div>

    <script>
        let score = 0;
        let combo = 0;
        let gameActive = false;
        let sequence = [];
        let currentStep = 0;
        let difficulty = 'normal';

        function startGame() {{
            if (gameActive) return;
            gameActive = true;
            score = 0;
            combo = 0;
            currentStep = 0;
            sequence = [];
            updateDisplay();
            const output = document.getElementById('outputContent');
            output.textContent = '🎵 Game started! Follow the rhythm pattern...\\n\\n';
            generateSequence();
            playSequence();
        }}

        function stopGame() {{
            gameActive = false;
            const output = document.getElementById('outputContent');
            output.textContent += '\\n\\n⏹️ Game stopped. Final Score: ' + score;
        }}

        function generateSequence() {{
            const length = difficulty === 'easy' ? 4 : difficulty === 'hard' ? 8 : 6;
            const colors = ['red', 'blue', 'green', 'yellow'];
            sequence = [];
            for (let i = 0; i < length; i++) {{
                sequence.push(colors[Math.floor(Math.random() * colors.length)]);
            }}
        }}

        function playSequence() {{
            let step = 0;
            const interval = setInterval(() => {{
                if (step >= sequence.length) {{
                    clearInterval(interval);
                    document.getElementById('outputContent').textContent += '\\n\\n🎯 Your turn! Repeat the sequence.';
                    return;
                }}
                flashButton(sequence[step]);
                step++;
            }}, 800);
        }}

        function flashButton(color) {{
            const btn = document.querySelector(`.${{color}}`);
            btn.style.transform = 'scale(1.2)';
            setTimeout(() => {{
                btn.style.transform = 'scale(1)';
            }}, 300);
        }}

        function hitButton(color) {{
            if (!gameActive) return;

            const output = document.getElementById('outputContent');
            if (currentStep < sequence.length) {{
                if (color === sequence[currentStep]) {{
                    combo++;
                    score += 10 * combo;
                    output.textContent += `✅ Hit! Combo: ${{combo}}\\n`;
                    currentStep++;
                    if (currentStep >= sequence.length) {{
                        output.textContent += `\\n🎉 Sequence complete! +${{10 * combo}} points\\n`;
                        setTimeout(() => {{
                            generateSequence();
                            currentStep = 0;
                            playSequence();
                        }}, 2000);
                    }}
                }} else {{
                    combo = 0;
                    score = Math.max(0, score - 20);
                    output.textContent += `❌ Miss! Combo broken.\\n`;
                    currentStep = 0;
                    setTimeout(() => playSequence(), 1500);
                }}
                updateDisplay();
            }}
        }}

        function changeDifficulty() {{
            const difficulties = ['easy', 'normal', 'hard'];
            const currentIndex = difficulties.indexOf(difficulty);
            difficulty = difficulties[(currentIndex + 1) % difficulties.length];
            document.getElementById('outputContent').textContent = `⚙️ Difficulty changed to: ${{difficulty.toUpperCase()}}\\n\\nEasy: 4 notes\\nNormal: 6 notes\\nHard: 8 notes`;
        }}

        function showStats() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📊 Game Statistics\\n\\n`;
            output.textContent += `Current Score: ${{score}}\\n`;
            output.textContent += `Best Combo: ${{combo}}\\n`;
            output.textContent += `Difficulty: ${{difficulty}}\\n`;
            output.textContent += `Games Played: 1\\n`;
            output.textContent += `Accuracy: ${{((score / Math.max(1, score + 20)) * 100).toFixed(1)}}%\\n`;
        }}

        function updateDisplay() {{
            document.getElementById('score').textContent = score;
            document.getElementById('combo').textContent = combo;
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_ai_music_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AI Music Composer</title>
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
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .composer {{
            padding: 30px;
        }}
        .controls {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .control-group {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }}
        .slider {{
            width: 100%;
            margin: 10px 0;
        }}
        button {{
            background: #007bff;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #0056b3;
            transform: translateY(-2px);
        }}
        .play-btn {{
            background: #28a745;
            font-size: 1.2em;
            padding: 15px 30px;
        }}
        .play-btn:hover {{
            background: #218838;
        }}
        .piano {{
            display: flex;
            justify-content: center;
            margin: 30px 0;
            flex-wrap: wrap;
        }}
        .key {{
            width: 40px;
            height: 120px;
            background: white;
            border: 1px solid #ccc;
            margin: 0 2px;
            cursor: pointer;
            border-radius: 0 0 5px 5px;
            transition: all 0.1s ease;
        }}
        .key:active {{
            background: #e9ecef;
            transform: scale(0.98);
        }}
        .black-key {{
            width: 25px;
            height: 80px;
            background: black;
            color: white;
            position: relative;
            z-index: 1;
            margin-left: -12px;
            margin-right: -12px;
            border-radius: 0 0 3px 3px;
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎼 {title}</h1>
            <p>AI-Powered Music Composer - Tema: {', '.join(themes)}</p>
        </div>

        <div class="composer">
            <div class="controls">
                <div class="control-group">
                    <h3>🎵 Genre</h3>
                    <select id="genre" style="width: 100%; padding: 8px; border-radius: 5px;">
                        <option>Jazz</option>
                        <option>Classical</option>
                        <option>Electronic</option>
                        <option>Ambient</option>
                        <option>Rock</option>
                    </select>
                </div>
                <div class="control-group">
                    <h3>🎼 Tempo</h3>
                    <input type="range" id="tempo" class="slider" min="60" max="180" value="120">
                    <div id="tempoValue">120 BPM</div>
                </div>
                <div class="control-group">
                    <h3>🎹 Complexity</h3>
                    <input type="range" id="complexity" class="slider" min="1" max="10" value="5">
                    <div id="complexityValue">Level 5</div>
                </div>
                <div class="control-group">
                    <h3>🎶 Mood</h3>
                    <select id="mood" style="width: 100%; padding: 8px; border-radius: 5px;">
                        <option>Happy</option>
                        <option>Melancholic</option>
                        <option>Energetic</option>
                        <option>Calm</option>
                        <option>Mysterious</option>
                    </select>
                </div>
            </div>

            <div style="text-align: center; margin: 30px 0;">
                <button class="play-btn" onclick="generateComposition()">🎼 Generate AI Composition</button>
                <button onclick="playComposition()">▶️ Play</button>
                <button onclick="stopPlayback()">⏹️ Stop</button>
                <button onclick="saveComposition()">💾 Save</button>
            </div>

            <div class="piano">
                <div class="key" onclick="playNote('C4')">C</div>
                <div class="key black-key" onclick="playNote('C#4')">C#</div>
                <div class="key" onclick="playNote('D4')">D</div>
                <div class="key black-key" onclick="playNote('D#4')">D#</div>
                <div class="key" onclick="playNote('E4')">E</div>
                <div class="key" onclick="playNote('F4')">F</div>
                <div class="key black-key" onclick="playNote('F#4')">F#</div>
                <div class="key" onclick="playNote('G4')">G</div>
                <div class="key black-key" onclick="playNote('G#4')">G#</div>
                <div class="key" onclick="playNote('A4')">A</div>
                <div class="key black-key" onclick="playNote('A#4')">A#</div>
                <div class="key" onclick="playNote('B4')">B</div>
            </div>
        </div>

        <div class="output">
            <h3>AI Composer Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to AI Music Composer! Adjust the settings above and click "Generate AI Composition" to create music.
            </div>
        </div>
    </div>

    <script>
        let currentComposition = [];
        let isPlaying = false;

        document.getElementById('tempo').addEventListener('input', function() {{
            document.getElementById('tempoValue').textContent = this.value + ' BPM';
        }});

        document.getElementById('complexity').addEventListener('input', function() {{
            document.getElementById('complexityValue').textContent = 'Level ' + this.value;
        }});

        function generateComposition() {{
            const genre = document.getElementById('genre').value;
            const tempo = document.getElementById('tempo').value;
            const complexity = document.getElementById('complexity').value;
            const mood = document.getElementById('mood').value;

            const output = document.getElementById('outputContent');
            output.textContent = `🎼 Generating AI Composition...\\n\\n`;
            output.textContent += `Genre: ${{genre}}\\n`;
            output.textContent += `Tempo: ${{tempo}} BPM\\n`;
            output.textContent += `Complexity: Level ${{complexity}}\\n`;
            output.textContent += `Mood: ${{mood}}\\n\\n`;

            // Simulate AI composition generation
            setTimeout(() => {{
                const notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'];
                currentComposition = [];
                const length = parseInt(complexity) * 8;

                for (let i = 0; i < length; i++) {{
                    const note = notes[Math.floor(Math.random() * notes.length)];
                    const duration = Math.random() > 0.7 ? 'half' : 'quarter';
                    currentComposition.push({{note, duration}});
                }}

                output.textContent += `✅ Composition generated!\\n`;
                output.textContent += `Length: ${{currentComposition.length}} notes\\n`;
                output.textContent += `Key signature: C Major\\n`;
                output.textContent += `AI Analysis: ${{mood.toLowerCase()}} melody with ${{genre.toLowerCase()}} influences\\n\\n`;
                output.textContent += `🎵 Ready to play! Click the Play button.`;
            }}, 2000);
        }}

        function playComposition() {{
            if (currentComposition.length === 0) {{
                alert('Generate a composition first!');
                return;
            }}

            if (isPlaying) return;
            isPlaying = true;

            const output = document.getElementById('outputContent');
            output.textContent += '\\n\\n▶️ Playing composition...\\n';

            let index = 0;
            const tempo = parseInt(document.getElementById('tempo').value);
            const noteDuration = 60000 / tempo / 4; // quarter note duration in ms

            const playNext = () => {{
                if (!isPlaying || index >= currentComposition.length) {{
                    isPlaying = false;
                    output.textContent += '\\n\\n⏹️ Playback finished!';
                    return;
                }}

                const note = currentComposition[index];
                playNote(note.note);
                output.textContent += `♪ ${{note.note}} `;

                index++;
                setTimeout(playNext, noteDuration * (note.duration === 'half' ? 2 : 1));
            }};

            playNext();
        }}

        function stopPlayback() {{
            isPlaying = false;
            const output = document.getElementById('outputContent');
            output.textContent += '\\n\\n⏹️ Playback stopped.';
        }}

        function playNote(note) {{
            // Visual feedback
            const keys = document.querySelectorAll('.key');
            keys.forEach(key => {{
                if (key.textContent.trim() === note.replace(/[0-9]/g, '')) {{
                    key.style.background = '#007bff';
                    setTimeout(() => {{
                        key.style.background = key.classList.contains('black-key') ? 'black' : 'white';
                    }}, 200);
                }}
            }});

            // Simulate audio (would need Web Audio API for real sound)
            console.log(`Playing note: ${{note}}`);
        }}

        function saveComposition() {{
            if (currentComposition.length === 0) {{
                alert('Generate a composition first!');
                return;
            }}

            const output = document.getElementById('outputContent');
            output.textContent += `\\n\\n💾 Composition saved as 'ai_composition_${{Date.now()}}.json'\\n`;
            output.textContent += `Format: MIDI-ready\\n`;
            output.textContent += `Size: ${{JSON.stringify(currentComposition).length}} bytes`;
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_iot_productivity_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - IoT Productivity Hub</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .device-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }}
        .device-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        .device-status {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }}
        .status-indicator {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }}
        .online {{ background: #28a745; }}
        .offline {{ background: #dc3545; }}
        .unknown {{ background: #ffc107; }}
        button {{
            background: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9em;
            margin: 2px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #0056b3;
            transform: translateY(-1px);
        }}
        .productivity-zone {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            margin: 0 30px 30px 30px;
            border-radius: 15px;
        }}
        .task-list {{
            background: white;
            color: #333;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }}
        .task-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔗 {title}</h1>
            <p>IoT Productivity Hub - Tema: {', '.join(themes)}</p>
        </div>

        <div class="dashboard">
            <div class="device-card">
                <div class="device-status">
                    <h3>💡 Smart Lights</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <p>Living Room: 75% brightness</p>
                <button onclick="controlLight('living_room', 'on')">Turn On</button>
                <button onclick="controlLight('living_room', 'off')">Turn Off</button>
                <button onclick="setBrightness('living_room')">Set Brightness</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>🌡️ Smart Thermostat</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <p>Current: 24°C | Target: 22°C</p>
                <button onclick="adjustTemp('up')">🔥 +1°C</button>
                <button onclick="adjustTemp('down')">❄️ -1°C</button>
                <button onclick="setSchedule()">Set Schedule</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>📷 Security Camera</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <p>Front Door - Motion detected</p>
                <button onclick="viewCamera('front')">View Live</button>
                <button onclick="armSecurity()">Arm System</button>
                <button onclick="checkRecordings()">View Recordings</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>🎧 Smart Speaker</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <p>Playing: Focus Music | Volume: 60%</p>
                <button onclick="playMusic()">Play Music</button>
                <button onclick="adjustVolume('up')">🔊 +</button>
                <button onclick="adjustVolume('down')">🔉 -</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>☕ Smart Coffee Maker</h3>
                    <span><span class="status-indicator offline"></span>Offline</span>
                </div>
                <p>Last brewed: 2 hours ago</p>
                <button onclick="brewCoffee()">Brew Coffee</button>
                <button onclick="scheduleBrew()">Schedule Brew</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>🏃‍♂️ Fitness Tracker</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <p>Steps: 8,432 | Goal: 10,000</p>
                <button onclick="syncFitness()">Sync Data</button>
                <button onclick="setGoal()">Set Goal</button>
            </div>
        </div>

        <div class="productivity-zone">
            <h2>🎯 Productivity Dashboard</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px;">
                <div style="text-align: center;">
                    <h3>Focus Time</h3>
                    <div style="font-size: 2em;">2h 15m</div>
                </div>
                <div style="text-align: center;">
                    <h3>Tasks Completed</h3>
                    <div style="font-size: 2em;">12/15</div>
                </div>
                <div style="text-align: center;">
                    <h3>Energy Level</h3>
                    <div style="font-size: 2em;">78%</div>
                </div>
                <div style="text-align: center;">
                    <h3>Break Reminder</h3>
                    <div style="font-size: 2em;">15m</div>
                </div>
            </div>

            <div class="task-list">
                <h3>Today's Tasks</h3>
                <div class="task-item">
                    <span>Meeting with team</span>
                    <span>14:00</span>
                </div>
                <div class="task-item">
                    <span>Review code changes</span>
                    <span>16:00</span>
                </div>
                <div class="task-item">
                    <span>Update documentation</span>
                    <span>17:30</span>
                </div>
            </div>
        </div>

        <div class="output">
            <h3>IoT Hub Activity Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to IoT Productivity Hub! Control your smart devices and track productivity metrics.
            </div>
        </div>
    </div>

    <script>
        let thermostatTemp = 24;
        let lightBrightness = 75;
        let speakerVolume = 60;

        function controlLight(room, action) {{
            const output = document.getElementById('outputContent');
            if (action === 'on') {{
                output.textContent = `💡 Turning on lights in ${{room.replace('_', ' ')}}...\\n✅ Lights activated at ${{lightBrightness}}% brightness\\n`;
            }} else {{
                output.textContent = `💡 Turning off lights in ${{room.replace('_', ' ')}}...\\n✅ Lights deactivated\\n`;
            }}
        }}

        function setBrightness(room) {{
            const brightness = prompt('Set brightness (0-100):', lightBrightness);
            if (brightness !== null) {{
                lightBrightness = Math.max(0, Math.min(100, parseInt(brightness)));
                const output = document.getElementById('outputContent');
                output.textContent = `💡 Adjusting brightness in ${{room.replace('_', ' ')}} to ${{lightBrightness}}%...\\n✅ Brightness updated\\n`;
            }}
        }}

        function adjustTemp(direction) {{
            if (direction === 'up') {{
                thermostatTemp += 1;
            }} else {{
                thermostatTemp -= 1;
            }}
            thermostatTemp = Math.max(16, Math.min(30, thermostatTemp));
            const output = document.getElementById('outputContent');
            output.textContent = `🌡️ Adjusting thermostat temperature to ${{thermostatTemp}}°C...\\n✅ Temperature set\\n`;
        }}

        function setSchedule() {{
            const output = document.getElementById('outputContent');
            output.textContent = `⏰ Setting up smart schedule...\\n✅ Schedule configured:\\n  - 07:00: Wake up (lights on, coffee brewing)\\n  - 18:00: Evening mode (lights dimmed)\\n  - 22:00: Night mode (security armed)\\n`;
        }}

        function viewCamera(location) {{
            const output = document.getElementById('outputContent');
            output.textContent = `📷 Accessing camera feed for ${{location.replace('_', ' ')}}...\\n✅ Live feed active\\n📊 Motion detection: Enabled\\n🔒 Security status: Monitoring\\n`;
        }}

        function armSecurity() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🔒 Arming security system...\\n✅ All cameras activated\\n✅ Motion sensors enabled\\n✅ Alarm system ready\\n`;
        }}

        function playMusic() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🎧 Starting music playback...\\n🎵 Now playing: "Productive Focus" playlist\\n🔊 Volume: ${{speakerVolume}}%\\n⏯️ Status: Playing\\n`;
        }}

        function adjustVolume(direction) {{
            if (direction === 'up') {{
                speakerVolume = Math.min(100, speakerVolume + 10);
            }} else {{
                speakerVolume = Math.max(0, speakerVolume - 10);
            }}
            const output = document.getElementById('outputContent');
            output.textContent = `🔊 Adjusting volume to ${{speakerVolume}}%...\\n✅ Volume updated\\n`;
        }}

        function brewCoffee() {{
            const output = document.getElementById('outputContent');
            output.textContent = `☕ Starting coffee brewing process...\\n🔥 Heating water...\\n☕ Brewing...\\n✅ Coffee ready! Estimated time: 4 minutes\\n`;
        }}

        function syncFitness() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🏃‍♂️ Syncing fitness data...\\n📊 Steps today: 8,432\\n🔥 Calories burned: 1,250\\n❤️ Heart rate avg: 72 BPM\\n😴 Sleep last night: 7.5 hours\\n✅ Data synchronized\\n`;
        }}

        function setGoal() {{
            const goal = prompt('Set daily step goal:', '10000');
            if (goal) {{
                const output = document.getElementById('outputContent');
                output.textContent = `🎯 Setting new fitness goal: ${{goal}} steps per day\\n✅ Goal updated\\n💪 Let's crush it!\\n`;
            }}
        }}

        function checkRecordings() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📹 Accessing security recordings...\\n📅 Today:\\n  - 08:15: Front door motion\\n  - 12:30: Backyard activity\\n  - 18:45: Delivery person\\n📅 Yesterday:\\n  - 22:10: Evening walk\\n✅ Recordings loaded\\n`;
        }}

        function scheduleBrew() {{
            const time = prompt('Set brew time (HH:MM):', '07:00');
            if (time) {{
                const output = document.getElementById('outputContent');
                output.textContent = `⏰ Scheduling coffee brew for ${{time}}...\\n✅ Auto-brew scheduled\\n☕ Fresh coffee every morning!\\n`;
            }}
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_health_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Health Tracker</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .metric-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border: 2px solid #e9ecef;
        }}
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            color: #007bff;
        }}
        .progress-bar {{
            background: #e9ecef;
            border-radius: 10px;
            height: 10px;
            margin: 10px 0;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745, #20c997);
            border-radius: 10px;
        }}
        button {{
            background: #28a745;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #218838;
            transform: translateY(-2px);
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 {title}</h1>
            <p>Personal Health Tracker - Tema: {', '.join(themes)}</p>
        </div>

        <div class="dashboard">
            <div class="metric-card">
                <h3>Steps Today</h3>
                <div class="metric-value" id="steps">8,432</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 84%"></div>
                </div>
                <small>Goal: 10,000</small>
            </div>
            <div class="metric-card">
                <h3>Calories Burned</h3>
                <div class="metric-value" id="calories">1,250</div>
                <small>Active calories: 850</small>
            </div>
            <div class="metric-card">
                <h3>Sleep Quality</h3>
                <div class="metric-value" id="sleep">7.5h</div>
                <small>Deep sleep: 2.1h</small>
            </div>
            <div class="metric-card">
                <h3>Water Intake</h3>
                <div class="metric-value" id="water">1.8L</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 72%"></div>
                </div>
                <small>Goal: 2.5L</small>
            </div>
            <div class="metric-card">
                <h3>Heart Rate</h3>
                <div class="metric-value" id="heartrate">72</div>
                <small>BPM (Resting)</small>
            </div>
            <div class="metric-card">
                <h3>Weight</h3>
                <div class="metric-value" id="weight">68.5</div>
                <small>kg (↓0.3kg this week)</small>
            </div>
        </div>

        <div style="text-align: center; padding: 30px;">
            <button onclick="logActivity()">📝 Log Activity</button>
            <button onclick="startWorkout()">🏃‍♂️ Start Workout</button>
            <button onclick="trackMeal()">🍎 Track Meal</button>
            <button onclick="checkHealth()">🏥 Health Check</button>
            <button onclick="viewTrends()">📊 View Trends</button>
        </div>

        <div class="output">
            <h3>Health Activity Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to Health Tracker! Monitor your daily health metrics and stay on top of your wellness goals.
            </div>
        </div>
    </div>

    <script>
        function logActivity() {{
            const output = document.getElementById('outputContent');
            const activities = [
                'Morning jog - 30 minutes',
                'Yoga session - 45 minutes',
                'Weight training - 60 minutes',
                'Swimming - 40 minutes'
            ];
            const activity = activities[Math.floor(Math.random() * activities.length)];
            output.textContent = `📝 Logging activity: ${{activity}}\\n\\n`;
            output.textContent += `⏱️ Duration recorded\\n`;
            output.textContent += `🔥 Calories burned: +${{Math.floor(Math.random() * 300) + 100}}\\n`;
            output.textContent += `✅ Activity logged successfully!\\n`;
            updateMetrics();
        }}

        function startWorkout() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🏃‍♂️ Starting workout session...\\n\\n`;
            output.textContent += `🎯 Workout plan loaded:\\n`;
            output.textContent += `  - Warm-up: 5 minutes\\n`;
            output.textContent += `  - Cardio: 20 minutes\\n`;
            output.textContent += `  - Strength: 15 minutes\\n`;
            output.textContent += `  - Cool-down: 5 minutes\\n\\n`;
            output.textContent += `💪 Let's crush this workout!\\n`;
        }}

        function trackMeal() {{
            const output = document.getElementById('outputContent');
            const meals = [
                'Breakfast: Oatmeal with berries - 320 cal',
                'Lunch: Grilled chicken salad - 450 cal',
                'Dinner: Salmon with vegetables - 520 cal',
                'Snack: Greek yogurt - 150 cal'
            ];
            const meal = meals[Math.floor(Math.random() * meals.length)];
            output.textContent = `🍎 Tracking meal: ${{meal}}\\n\\n`;
            output.textContent += `📊 Nutrition breakdown:\\n`;
            output.textContent += `  - Protein: ${{Math.floor(Math.random() * 30) + 10}}g\\n`;
            output.textContent += `  - Carbs: ${{Math.floor(Math.random() * 50) + 20}}g\\n`;
            output.textContent += `  - Fat: ${{Math.floor(Math.random() * 20) + 5}}g\\n`;
            output.textContent += `✅ Meal logged!\\n`;
        }}

        function checkHealth() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🏥 Running health assessment...\\n\\n`;
            output.textContent += `📊 Current vitals:\\n`;
            output.textContent += `  - Blood pressure: 120/80\\n`;
            output.textContent += `  - BMI: 22.3 (Normal)\\n`;
            output.textContent += `  - Body fat: 18%\\n\\n`;
            output.textContent += `💡 Health recommendations:\\n`;
            output.textContent += `  - Stay hydrated\\n`;
            output.textContent += `  - Get 7-8 hours of sleep\\n`;
            output.textContent += `  - Maintain regular exercise\\n\\n`;
            output.textContent += `✅ Assessment complete!\\n`;
        }}

        function viewTrends() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📊 Health trends analysis:\\n\\n`;
            output.textContent += `📈 This week:\\n`;
            output.textContent += `  - Steps: ↑12%\\n`;
            output.textContent += `  - Sleep: ↑8%\\n`;
            output.textContent += `  - Weight: ↓0.5kg\\n\\n`;
            output.textContent += `🎯 Goals progress:\\n`;
            output.textContent += `  - Daily steps: 84% achieved\\n`;
            output.textContent += `  - Water intake: 72% achieved\\n`;
            output.textContent += `  - Workout frequency: 100% achieved\\n\\n`;
            output.textContent += `🏆 Keep up the great work!\\n`;
        }}

        function updateMetrics() {{
            // Simulate metric updates
            const stepsEl = document.getElementById('steps');
            const currentSteps = parseInt(stepsEl.textContent.replace(',', ''));
            const newSteps = currentSteps + Math.floor(Math.random() * 500) + 100;
            stepsEl.textContent = newSteps.toLocaleString();

            const caloriesEl = document.getElementById('calories');
            const currentCal = parseInt(caloriesEl.textContent.replace(',', ''));
            const newCal = currentCal + Math.floor(Math.random() * 200) + 50;
            caloriesEl.textContent = newCal.toLocaleString();
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_game_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Game Hub</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .game-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .game-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
            cursor: pointer;
        }}
        .game-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        .game-icon {{
            font-size: 3em;
            margin-bottom: 15px;
        }}
        button {{
            background: #007bff;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #0056b3;
            transform: translateY(-2px);
        }}
        .score-display {{
            font-size: 2em;
            margin: 20px 0;
            font-weight: bold;
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 {title}</h1>
            <p>Game Hub & Entertainment - Tema: {', '.join(themes)}</p>
        </div>

        <div style="text-align: center; padding: 20px;">
            <div class="score-display">
                Total Score: <span id="totalScore">0</span> | Games Played: <span id="gamesPlayed">0</span>
            </div>
        </div>

        <div class="game-grid">
            <div class="game-card" onclick="playNumberGuess()">
                <div class="game-icon">🔢</div>
                <h3>Number Guessing</h3>
                <p>Guess the secret number!</p>
                <small>High Score: 5 attempts</small>
            </div>
            <div class="game-card" onclick="playWordPuzzle()">
                <div class="game-icon">📝</div>
                <h3>Word Puzzle</h3>
                <p>Unscramble the words!</p>
                <small>High Score: 120 pts</small>
            </div>
            <div class="game-card" onclick="playMemoryGame()">
                <div class="game-icon">🧠</div>
                <h3>Memory Challenge</h3>
                <p>Remember the sequence!</p>
                <small>High Score: 15 levels</small>
            </div>
            <div class="game-card" onclick="playTrivia()">
                <div class="game-icon">🧠</div>
                <h3>Trivia Quiz</h3>
                <p>Test your knowledge!</p>
                <small>High Score: 95%</small>
            </div>
            <div class="game-card" onclick="playReaction()">
                <div class="game-icon">⚡</div>
                <h3>Reaction Time</h3>
                <p>How fast are you?</p>
                <small>Best Time: 0.23s</small>
            </div>
            <div class="game-card" onclick="playMathQuiz()">
                <div class="game-icon">🔢</div>
                <h3>Math Quiz</h3>
                <p>Quick calculations!</p>
                <small>High Score: 25 correct</small>
            </div>
        </div>

        <div style="text-align: center; padding: 20px;">
            <button onclick="viewLeaderboard()">🏆 Leaderboard</button>
            <button onclick="resetScores()">🔄 Reset Scores</button>
            <button onclick="gameSettings()">⚙️ Settings</button>
        </div>

        <div class="output">
            <h3>Game Activity</h3>
            <div class="output-content" id="outputContent">
                Welcome to Game Hub! Choose a game from the grid above to start playing.
            </div>
        </div>
    </div>

    <script>
        let totalScore = 0;
        let gamesPlayed = 0;
        let currentGame = null;

        function updateScoreDisplay() {{
            document.getElementById('totalScore').textContent = totalScore;
            document.getElementById('gamesPlayed').textContent = gamesPlayed;
        }}

        function playNumberGuess() {{
            const output = document.getElementById('outputContent');
            output.textContent = '🔢 Starting Number Guessing Game!\\n\\n';
            output.textContent += 'I\'m thinking of a number between 1 and 100...\\n\\n';
            let attempts = 0;
            const secretNumber = Math.floor(Math.random() * 100) + 1;

            currentGame = {{
                type: 'number_guess',
                secret: secretNumber,
                attempts: 0,
                guess: function(num) {{
                    this.attempts++;
                    if (num === this.secret) {{
                        const points = Math.max(100 - this.attempts * 10, 10);
                        totalScore += points;
                        gamesPlayed++;
                        updateScoreDisplay();
                        output.textContent += `\\n🎉 Correct! You got it in ${{this.attempts}} attempts.\\n🏆 Earned ${{points}} points!\\n`;
                        currentGame = null;
                    }} else if (num < this.secret) {{
                        output.textContent += `\\n📉 Too low! Try higher.\\n`;
                    }} else {{
                        output.textContent += `\\n📈 Too high! Try lower.\\n`;
                    }}
                }}
            }};
        }}

        function playWordPuzzle() {{
            const output = document.getElementById('outputContent');
            const words = [
                {{scrambled: 'tobor', answer: 'robot'}},
                {{scrambled: 'mupetc', answer: 'compute'}},
                {{scrambled: 'gamenig', answer: 'gaming'}}
            ];
            const word = words[Math.floor(Math.random() * words.length)];

            output.textContent = `📝 Word Puzzle Challenge!\\n\\n`;
            output.textContent += `Unscramble: ${{word.scrambled.toUpperCase()}}\\n\\n`;
            output.textContent += `Hint: It's related to technology/games.\\n`;

            currentGame = {{
                type: 'word_puzzle',
                answer: word.answer,
                scrambled: word.scrambled,
                solve: function(guess) {{
                    if (guess.toLowerCase() === this.answer) {{
                        const points = 50;
                        totalScore += points;
                        gamesPlayed++;
                        updateScoreDisplay();
                        output.textContent += `\\n🎉 Correct! "${{this.answer}}" is right!\\n🏆 Earned ${{points}} points!\\n`;
                        currentGame = null;
                    }} else {{
                        output.textContent += `\\n❌ Not quite right. Try again!\\n`;
                    }}
                }}
            }};
        }}

        function playMemoryGame() {{
            const output = document.getElementById('outputContent');
            output.textContent = '🧠 Memory Challenge Starting!\\n\\n';
            output.textContent += 'Watch the sequence carefully...\\n\\n';

            const colors = ['🔴', '🔵', '🟢', '🟡'];
            let sequence = [];
            let playerSequence = [];
            let level = 1;

            function showSequence() {{
                output.textContent = `🧠 Level ${{level}} - Watch closely:\\n`;
                sequence.forEach((color, i) => {{
                    setTimeout(() => {{
                        output.textContent += color + ' ';
                    }}, i * 1000);
                }});
                setTimeout(() => {{
                    output.textContent += '\\n\\n🎯 Your turn! Repeat the sequence.\\n';
                }}, sequence.length * 1000 + 500);
            }}

            function nextLevel() {{
                sequence.push(colors[Math.floor(Math.random() * colors.length)]);
                showSequence();
            }}

            currentGame = {{
                type: 'memory',
                sequence: sequence,
                playerSequence: playerSequence,
                level: level,
                nextLevel: nextLevel,
                checkSequence: function(color) {{
                    // This would need more complex input handling
                    output.textContent += `Clicked: ${{color}}\\n`;
                }}
            }};

            nextLevel();
        }}

        function playTrivia() {{
            const output = document.getElementById('outputContent');
            const questions = [
                {{
                    q: 'What does CPU stand for?',
                    a: 'central processing unit',
                    options: ['central processing unit', 'computer power unit', 'central program utility']
                }},
                {{
                    q: 'Which programming language was created by Guido van Rossum?',
                    a: 'python',
                    options: ['python', 'java', 'javascript']
                }}
            ];

            const q = questions[Math.floor(Math.random() * questions.length)];
            output.textContent = `🧠 Trivia Question!\\n\\n${{q.q}}\\n\\n`;
            q.options.forEach((opt, i) => {{
                output.textContent += `${{i + 1}}. ${{opt}}\\n`;
            }});

            currentGame = {{
                type: 'trivia',
                answer: q.a,
                check: function(choice) {{
                    const selected = q.options[choice - 1];
                    if (selected && selected.toLowerCase() === this.answer) {{
                        const points = 25;
                        totalScore += points;
                        gamesPlayed++;
                        updateScoreDisplay();
                        output.textContent += `\\n✅ Correct! Well done!\\n🏆 Earned ${{points}} points!\\n`;
                        currentGame = null;
                    }} else {{
                        output.textContent += `\\n❌ Incorrect. The answer was: ${{this.answer}}\\n`;
                        currentGame = null;
                    }}
                }}
            }};
        }}

        function playReaction() {{
            const output = document.getElementById('outputContent');
            output.textContent = '⚡ Reaction Time Test!\\n\\n';
            output.textContent += 'Get ready...\\n';

            setTimeout(() => {{
                const startTime = Date.now();
                output.textContent += '🟢 CLICK NOW!\\n';

                currentGame = {{
                    type: 'reaction',
                    startTime: startTime,
                    click: function() {{
                        const reactionTime = Date.now() - this.startTime;
                        const points = Math.max(100 - Math.floor(reactionTime / 10), 10);
                        totalScore += points;
                        gamesPlayed++;
                        updateScoreDisplay();
                        output.textContent += `\\n⚡ Reaction time: ${{reactionTime}}ms\\n🏆 Earned ${{points}} points!\\n`;
                        currentGame = null;
                    }}
                }};
            }}, Math.random() * 3000 + 1000);
        }}

        function playMathQuiz() {{
            const output = document.getElementById('outputContent');
            const num1 = Math.floor(Math.random() * 20) + 1;
            const num2 = Math.floor(Math.random() * 20) + 1;
            const answer = num1 + num2;

            output.textContent = `🔢 Math Quiz!\\n\\nWhat is ${{num1}} + ${{num2}}?\\n`;

            currentGame = {{
                type: 'math',
                answer: answer,
                check: function(guess) {{
                    if (parseInt(guess) === this.answer) {{
                        const points = 10;
                        totalScore += points;
                        gamesPlayed++;
                        updateScoreDisplay();
                        output.textContent += `\\n✅ Correct! ${{num1}} + ${{num2}} = ${{this.answer}}\\n🏆 Earned ${{points}} points!\\n`;
                        currentGame = null;
                    }} else {{
                        output.textContent += `\\n❌ Incorrect. The answer is ${{this.answer}}.\\n`;
                        currentGame = null;
                    }}
                }}
            }};
        }}

        function viewLeaderboard() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🏆 Game Leaderboard\\n\\n`;
            output.textContent += `🎯 Total Score: ${{totalScore}}\\n`;
            output.textContent += `🎮 Games Played: ${{gamesPlayed}}\\n`;
            output.textContent += `📊 Average Score: ${{gamesPlayed > 0 ? Math.round(totalScore / gamesPlayed) : 0}}\\n\\n`;
            output.textContent += `🏅 Achievements:\\n`;
            if (totalScore >= 500) output.textContent += `  - 🏆 Master Gamer\\n`;
            if (gamesPlayed >= 10) output.textContent += `  - 🎮 Game Addict\\n`;
            if (totalScore >= 1000) output.textContent += `  - 💎 Diamond Player\\n`;
        }}

        function resetScores() {{
            if (confirm('Reset all scores and progress?')) {{
                totalScore = 0;
                gamesPlayed = 0;
                updateScoreDisplay();
                const output = document.getElementById('outputContent');
                output.textContent = '🔄 Scores reset! Start fresh and beat your records!';
            }}
        }}

        function gameSettings() {{
            const output = document.getElementById('outputContent');
            output.textContent = `⚙️ Game Settings\\n\\n`;
            output.textContent += `🎵 Sound Effects: Enabled\\n`;
            output.textContent += `🌈 Visual Effects: Enabled\\n`;
            output.textContent += `⏱️ Time Limits: Standard\\n`;
            output.textContent += `🎯 Difficulty: Normal\\n\\n`;
            output.textContent += `💡 Tip: Play regularly to improve your scores!`;
        }}
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_music_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Music Player</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .player {{
            padding: 30px;
            text-align: center;
        }}
        .album-art {{
            width: 200px;
            height: 200px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 50%;
            margin: 0 auto 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4em;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        .track-info {{
            margin-bottom: 30px;
        }}
        .track-title {{
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .artist {{
            color: #666;
            margin-bottom: 20px;
        }}
        .progress-bar {{
            width: 100%;
            height: 6px;
            background: #e9ecef;
            border-radius: 3px;
            margin: 20px 0;
            cursor: pointer;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
            border-radius: 3px;
            width: 0%;
        }}
        .controls {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin: 30px 0;
        }}
        .control-btn {{
            background: #007bff;
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1.2em;
            transition: all 0.3s ease;
        }}
        .control-btn:hover {{
            background: #0056b3;
            transform: scale(1.1);
        }}
        .play-btn {{
            width: 60px;
            height: 60px;
            background: #28a745;
        }}
        .play-btn:hover {{
            background: #218838;
        }}
        .playlist {{
            margin-top: 40px;
        }}
        .playlist-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            border-bottom: 1px solid #eee;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .playlist-item:hover {{
            background: #f8f9fa;
        }}
        .playlist-item.active {{
            background: #e3f2fd;
            border-left: 4px solid #007bff;
        }}
        button {{
            background: #6c757d;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #5a6268;
            transform: translateY(-1px);
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎵 {title}</h1>
            <p>Music Player & Audio Experience - Tema: {', '.join(themes)}</p>
        </div>

        <div class="player">
            <div class="album-art" id="albumArt">🎵</div>

            <div class="track-info">
                <div class="track-title" id="trackTitle">Select a track to play</div>
                <div class="artist" id="artist">Choose from playlist below</div>
                <div id="timeDisplay">0:00 / 0:00</div>
            </div>

            <div class="progress-bar" onclick="seek(event)">
                <div class="progress-fill" id="progressFill"></div>
            </div>

            <div class="controls">
                <button class="control-btn" onclick="previousTrack()">⏮️</button>
                <button class="control-btn play-btn" id="playBtn" onclick="togglePlay()">▶️</button>
                <button class="control-btn" onclick="nextTrack()">⏭️</button>
                <button onclick="toggleShuffle()">🔀</button>
                <button onclick="toggleRepeat()">🔁</button>
            </div>

            <div style="margin-top: 20px;">
                <input type="range" id="volumeSlider" min="0" max="100" value="70" onchange="setVolume(this.value)">
                <label for="volumeSlider">🔊 Volume: <span id="volumeValue">70</span>%</label>
            </div>
        </div>

        <div class="playlist">
            <h3 style="text-align: center; margin-bottom: 20px;">🎶 Playlist</h3>
            <div id="playlist">
                <div class="playlist-item active" onclick="selectTrack(0)">
                    <div>
                        <div style="font-weight: bold;">Ocean Waves</div>
                        <div style="color: #666; font-size: 0.9em;">Nature Sounds</div>
                    </div>
                    <div>3:24</div>
                </div>
                <div class="playlist-item" onclick="selectTrack(1)">
                    <div>
                        <div style="font-weight: bold;">Forest Ambience</div>
                        <div style="color: #666; font-size: 0.9em;">Relaxation</div>
                    </div>
                    <div>4:12</div>
                </div>
                <div class="playlist-item" onclick="selectTrack(2)">
                    <div>
                        <div style="font-weight: bold;">Rain Sounds</div>
                        <div style="color: #666; font-size: 0.9em;">Sleep Aid</div>
                    </div>
                    <div>2:58</div>
                </div>
                <div class="playlist-item" onclick="selectTrack(3)">
                    <div>
                        <div style="font-weight: bold;">Jazz Piano</div>
                        <div style="color: #666; font-size: 0.9em;">Instrumental</div>
                    </div>
                    <div>5:43</div>
                </div>
                <div class="playlist-item" onclick="selectTrack(4)">
                    <div>
                        <div style="font-weight: bold;">Electronic Beats</div>
                        <div style="color: #666; font-size: 0.9em;">EDM</div>
                    </div>
                    <div>3:57</div>
                </div>
            </div>
        </div>

        <div style="text-align: center; padding: 20px;">
            <button onclick="createPlaylist()">➕ Create Playlist</button>
            <button onclick="importMusic()">📁 Import Music</button>
            <button onclick="equalizerSettings()">🎛️ Equalizer</button>
        </div>

        <div class="output">
            <h3>Music Activity Log</h3>
            <div class="output-content" id="outputContent">
                Welcome to Music Player! Select a track from the playlist above to start listening.
            </div>
        </div>
    </div>

    <script>
        let currentTrack = 0;
        let isPlaying = false;
        let currentTime = 0;
        let duration = 0;
        let volume = 70;
        let shuffle = false;
        let repeat = false;

        const tracks = [
            {{title: 'Ocean Waves', artist: 'Nature Sounds', duration: 204}},
            {{title: 'Forest Ambience', artist: 'Relaxation', duration: 252}},
            {{title: 'Rain Sounds', artist: 'Sleep Aid', duration: 178}},
            {{title: 'Jazz Piano', artist: 'Instrumental', duration: 343}},
            {{title: 'Electronic Beats', artist: 'EDM', duration: 237}}
        ];

        function selectTrack(index) {{
            currentTrack = index;
            currentTime = 0;
            updateTrackDisplay();
            updatePlaylistUI();
            if (isPlaying) {{
                // Would start actual playback here
            }}
            const output = document.getElementById('outputContent');
            output.textContent = `🎵 Selected: ${{tracks[currentTrack].title}} by ${{tracks[currentTrack].artist}}\\n\\nReady to play!`;
        }}

        function updateTrackDisplay() {{
            const track = tracks[currentTrack];
            document.getElementById('trackTitle').textContent = track.title;
            document.getElementById('artist').textContent = track.artist;
            duration = track.duration;
            updateTimeDisplay();
        }}

        function updateTimeDisplay() {{
            const current = formatTime(currentTime);
            const total = formatTime(duration);
            document.getElementById('timeDisplay').textContent = `${{current}} / ${{total}}`;
            const progressPercent = (currentTime / duration) * 100;
            document.getElementById('progressFill').style.width = `${{progressPercent}}%`;
        }}

        function formatTime(seconds) {{
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            return `${{mins}}:${{secs.toString().padStart(2, '0')}}`;
        }}

        function togglePlay() {{
            isPlaying = !isPlaying;
            const playBtn = document.getElementById('playBtn');
            const output = document.getElementById('outputContent');

            if (isPlaying) {{
                playBtn.textContent = '⏸️';
                output.textContent = `▶️ Now playing: ${{tracks[currentTrack].title}}\\n\\n`;
                output.textContent += `🎵 Artist: ${{tracks[currentTrack].artist}}\\n`;
                output.textContent += `⏱️ Duration: ${{formatTime(duration)}}\\n`;
                output.textContent += `🔊 Volume: ${{volume}}%\\n\\n`;
                output.textContent += `🎶 Enjoy your music!`;

                // Simulate playback progress
                const progressInterval = setInterval(() => {{
                    if (!isPlaying) {{
                        clearInterval(progressInterval);
                        return;
                    }}
                    currentTime += 1;
                    if (currentTime >= duration) {{
                        if (repeat) {{
                            currentTime = 0;
                        }} else {{
                            nextTrack();
                        }}
                    }}
                    updateTimeDisplay();
                }}, 1000);
            }} else {{
                playBtn.textContent = '▶️';
                output.textContent = `⏸️ Paused: ${{tracks[currentTrack].title}}\\n\\nResume playback when ready.`;
            }}
        }}

        function nextTrack() {{
            if (shuffle) {{
                currentTrack = Math.floor(Math.random() * tracks.length);
            }} else {{
                currentTrack = (currentTrack + 1) % tracks.length;
            }}
            selectTrack(currentTrack);
            if (isPlaying) {{
                // Would continue playback
            }}
        }}

        function previousTrack() {{
            currentTrack = currentTrack > 0 ? currentTrack - 1 : tracks.length - 1;
            selectTrack(currentTrack);
            if (isPlaying) {{
                // Would continue playback
            }}
        }}

        function seek(event) {{
            const progressBar = event.target;
            const rect = progressBar.getBoundingClientRect();
            const clickX = event.clientX - rect.left;
            const percentage = clickX / rect.width;
            currentTime = Math.floor(percentage * duration);
            updateTimeDisplay();
        }}

        function setVolume(value) {{
            volume = value;
            document.getElementById('volumeValue').textContent = volume;
            const output = document.getElementById('outputContent');
            output.textContent += `\\n\\n🔊 Volume set to ${{volume}}%`;
        }}

        function toggleShuffle() {{
            shuffle = !shuffle;
            const output = document.getElementById('outputContent');
            output.textContent += `\\n\\n🔀 Shuffle ${{shuffle ? 'enabled' : 'disabled'}}`;
        }}

        function toggleRepeat() {{
            repeat = !repeat;
            const output = document.getElementById('outputContent');
            output.textContent += `\\n\\n🔁 Repeat ${{repeat ? 'enabled' : 'disabled'}}`;
        }}

        function updatePlaylistUI() {{
            const items = document.querySelectorAll('.playlist-item');
            items.forEach((item, index) => {{
                item.classList.toggle('active', index === currentTrack);
            }});
        }}

        function createPlaylist() {{
            const output = document.getElementById('outputContent');
            output.textContent = `➕ Creating new playlist...\\n\\n`;
            output.textContent += `📝 Playlist name: "My Favorites"\\n`;
            output.textContent += `🎵 Tracks added: 0\\n`;
            output.textContent += `⏱️ Total duration: 0:00\\n\\n`;
            output.textContent += `💡 Add tracks to your playlist by selecting them!`;
        }}

        function importMusic() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📁 Importing music files...\\n\\n`;
            output.textContent += `🔍 Scanning music folder...\\n`;
            output.textContent += `📊 Found 15 audio files\\n`;
            output.textContent += `🎵 Added to library: 12 tracks\\n`;
            output.textContent += `⚠️ Skipped 3 unsupported files\\n\\n`;
            output.textContent += `✅ Import complete!`;
        }}

        function equalizerSettings() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🎛️ Audio Equalizer Settings\\n\\n`;
            output.textContent += `🎚️ Bass: +2dB\\n`;
            output.textContent += `🎚️ Mid: 0dB\\n`;
            output.textContent += `🎚️ Treble: +1dB\\n`;
            output.textContent += `🎚️ Presence: 0dB\\n\\n`;
            output.textContent += `🎛️ Preset: "Rock"\\n`;
            output.textContent += `🔊 Balance: Center\\n\\n`;
            output.textContent += `💡 Adjust settings for optimal sound quality!`;
        }}

        // Initialize
        updateTrackDisplay();
        updatePlaylistUI();
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_ai_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AI Assistant</title>
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
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .chat-container {{
            height: 500px;
            display: flex;
            flex-direction: column;
            padding: 30px;
        }}
        .chat-messages {{
            flex: 1;
            overflow-y: auto;
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .message {{
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 15px;
            max-width: 80%;
        }}
        .message.user {{
            background: #007bff;
            color: white;
            margin-left: auto;
            text-align: right;
        }}
        .message.ai {{
            background: white;
            border: 1px solid #e9ecef;
        }}
        .input-area {{
            display: flex;
            gap: 10px;
        }}
        .message-input {{
            flex: 1;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 1em;
        }}
        .send-btn {{
            background: #28a745;
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s ease;
        }}
        .send-btn:hover {{
            background: #218838;
            transform: translateY(-2px);
        }}
        .quick-actions {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        .action-btn {{
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            padding: 15px;
            border-radius: 15px;
            cursor: pointer;
            text-align: center;
            transition: all 0.3s ease;
        }}
        .action-btn:hover {{
            background: #007bff;
            color: white;
            border-color: #007bff;
            transform: translateY(-2px);
        }}
        .ai-avatar {{
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            font-size: 1.2em;
        }}
        .typing {{
            display: none;
            padding: 15px;
            color: #666;
            font-style: italic;
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 {title}</h1>
            <p>AI Assistant & Intelligent Helper - Tema: {', '.join(themes)}</p>
        </div>

        <div class="chat-container">
            <div class="quick-actions">
                <div class="action-btn" onclick="quickAction('schedule')">📅 Plan my day</div>
                <div class="action-btn" onclick="quickAction('reminder')">⏰ Set reminder</div>
                <div class="action-btn" onclick="quickAction('weather')">🌤️ Check weather</div>
                <div class="action-btn" onclick="quickAction('recipe')">🍳 Suggest recipe</div>
                <div class="action-btn" onclick="quickAction('joke')">😄 Tell a joke</div>
                <div class="action-btn" onclick="quickAction('translate')">🌐 Translate text</div>
            </div>

            <div class="chat-messages" id="chatMessages">
                <div class="message ai">
                    <div class="ai-avatar">🤖</div>
                    Hello! I'm your AI assistant. How can I help you today?
                </div>
            </div>

            <div class="typing" id="typingIndicator">
                AI is typing...
            </div>

            <div class="input-area">
                <input type="text" class="message-input" id="messageInput" placeholder="Type your message here..." onkeypress="handleKeyPress(event)">
                <button class="send-btn" onclick="sendMessage()">Send</button>
            </div>
        </div>

        <div class="output">
            <h3>AI Activity Log</h3>
            <div class="output-content" id="outputContent">
                AI Assistant initialized. Ready to help with various tasks and queries.
            </div>
        </div>
    </div>

    <script>
        let conversationHistory = [
            {{role: 'ai', content: 'Hello! I\\'m your AI assistant. How can I help you today?'}}
        ];

        function addMessage(content, sender) {{
            const messagesDiv = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${{sender}}`;

            if (sender === 'ai') {{
                messageDiv.innerHTML = `<div class="ai-avatar">🤖</div>${{content}}`;
            }} else {{
                messageDiv.textContent = content;
            }}

            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }}

        function showTyping() {{
            document.getElementById('typingIndicator').style.display = 'block';
        }}

        function hideTyping() {{
            document.getElementById('typingIndicator').style.display = 'none';
        }}

        function sendMessage() {{
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            if (!message) return;

            addMessage(message, 'user');
            conversationHistory.push({{role: 'user', content: message}});
            input.value = '';

            showTyping();

            // Simulate AI response
            setTimeout(() => {{
                hideTyping();
                const response = generateAIResponse(message);
                addMessage(response, 'ai');
                conversationHistory.push({{role: 'ai', content: response}});

                const output = document.getElementById('outputContent');
                output.textContent = `💬 Latest interaction:\\nUser: ${{message}}\\nAI: ${{response}}\\n\\n📊 Conversation length: ${{conversationHistory.length}} messages`;
            }}, 1000 + Math.random() * 2000);
        }}

        function handleKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendMessage();
            }}
        }}

        function generateAIResponse(message) {{
            const lowerMessage = message.toLowerCase();

            if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {{
                return 'Hello! Nice to meet you. What would you like to talk about?';
            }}

            if (lowerMessage.includes('weather')) {{
                const conditions = ['sunny', 'cloudy', 'rainy', 'windy'];
                const temp = Math.floor(Math.random() * 20) + 15;
                const condition = conditions[Math.floor(Math.random() * conditions.length)];
                return `🌤️ Today's weather: ${{temp}}°C and ${{condition}}. Perfect day for outdoor activities!`;
            }}

            if (lowerMessage.includes('time')) {{
                return `🕐 Current time is ${{new Date().toLocaleTimeString()}}. How can I help you make the most of your day?`;
            }}

            if (lowerMessage.includes('joke')) {{
                const jokes = [
                    'Why did the computer go to therapy? It had too many bytes of emotional baggage! 🤖',
                    'What do you call a bear with no teeth? A gummy bear! 🐻',
                    'Why did the scarecrow win an award? Because he was outstanding in his field! 🌾'
                ];
                return jokes[Math.floor(Math.random() * jokes.length)];
            }}

            if (lowerMessage.includes('help')) {{
                return 'I can help you with:\\n• 📅 Planning and scheduling\\n• ⏰ Setting reminders\\n• 🌤️ Weather information\\n• 🍳 Recipe suggestions\\n• 😄 Jokes and entertainment\\n• 🌐 Translation services\\n\\nWhat would you like to try?';
            }}

            if (lowerMessage.includes('thank')) {{
                return 'You\\'re very welcome! 😊 Is there anything else I can help you with?';
            }}

            // Generic responses
            const responses = [
                'That\\'s interesting! Tell me more about that.',
                'I understand. How can I assist you further?',
                'Thanks for sharing that with me. What else is on your mind?',
                'I\\'m here to help! What would you like to know?',
                'That sounds important. How can I support you with that?'
            ];

            return responses[Math.floor(Math.random() * responses.length)];
        }}

        function quickAction(action) {{
            let message = '';

            switch(action) {{
                case 'schedule':
                    message = 'Help me plan my day';
                    break;
                case 'reminder':
                    message = 'Set a reminder for me';
                    break;
                case 'weather':
                    message = 'What\\'s the weather like today?';
                    break;
                case 'recipe':
                    message = 'Suggest a recipe for dinner';
                    break;
                case 'joke':
                    message = 'Tell me a joke';
                    break;
                case 'translate':
                    message = 'Translate this text to Spanish: Hello world';
                    break;
            }}

            document.getElementById('messageInput').value = message;
            sendMessage();
        }}

        // Welcome message in output
        document.getElementById('outputContent').textContent = '🤖 AI Assistant activated\\n\\n📊 Status: Online\\n💬 Conversations: 1\\n⚡ Response time: <2 seconds\\n\\nReady to assist!';
    </script>
</body>
</html>"""

    @staticmethod
    def _generate_iot_ui(title: str, themes: list) -> str:
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - IoT Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .device-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }}
        .device-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        .device-status {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }}
        .status-indicator {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }}
        .online {{ background: #28a745; }}
        .offline {{ background: #dc3545; }}
        .unknown {{ background: #ffc107; }}
        button {{
            background: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9em;
            margin: 2px;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #0056b3;
            transform: translateY(-1px);
        }}
        .sensor-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}
        .sensor-card {{
            background: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #dee2e6;
        }}
        .sensor-value {{
            font-size: 1.5em;
            font-weight: bold;
            color: #007bff;
        }}
        .automation-rules {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            margin: 0 30px 30px 30px;
            border-radius: 15px;
        }}
        .rule-item {{
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
        }}
        .output {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }}
        .output-content {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔗 {title}</h1>
            <p>IoT Control Center & Smart Home Hub - Tema: {', '.join(themes)}</p>
        </div>

        <div class="dashboard">
            <div class="device-card">
                <div class="device-status">
                    <h3>🌡️ Temperature Sensor</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <div class="sensor-value" id="temperature">24.5°C</div>
                <p>Humidity: 65%</p>
                <button onclick="adjustClimate('heat')">🔥 Heat</button>
                <button onclick="adjustClimate('cool')">❄️ Cool</button>
                <button onclick="setTemperature()">Set Temp</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>💡 Smart Lighting</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <div class="sensor-value" id="brightness">75%</div>
                <p>Living Room - Warm White</p>
                <button onclick="controlLights('on')">Turn On</button>
                <button onclick="controlLights('off')">Turn Off</button>
                <button onclick="setBrightness()">Brightness</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>🔒 Smart Lock</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <div class="sensor-value">Locked</div>
                <p>Last access: 2 hours ago</p>
                <button onclick="lockDoor()">Lock</button>
                <button onclick="unlockDoor()">Unlock</button>
                <button onclick="viewAccessLog()">Access Log</button>
            </div>

            <div class="device-card">
                <div class="device-status">
                    <h3>📷 Security Camera</h3>
                    <span><span class="status-indicator online"></span>Online</span>
                </div>
                <div class="sensor-value">Active</div>
                <p>Motion detected: None</p>
                <button onclick="viewCamera()">Live View</button>
                <button onclick="armSystem()">Arm</button>
                <button onclick="recordings()">Recordings</button>
            </div>

            <div class="device-card">
                <div class="sensor-grid">
                    <div class="sensor-card">
                        <h4>🌬️ Air Quality</h4>
                        <div class="sensor-value">Good</div>
                        <small>PM2.5: 12 µg/m³</small>
                    </div>
                    <div class="sensor-card">
                        <h4>🔊 Noise Level</h4>
                        <div class="sensor-value">45dB</div>
                        <small>Quiet environment</small>
                    </div>
                </div>
            </div>

            <div class="device-card">
                <div class="sensor-grid">
                    <div class="sensor-card">
                        <h4>⚡ Energy Usage</h4>
                        <div class="sensor-value">2.4kW</div>
                        <small>Daily: 18.5 kWh</small>
                    </div>
                    <div class="sensor-card">
                        <h4>💧 Water Flow</h4>
                        <div class="sensor-value">0.0 L/m</div>
                        <small>No active usage</small>
                    </div>
                </div>
            </div>
        </div>

        <div class="automation-rules">
            <h2>🤖 Smart Automation Rules</h2>
            <div class="rule-item">
                <strong>🌅 Morning Routine:</strong> Turn on lights at 7:00 AM when motion detected
            </div>
            <div class="rule-item">
                <strong>🌙 Evening Mode:</strong> Dim lights and lock doors at 11:00 PM
            </div>
            <div class="rule-item">
                <strong>🏠 Away Mode:</strong> Activate security when no motion for 30 minutes
            </div>
            <div class="rule-item">
                <strong>🌡️ Climate Control:</strong> Adjust thermostat based on weather forecast
            </div>
        </div>

        <div style="text-align: center; padding: 20px;">
            <button onclick="addDevice()">➕ Add Device</button>
            <button onclick="createAutomation()">⚙️ Create Rule</button>
            <button onclick="systemSettings()">🔧 Settings</button>
            <button onclick="viewAnalytics()">📊 Analytics</button>
        </div>

        <div class="output">
            <h3>IoT System Log</h3>
            <div class="output-content" id="outputContent">
                IoT Hub initialized. All systems online and monitoring.
            </div>
        </div>
    </div>

    <script>
        function controlLights(action) {{
            const output = document.getElementById('outputContent');
            if (action === 'on') {{
                output.textContent = `💡 Activating smart lighting system...\\n✅ All lights turned on\\n🌟 Brightness: 75%\\n🎨 Color: Warm White\\n`;
            }} else {{
                output.textContent = `💡 Deactivating smart lighting system...\\n✅ All lights turned off\\n🌙 Night mode activated\\n`;
            }}
        }}

        function setBrightness() {{
            const brightness = prompt('Set brightness (0-100%):', '75');
            if (brightness !== null) {{
                document.getElementById('brightness').textContent = brightness + '%';
                const output = document.getElementById('outputContent');
                output.textContent = `💡 Adjusting brightness to ${{brightness}}%...\\n✅ Lighting updated across all zones\\n`;
            }}
        }}

        function adjustClimate(mode) {{
            const output = document.getElementById('outputContent');
            const currentTemp = parseFloat(document.getElementById('temperature').textContent);
            let newTemp = currentTemp;

            if (mode === 'heat') {{
                newTemp = Math.min(30, currentTemp + 1);
                output.textContent = `🔥 Activating heating system...\\n🌡️ Temperature increasing to ${{newTemp}}°C\\n`;
            }} else {{
                newTemp = Math.max(16, currentTemp - 1);
                output.textContent = `❄️ Activating cooling system...\\n🌡️ Temperature decreasing to ${{newTemp}}°C\\n`;
            }}

            document.getElementById('temperature').textContent = newTemp + '°C';
        }}

        function setTemperature() {{
            const temp = prompt('Set target temperature (°C):', '24');
            if (temp !== null) {{
                const targetTemp = Math.max(16, Math.min(30, parseFloat(temp)));
                document.getElementById('temperature').textContent = targetTemp + '°C';
                const output = document.getElementById('outputContent');
                output.textContent = `🌡️ Setting thermostat to ${{targetTemp}}°C...\\n✅ Temperature control activated\\n🎯 Target reached in approximately 15 minutes\\n`;
            }}
        }}

        function lockDoor() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🔒 Activating smart lock...\\n✅ Front door locked\\n🔔 Security system armed\\n📱 Notification sent to all users\\n`;
        }}

        function unlockDoor() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🔓 Deactivating smart lock...\\n⚠️ Front door unlocked\\n👁️ Camera monitoring active\\n⏰ Auto-lock in 5 minutes\\n`;
        }}

        function viewAccessLog() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📋 Access Log - Last 24 hours:\\n\\n`;
            output.textContent += `🕐 08:15 - Front door unlocked (Key fob)\\n`;
            output.textContent += `🕐 12:30 - Garage door opened (App)\\n`;
            output.textContent += `🕐 18:45 - Back door accessed (PIN)\\n`;
            output.textContent += `🕐 22:10 - Security system armed (Auto)\\n\\n`;
            output.textContent += `🔐 Total events: 4\\n✅ No unauthorized access\\n`;
        }}

        function viewCamera() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📷 Accessing live camera feed...\\n✅ Connecting to security cameras\\n\\n`;
            output.textContent += `📍 Front Door: Motion detected - Delivery person\\n`;
            output.textContent += `📍 Backyard: No activity\\n`;
            output.textContent += `📍 Garage: Vehicle present\\n\\n`;
            output.textContent += `🎥 Recording: Active\\n🔄 Auto-refresh: Every 30 seconds\\n`;
        }}

        function armSystem() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🛡️ Arming security system...\\n✅ All cameras activated\\n🚨 Motion sensors enabled\\n🔊 Alarm system ready\\n📱 Emergency contacts notified\\n`;
        }}

        function recordings() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📹 Security Recordings:\\n\\n`;
            output.textContent += `📅 Today:\\n  - 08:15: Front door motion (2 min)\\n  - 12:30: Backyard activity (5 min)\\n  - 18:45: Delivery (3 min)\\n\\n`;
            output.textContent += `📅 Yesterday:\\n  - 19:20: Evening walk (1 min)\\n  - 22:10: Animal detection (30 sec)\\n\\n`;
            output.textContent += `💾 Storage used: 2.4 GB\\n🎬 Total recordings: 15\\n`;
        }}

        function addDevice() {{
            const output = document.getElementById('outputContent');
            output.textContent = `➕ Adding new IoT device...\\n🔍 Scanning for devices...\\n\\n`;
            output.textContent += `📡 Found devices:\\n  - Smart Thermostat (Living Room)\\n  - Motion Sensor (Hallway)\\n  - Smart Plug (Kitchen)\\n\\n`;
            output.textContent += `✅ Device "Smart Thermostat" added successfully\\n🔗 Connecting to network...\\n⚙️ Configuring settings...\\n🎯 Ready to use!\\n`;
        }}

        function createAutomation() {{
            const output = document.getElementById('outputContent');
            output.textContent = `⚙️ Creating new automation rule...\\n\\n`;
            output.textContent += `📝 Rule: "Good Morning Routine"\\n`;
            output.textContent += `⏰ Trigger: 7:00 AM daily\\n`;
            output.textContent += `🎬 Actions:\\n  - Turn on bedroom lights (50% brightness)\\n  - Start coffee maker\\n  - Play morning playlist\\n  - Send wake-up reminder\\n\\n`;
            output.textContent += `✅ Automation rule created and activated\\n`;
        }}

        function systemSettings() {{
            const output = document.getElementById('outputContent');
            output.textContent = `🔧 IoT System Settings:\\n\\n`;
            output.textContent += `🌐 Network: Connected (192.168.1.100)\\n`;
            output.textContent += `📊 Devices: 12 online, 2 offline\\n`;
            output.textContent += `💾 Storage: 75% used\\n`;
            output.textContent += `🔋 Battery levels: All >80%\\n`;
            output.textContent += `📡 Signal strength: Excellent\\n`;
            output.textContent += `🔄 Auto-backup: Daily at 2:00 AM\\n\\n`;
            output.textContent += `⚙️ Firmware: Up to date\\n`;
        }}

        function viewAnalytics() {{
            const output = document.getElementById('outputContent');
            output.textContent = `📊 IoT Analytics Dashboard:\\n\\n`;
            output.textContent += `📈 Energy Savings: 23% this month\\n`;
            output.textContent += `🏠 Occupancy: 85% of the time\\n`;
            output.textContent += `🔒 Security Events: 3 (all authorized)\\n`;
            output.textContent += `🌡️ Temperature Range: 18-26°C\\n`;
            output.textContent += `💡 Lighting Usage: 6.5 hours/day\\n\\n`;
            output.textContent += `💡 Insights:\\n  - Most active: Evening hours\\n  - Peak energy: 7-9 PM\\n  - Security: No incidents\\n`;
        }}

        // Simulate real-time updates
        setInterval(() => {{
            const tempEl = document.getElementById('temperature');
            const currentTemp = parseFloat(tempEl.textContent);
            const variation = (Math.random() - 0.5) * 0.2; // Small random variation
            const newTemp = Math.round((currentTemp + variation) * 10) / 10;
            tempEl.textContent = newTemp + '°C';
        }}, 10000);
    </script>
</body>
</html>"""