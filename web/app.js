const coreThemes = [
  "Produktivitas",
  "Edukasi",
  "Hiburan",
  "Kesehatan",
  "Sosial",
  "Kreativitas",
  "Keuangan",
  "Musik",
  "Seni",
  "Game",
  "Data",
  "Komunikasi",
  "IoT",
  "Alam",
  "Kebiasaan",
  "Waktu",
  "Keamanan",
  "Kebudayaan",
  "Bahasa",
  "Eksperimen"
];

const abstractThemes = [
  "Alam bawah sadar",
  "Mimpi",
  "Horor",
  "Retro",
  "Minimalis",
  "Futuristik",
  "Steampunk",
  "Fantasi",
  "Cyberpunk",
  "Meditasi",
  "Sains",
  "Komedi",
  "Paradox",
  "Makhluk",
  "Urban",
  "Kosmik",
  "Ritual",
  "Mitos",
  "Fragmented",
  "Koneksi"
];

const extraThemes = [
  "AI",
  "AR",
  "VR",
  "IoT",
  "Neural",
  "Ritme",
  "Sinyal",
  "Jaringan",
  "Kolektif",
  "Polaris",
  "Nostalgia",
  "Transformer",
  "Satir",
  "Kuantum",
  "Orbital",
  "Ritual",
  "Eko",
  "Sudut pandang",
  "Paralel",
  "Wahyu"
];

const languages = [
  { key: "python", name: "Python", file: "main.py" },
  { key: "javascript", name: "JavaScript", file: "index.js" },
  { key: "typescript", name: "TypeScript", file: "index.ts" },
  { key: "go", name: "Go", file: "main.go" },
  { key: "rust", name: "Rust", file: "main.rs" },
  { key: "html", name: "HTML", file: "index.html" }
];

const titlePatterns = [
  "{theme} {style} Explorer",
  "{theme} {twist} Companion",
  "{theme} dan {style} Playground",
  "{style} {theme} Studio",
  "{twist} {theme} Lab",
  "{theme} {style} Memory",
  "{style} {theme} Journey",
  "{theme} {twist} Portal",
  "{theme} {style} Assistant",
  "{style} {twist} Dashboard"
];

const dom = {
  generateButton: document.getElementById("generateButton"),
  downloadReadme: document.getElementById("downloadReadme"),
  downloadManifest: document.getElementById("downloadManifest"),
  downloadNotes: document.getElementById("downloadNotes"),
  result: document.getElementById("result"),
  projectTitle: document.getElementById("projectTitle"),
  projectDescription: document.getElementById("projectDescription"),
  themeList: document.getElementById("themeList"),
  languageName: document.getElementById("languageName"),
  entryFile: document.getElementById("entryFile"),
  codePreview: document.getElementById("codePreview"),
  projectFolder: document.getElementById("projectFolder"),
  projectDate: document.getElementById("projectDate")
};

let currentProject = null;

function randomChoice(list) {
  return list[Math.floor(Math.random() * list.length)];
}

function slugify(value) {
  const cleaned = value.toLowerCase().replace(/\s+/g, "-");
  return cleaned.replace(/[^a-z0-9-]/g, "").replace(/-+/g, "-").replace(/^-|-$/g, "");
}

function buildIdea(themeCombo, language) {
  const template = randomChoice(titlePatterns);
  const title = template
    .replace("{theme}", themeCombo[0])
    .replace("{style}", themeCombo[1])
    .replace("{twist}", themeCombo[2])
    .replace(/\s+/g, " ")
    .trim();

  const description = `Aplikasi ${title.toLowerCase()} yang menyatukan tema ${themeCombo.join(", ")}. Dibangun sebagai prototype sederhana menggunakan ${language.name} untuk mengeksplorasi ide kreatif dan kegunaan sehari-hari.`;
  return { title, description };
}

