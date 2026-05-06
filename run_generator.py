import argparse
import json
import random
import sys
from datetime import datetime
from pathlib import Path

from ai_agent import AIWriter

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"

SUPPORTED_LANGUAGE_FILES = {
    "python": "main.py",
    "javascript": "index.js",
    "typescript": "index.ts",
    "go": "main.go",
    "rust": "main.rs",
    "html": "index.html",
    "java": "Main.java",
    "ruby": "main.rb",
    "php": "index.php",
}


def load_json(filename: str) -> dict:
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def slugify(value: str) -> str:
    cleaned = value.lower().replace(" ", "-")
    allowed = [c for c in cleaned if c.isalnum() or c == "-"]
    slug = "".join(allowed).strip("-")
    return slug[:48]


def choose_theme_combination(themes: dict) -> list[str]:
    core = random.choice(themes["core"])
    abstract = random.choice(themes["abstract"])
    extra = random.choice(themes["extra"])
    return [core, abstract, extra]


def choose_language(language_profiles: list[dict], theme_combination: list[str]) -> dict:
    scores = []
    for profile in language_profiles:
        score = 0
        for theme in theme_combination:
            if theme.lower() in profile.get("preferred_themes", []):
                score += 2
        score += random.random()
        scores.append((score, profile))
    return max(scores, key=lambda item: item[0])[1]


def generate_idea(title_patterns: list[str], theme_combination: list[str], language: dict) -> dict:
    title_template = random.choice(title_patterns)
    title = title_template.format(
        theme=theme_combination[0],
        style=theme_combination[1],
        twist=theme_combination[2],
        language=language["name"],
    )
    title = title.replace("  ", " ").strip()
    description = (
        f"Aplikasi {title.lower()} yang menyatukan tema {theme_combination[0]}, "
        f"dengan nuansa {theme_combination[1]} dan fungsi {theme_combination[2]}. "
        f"Dibangun sebagai prototype sederhana menggunakan {language['name']} untuk mengeksplorasi ide kreatif dan kegunaan sehari-hari."
    )
    return {"title": title, "description": description}


def build_project_metadata(name: str, theme_combination: list[str], language: dict, idea: dict) -> dict:
    language_file = SUPPORTED_LANGUAGE_FILES.get(language["key"], "main.txt")
    language_data = {**language, "file": language_file}
    return {
        "name": name,
        "title": idea["title"],
        "description": idea["description"],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "themes": theme_combination,
        "language": language_data,
        "files": [],
        "keywords": [theme.lower() for theme in theme_combination],
    }


def build_readme_contents(metadata: dict) -> str:
    web_hint = (
        "- Buka `web/index.html` di browser untuk melihat UI web proyek dan instruksi run.\n"
        if metadata["language"]["key"] != "html"
        else "- Buka `web/index.html` di browser untuk melihat aplikasi HTML langsung.\n"
    )
    return (
        f"# {metadata['title']}\n\n"
        f"{metadata['description']}\n\n"
        "## Tema\n"
        + "\n".join(f"- {theme}" for theme in metadata["themes"]) + "\n\n"
        "## Bahasa Pemrograman\n"
        f"- {metadata['language']['name']}\n\n"
        "## Struktur Awal\n"
        "- `project.json` sebagai metadata proyek\n"
        "- `ai_notes.md` sebagai catatan AI Agent\n"
        "- `src/` sebagai tempat kode sumber awal\n"
        "- `web/` sebagai UI web lokal untuk preview dan prosedur run\n\n"
        "## Web UI\n"
        "- Buka `web/index.html` di browser untuk melihat info proyek dan run instructions.\n"
        f"{web_hint}\n"
        "## Cara Menjalankan\n"
        + "```\n"
        + f"# Buka folder proyek dan jalankan kode sesuai bahasa {metadata['language']['name']}\n"
        + "```\n"
    )


def build_manifest(project_dir: Path, metadata: dict) -> None:
    manifest_path = project_dir / "project.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2, ensure_ascii=False)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_placeholder_file(project_dir: Path, language_key: str, metadata: dict, code_level: str = "basic") -> None:
    src_dir = project_dir / "src"
    src_dir.mkdir(parents=True, exist_ok=True)
    filename = SUPPORTED_LANGUAGE_FILES.get(language_key, "README.md")
    path = src_dir / filename

    if code_level == "full":
        content = AIWriter.generate_full_features(metadata)
    else:
        content = AIWriter.generate_basic_code(metadata)

    write_file(path, content)
    metadata["files"].append(str(path.relative_to(project_dir)))


