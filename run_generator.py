import argparse
import json
import random
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


def create_placeholder_file(project_dir: Path, language_key: str, metadata: dict) -> None:
    src_dir = project_dir / "src"
    src_dir.mkdir(parents=True, exist_ok=True)
    filename = SUPPORTED_LANGUAGE_FILES.get(language_key, "README.md")
    path = src_dir / filename
    if language_key == "python":
        content = (
            "# Prototype aplikasi\n"
            "def main():\n"
            f"    print('Running {metadata['title']}')\n"
            "    print('Tema: ' + ', '.join(metadata['themes']))\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
    elif language_key == "javascript":
        content = (
            "// Prototype aplikasi\n"
            f"console.log('Running {metadata['title']}');\n"
            "console.log('Tema: ' + ['" + "', '".join(metadata['themes']) + "']);\n"
        )
    elif language_key == "typescript":
        content = (
            "// Prototype aplikasi\n"
            f"console.log('Running {metadata['title']}');\n"
            "console.log('Tema: ' + [\n"
            + ", ".join(f'\"{theme}\"' for theme in metadata['themes'])
            + "]);\n"
        )
    elif language_key == "go":
        content = (
            "package main\n\n"
            "import \"fmt\"\n\n"
            "func main() {\n"
            f"    fmt.Println(\"Running {metadata['title']}\")\n"
            "}\n"
        )
    elif language_key == "rust":
        content = (
            "fn main() {\n"
            f"    println!(\"Running {metadata['title']}\");\n"
            "}\n"
        )
    elif language_key == "html":
        content = (
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            f"  <title>{metadata['title']}</title>\n"
            "  <meta charset=\"UTF-8\">\n"
            "</head>\n<body>\n"
            f"  <h1>{metadata['title']}</h1>\n"
            f"  <p>{metadata['description']}</p>\n"
            "</body>\n</html>\n"
        )
    else:
        content = (
            f"# {metadata['title']}\n\n"
            "Placeholder kode untuk bahasa yang dipilih.\n"
        )
    write_file(path, content)
    metadata["files"].append(str(path.relative_to(project_dir)))


def build_web_code_preview(language_key: str, metadata: dict) -> str:
    if language_key == "python":
        return (
            "# Prototype aplikasi\n"
            f"print('Running {metadata['title']}')\n"
            f"print('Tema: {', '.join(metadata['themes'])}')\n"
        )
    if language_key == "javascript" or language_key == "typescript":
        return (
            "// Prototype aplikasi\n"
            f"console.log('Running {metadata['title']}');\n"
            f"console.log('Tema: {', '.join(metadata['themes'])}');\n"
        )
    if language_key == "go":
        return (
            "package main\n\n"
            "import \"fmt\"\n\n"
            "func main() {\n"
            f"    fmt.Println(\"Running {metadata['title']}\")\n"
            "}\n"
        )
    if language_key == "rust":
        return (
            "fn main() {\n"
            f"    println!(\"Running {metadata['title']}\");\n"
            "}\n"
        )
    if language_key == "html":
        return (
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            f"  <title>{metadata['title']}</title>\n"
            "  <meta charset=\"UTF-8\">\n"
            "</head>\n<body>\n"
            f"  <h1>{metadata['title']}</h1>\n"
            f"  <p>{metadata['description']}</p>\n"
            "</body>\n</html>\n"
        )
    return "# Placeholder kode untuk bahasa yang dipilih.\n"


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
    html = build_web_ui_html(metadata)
    write_file(project_dir / "web" / "index.html", html)
    metadata["files"].append(str(Path("web") / "index.html"))


def run_generation(name: str | None = None) -> Path:
    themes = load_json("themes.json")
    languages = load_json("languages.json")["languages"]
    title_patterns = load_json("idea_patterns.json")["patterns"]

    combination = choose_theme_combination(themes)
    language = choose_language(languages, combination)
    idea = generate_idea(title_patterns, combination, language)

    slug = slugify(idea["title"])
    date_part = datetime.now().strftime("%Y%m%d")
    folder_name = f"{date_part}_{slug}" if not name else name
    project_dir = OUTPUT_DIR / folder_name
    project_dir.mkdir(parents=True, exist_ok=True)

    metadata = build_project_metadata(folder_name, combination, language, idea)
    readme_text = build_readme_contents(metadata)

    write_file(project_dir / "README.md", readme_text)
    create_placeholder_file(project_dir, language["key"], metadata)
    create_project_web_ui(project_dir, metadata)
    notes_text = AIWriter.build_notes(metadata)
    write_file(project_dir / "ai_notes.md", notes_text)
    build_manifest(project_dir, metadata)

    return project_dir


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a unique Master APP project")
    parser.add_argument("--name", type=str, help="Custom output folder name")
    return parser.parse_args()


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    args = parse_arguments()
    project_path = run_generation(args.name)
    print(f"Generated project: {project_path}")