function buildCodePreview(languageKey, metadata) {
  if (languageKey === "python") {
    return `# Prototype aplikasi\ndef main():\n    print('Running ${metadata.title}')\n    print('Tema: ${metadata.themes.join(", ")}')\n\nif __name__ == '__main__':\n    main()`;
  }
  if (languageKey === "javascript") {
    return `// Prototype aplikasi\nconsole.log('Running ${metadata.title}');\nconsole.log('Tema: ${metadata.themes.join(" | ")}');`;
  }
  if (languageKey === "typescript") {
    return `// Prototype aplikasi\nconsole.log('Running ${metadata.title}');\nconsole.log('Tema: ${metadata.themes.join(" | ")}');`;
  }
  if (languageKey === "go") {
    return `package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Running ${metadata.title}\")\n}`;
  }
  if (languageKey === "rust") {
    return `fn main() {\n    println!(\"Running ${metadata.title}\");\n}`;
  }
  if (languageKey === "html") {
    return `<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>${metadata.title}</title>\n</head>\n<body>\n  <h1>${metadata.title}</h1>\n  <p>${metadata.description}</p>\n</body>\n</html>`;
  }
  return "Placeholder kode untuk bahasa yang dipilih.";
}

function createDownloadFile(name, content) {
  const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = name;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

function buildManifest(metadata) {
  return JSON.stringify(metadata, null, 2);
}

function generateProject() {
  const themeCombo = [randomChoice(coreThemes), randomChoice(abstractThemes), randomChoice(extraThemes)];
  const language = randomChoice(languages);
  const idea = buildIdea(themeCombo, language);
  const date = new Date();
  const datePart = date.toISOString().slice(0, 10).replace(/-/g, "");
  const folderName = `${datePart}_${slugify(idea.title)}`;

  const metadata = {
    name: folderName,
    title: idea.title,
    description: idea.description,
    created_at: new Date().toISOString(),
    themes: themeCombo,
    language: language,
    files: [language.file],
    keywords: themeCombo.map((theme) => theme.toLowerCase())
  };

  currentProject = metadata;

  dom.projectTitle.textContent = metadata.title;
  dom.projectDescription.textContent = metadata.description;
  dom.themeList.innerHTML = metadata.themes.map((theme) => `<li>${theme}</li>`).join("");
  dom.languageName.textContent = metadata.language.name;
  dom.entryFile.textContent = metadata.language.file;
  dom.codePreview.textContent = buildCodePreview(metadata.language.key, metadata);
  dom.projectFolder.textContent = metadata.name;
  dom.projectDate.textContent = new Date(metadata.created_at).toLocaleString();

  dom.result.classList.remove("hidden");
  dom.downloadReadme.disabled = false;
  dom.downloadManifest.disabled = false;
  dom.downloadNotes.disabled = false;
}

function init() {
  dom.generateButton.addEventListener("click", generateProject);
  dom.downloadReadme.addEventListener("click", () => {
    if (!currentProject) return;
    const content = `# ${currentProject.title}\n\n${currentProject.description}\n\n## Tema\n${currentProject.themes.map((item) => `- ${item}`).join("\n")}\n\n## Bahasa\n- ${currentProject.language.name}\n\n## File Awal\n- ${currentProject.language.file}\n`;
    createDownloadFile("README.md", content);
  });

  dom.downloadManifest.addEventListener("click", () => {
    if (!currentProject) return;
    createDownloadFile("project.json", buildManifest(currentProject));
  });

  dom.downloadNotes.addEventListener("click", () => {
    if (!currentProject) return;
    const content = `# Catatan AI Agent untuk ${currentProject.title}\n\nTanggal pembuatan: ${new Date(currentProject.created_at).toISOString()}\n\nIde utama: gabungan tema ${currentProject.themes.join(", ")}.\nBahasa utama: ${currentProject.language.name}.\n\n## Fokus eksperimen\n- Eksplorasi ide prototipe dengan struktur ringkas.\n- Pastikan output bisa dimodifikasi menjadi aplikasi nyata.\n- Tetap sederhana agar mudah dikembangkan besok.\n\n## Rekomendasi selanjutnya\n1. Evaluasi apakah ide ini mendukung pengalaman pengguna praktis.\n2. Tambahkan dokumentasi tambahan jika kamu ingin mengubahnya menjadi produk.\n3. Jika memilih ${currentProject.language.name}, mulai dari file ${currentProject.language.file}.\n`;
    createDownloadFile("ai_notes.md", content);
  });
}

init();