def build_web_code_preview(language_key: str, metadata: dict) -> str:
    # Gunakan AI Agent untuk generate preview kode
    return AIWriter.generate_basic_code(metadata)


def build_web_ui_html(metadata: dict) -> str:
    metadata_json = json.dumps(metadata, ensure_ascii=False)
    code_preview = build_web_code_preview(metadata["language"]["key"], metadata)
    run_commands = {
        "python": "python ../src/main.py",
        "javascript": "node ../src/index.js",
        "typescript": "npx ts-node ../src/index.ts",
        "go": "go run ../src/main.go",
        "rust": "rustc ../src/main.rs -o ../run-app && ../run-app",
        "html": "Buka ../src/index.html untuk melihat aplikasi langsung."
    }
    run_command = run_commands.get(metadata["language"]["key"], "Jalankan file sumber sesuai bahasa proyek.")
    return (
        f"<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"  <title>{metadata['title']} Web UI</title>\n"
        "  <style>body{font-family:Inter,system-ui,sans-serif;background:#f9fafb;color:#111827;margin:0;padding:24px;}"
        "  .container{max-width:980px;margin:0 auto;}"
        "  h1{margin-bottom:8px;}"
        "  .card{background:#ffffff;border-radius:20px;box-shadow:0 18px 48px rgba(15,23,42,.08);padding:24px;margin-top:20px;}"
        "  .grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px;}"
        "  pre{background:#111827;color:#f8fafc;padding:16px;border-radius:16px;overflow:auto;white-space:pre-wrap;word-break:break-word;}"
        "  button{border:none;padding:12px 18px;border-radius:12px;background:#2563eb;color:#fff;cursor:pointer;transition:all .15s ease;}"
        "  button:hover{background:#1d4ed8;}"
        "  iframe{width:100%;height:420px;border:1px solid #d1d5db;border-radius:16px;}"
        "  .run-output{background:#f3f4f6;padding:16px;border-radius:16px;white-space:pre-wrap;min-height:120px;}"
        "  @media(max-width:720px){.grid{grid-template-columns:1fr;}}</style>\n"
        "</head>\n<body>\n"
        "  <div class=\"container\">\n"
        f"    <h1>{metadata['title']} - Web UI</h1>\n"
        f"    <p>{metadata['description']}</p>\n"
        "    <div class=\"card\">\n"
        "      <h2>Detail Proyek</h2>\n"
        "      <div class=\"grid\">\n"
        "        <div>\n"
        f"          <p><strong>Folder:</strong> {metadata['name']}</p>\n"
        f"          <p><strong>Bahasa:</strong> {metadata['language']['name']}</p>\n"
        f"          <p><strong>File awal:</strong> {metadata['language']['file']}</p>\n"
        f"          <p><strong>Run command:</strong> <code>{run_command}</code></p>\n"
        "        </div>\n"
        "        <div>\n"
        f"          <p><strong>Tema:</strong></p>\n"
        f"          <ul>{''.join(f'<li>{theme}</li>' for theme in metadata['themes'])}</ul>\n"
        "        </div>\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class=\"card\">\n"
        "      <h2>Run UI</h2>\n"
        f"      <p>Gunakan halaman ini untuk melihat detail dan prosedur menjalankan aplikasi.</p>\n"
        f"      <p><a href=\"prototype.html\" target=\"_blank\">🔗 Buka Prototype UI Lengkap</a></p>\n"
        "      <div id=\"appPreview\"></div>\n"
        "      <div id=\"runArea\"></div>\n"
        "    </div>\n"
        "    <div class=\"card\">\n"
        "      <h2>Code Preview</h2>\n"
        f"      <pre>{code_preview}</pre>\n"
        "    </div>\n"
        "  </div>\n"
        "  <script>\n"
        f"const metadata = {metadata_json};\n"
        f"const codePreview = {json.dumps(code_preview, ensure_ascii=False)};\n"
        "const runArea = document.getElementById('runArea');\n"
        "function showHtmlPreview() {\n"
        "  runArea.innerHTML = '<h3>Preview HTML</h3><iframe src=\"../src/index.html\"></iframe>';\n"
        "}\n"
        "function showJsSimulation() {\n"
        "  runArea.innerHTML = '<button id=\"runButton\">Simulasikan Run</button><div class=\"run-output\" id=\"outputArea\">Tekan tombol untuk melihat output.</div>';\n"
        "  document.getElementById('runButton').addEventListener('click', function() {\n"
        "    document.getElementById('outputArea').textContent = 'Running ' + metadata.title + '\\nTema: ' + metadata.themes.join(', ');\n"
        "  });\n"
        "}\n"
        "function showCommandNote(command) {\n"
        "  runArea.innerHTML = '<p>Jalankan perintah di atas untuk mengeksekusi proyek di terminal atau environment yang sesuai.</p>';\n"
        "}\n"
        "if (metadata.language.key === 'html') { showHtmlPreview(); } else if (metadata.language.key === 'javascript') { showJsSimulation(); } else { showCommandNote(); }\n"
        "</script>\n"
        "</body>\n</html>\n"
    )


