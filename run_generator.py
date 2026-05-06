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
    return {
        "name": name,
        "title": idea["title"],
        "description": idea["description"],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "themes": theme_combination,
        "language": language,
        "files": [],
        "keywords": [theme.lower() for theme in theme_combination],
    }


def build_readme_contents(metadata: dict) -> str:
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
        "- `src/` sebagai tempat kode sumber awal\n\n"
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