def create_project_web_ui(project_dir: Path, metadata: dict) -> None:
    web_dir = project_dir / "web"
    web_dir.mkdir(parents=True, exist_ok=True)
    ui_html = build_web_ui_html(metadata)
    write_file(web_dir / "index.html", ui_html)

    # Create full UI prototype
    prototype_html = AIWriter.generate_ui_prototype(metadata)
    write_file(web_dir / "prototype.html", prototype_html)

    metadata["files"].append(str(Path("web") / "index.html"))
    metadata["files"].append(str(Path("web") / "prototype.html"))


def create_features_folders(project_dir: Path, metadata: dict) -> None:
    features_dir = project_dir / "features"
    features_dir.mkdir(parents=True, exist_ok=True)

    # Determine features based on themes
    features = []
    if "Kesehatan" in metadata["themes"]:
        features.append("health-tracking")
    if "Produktivitas" in metadata["themes"]:
        features.append("task-management")
    if "IoT" in metadata["themes"]:
        features.append("iot-connection")
    if "AI" in metadata["themes"]:
        features.append("ai-recommendation")
    if "Musik" in metadata["themes"]:
        features.append("music-player")
    if "Game" in metadata["themes"]:
        features.append("mini-game")
    if not features:
        features = ["basic-feature", "user-settings", "dashboard"]

    for feature in features:
        feature_dir = features_dir / feature
        feature_dir.mkdir(parents=True, exist_ok=True)

        # Create feature code
        feature_code = generate_feature_code(feature, metadata["language"]["key"], metadata)
        write_file(feature_dir / f"{feature}.py", feature_code)  # Assuming Python for simplicity, adjust for other languages

        # Create feature UI
        feature_ui = generate_feature_ui(feature, metadata)
        write_file(feature_dir / "index.html", feature_ui)

        # Create feature README
        feature_readme = f"# {feature.replace('-', ' ').title()}\n\nImplementasi fitur {feature} untuk aplikasi {metadata['title']}.\n\n## Cara menjalankan\n- Jalankan `{feature}.py` untuk backend\n- Buka `index.html` untuk UI web"
        write_file(feature_dir / "README.md", feature_readme)


def preview_candidate(metadata: dict) -> None:
    print("\n=== Preview Aplikasi ===")
    print(f"Judul        : {metadata['title']}")
    print(f"Deskripsi    : {metadata['description']}")
    print(f"Tema         : {', '.join(metadata['themes'])}")
    print(f"Bahasa       : {metadata['language']['name']}")
    print(f"File awal    : {metadata['language']['file']}")
    print(f"Folder tujuan: {metadata['name']}")
    print("========================\n")


def ensure_unique_folder_name(base_name: str) -> str:
    candidate = base_name
    counter = 1
    while (OUTPUT_DIR / candidate).exists():
        candidate = f"{base_name}_{counter}"
        counter += 1
    return candidate


def build_candidate(name: str | None = None) -> dict:
    themes = load_json("themes.json")
    languages = load_json("languages.json")["languages"]
    title_patterns = load_json("idea_patterns.json")["patterns"]

    combination = choose_theme_combination(themes)
    language = choose_language(languages, combination)
    idea = generate_idea(title_patterns, combination, language)

    slug = slugify(idea["title"])
    date_part = datetime.now().strftime("%Y%m%d")
    folder_name = f"{date_part}_{slug}" if not name else name
    folder_name = ensure_unique_folder_name(folder_name)

    return build_project_metadata(folder_name, combination, language, idea)


def create_project_files(metadata: dict, code_level: str = "basic") -> Path:
    project_dir = OUTPUT_DIR / metadata["name"]
    project_dir.mkdir(parents=True, exist_ok=True)
    write_file(project_dir / "README.md", build_readme_contents(metadata))
    create_placeholder_file(project_dir, metadata["language"]["key"], metadata, code_level)
    create_project_web_ui(project_dir, metadata)
    create_features_folders(project_dir, metadata)
    write_file(project_dir / "ai_notes.md", AIWriter.build_notes(metadata))
    build_manifest(project_dir, metadata)
    return project_dir


def run_generation(name: str | None = None, auto: bool = False) -> Path | None:
    while True:
        metadata = build_candidate(name)
        if auto:
            return create_project_files(metadata, "full")

        preview_candidate(metadata)
        answer = input("Apakah ingin membuat aplikasi ini? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            level_choice = input("Pilih level kode (basic/full): ").strip().lower()
            if level_choice not in {"basic", "full"}:
                level_choice = "basic"
            return create_project_files(metadata, level_choice)
        if answer in {"n", "no"}:
            again = input("Coba ide lain? (y/n): ").strip().lower()
            if again in {"y", "yes"}:
                continue
            print("Tidak ada proyek dibuat.")
            return None
        print("Masukkan y atau n.")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a unique Master APP project")
    parser.add_argument("--name", type=str, help="Custom output folder name")
    parser.add_argument("--auto", action="store_true", help="Buat proyek langsung tanpa konfirmasi")
    return parser.parse_args()


def generate_feature_code(feature: str, language_key: str, metadata: dict) -> str:
    title = metadata["title"]
    if language_key == "python":
        if feature == "health-tracking":
            return f"""# {title} - Health Tracking Feature
import json
import datetime

class HealthTracker:
    def __init__(self):
        self.data_file = "health_data.json"

    def log_activity(self, activity_type, value):
        data = self.load_data()
        today = datetime.date.today().isoformat()
        if today not in data:
            data[today] = {{}}
        data[today][activity_type] = value
        self.save_data(data)
        print(f"Logged {{activity_type}}: {{value}}")

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except:
            return {{}}

    def save_data(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

if __name__ == "__main__":
    tracker = HealthTracker()
    tracker.log_activity("steps", 8432)
    print("Health tracking feature ready!")
"""
        elif feature == "task-management":
            return f"""# {title} - Task Management Feature
import json

class TaskManager:
    def __init__(self):
        self.tasks_file = "tasks.json"

    def add_task(self, task):
        tasks = self.load_tasks()
        tasks.append({{"task": task, "done": False}})
        self.save_tasks(tasks)

    def list_tasks(self):
        tasks = self.load_tasks()
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "○"
            print(f"{{i}}. {{status}} {{task['task']}}")

    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        except:
            return []

    def save_tasks(self, tasks):
        with open(self.tasks_file, 'w') as f:
            json.dump(tasks, f, indent=2)

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Review code")
    manager.list_tasks()
"""
        # Add more features...
        else:
            return f"# {title} - {feature} Feature\n# Implementasi fitur {feature}\nprint('Feature {feature} executed!')"
    else:
        return f"# {title} - {feature} Feature\n# Placeholder for {language_key}"


def generate_feature_ui(feature: str, metadata: dict) -> str:
    title = metadata["title"]
    feature_title = feature.replace('-', ' ').title()

    if feature == "health-tracking":
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title} - {feature_title}</title>
    <style>body{{font-family:Arial; margin:20px;}} .log{{margin:10px 0;}}</style>
</head>
<body>
    <h1>{feature_title}</h1>
    <div>
        <input type="number" id="steps" placeholder="Steps today">
        <button onclick="logSteps()">Log Steps</button>
    </div>
    <div id="logs"></div>
    <script>
        function logSteps() {{
            const steps = document.getElementById('steps').value;
            document.getElementById('logs').innerHTML += `<div class="log">Logged {{steps}} steps</div>`;
        }}
    </script>
</body>
</html>"""
    elif feature == "task-management":
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title} - {feature_title}</title>
    <style>body{{font-family:Arial; margin:20px;}} .task{{margin:5px 0;}}</style>
</head>
<body>
    <h1>{feature_title}</h1>
    <input type="text" id="newTask" placeholder="New task">
    <button onclick="addTask()">Add Task</button>
    <div id="tasks"></div>
    <script>
        let tasks = [];
        function addTask() {{
            const task = document.getElementById('newTask').value;
            tasks.push(task);
            document.getElementById('newTask').value = '';
            renderTasks();
        }}
        function renderTasks() {{
            document.getElementById('tasks').innerHTML = tasks.map(t => `<div class="task">○ {{t}}</div>`).join('');
        }}
    </script>
</body>
</html>"""
    else:
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title} - {feature_title}</title>
</head>
<body>
    <h1>{feature_title}</h1>
    <p>UI untuk fitur {feature}.</p>
</body>
</html>"""


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    args = parse_arguments()
    project_path = run_generation(args.name, auto=args.auto)
    if project_path:
        print(f"Generated project: {project_path}")
    else:
        print("Tidak ada proyek yang dibuat.")
