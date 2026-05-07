// Eksperimen Ritme Companion
// Aplikasi lengkap dengan fitur: Fitur dasar aplikasi, Pengaturan pengguna, Dashboard sederhana

use std::collections::HashMap;
use std::fs;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct EksperimenRitmeCompanionApp {
    title: String,
    themes: Vec<String>,
    features: Vec<String>,
    data_file: String,
}

impl EksperimenRitmeCompanionApp {
    fn new() -> Self {
        Self {
            title: "Eksperimen Ritme Companion".to_string(),
            themes: vec!["Eksperimen".to_string(), "Futuristik".to_string(), "Ritme".to_string()],
            features: vec!["Fitur dasar aplikasi".to_string(), "Pengaturan pengguna".to_string(), "Dashboard sederhana".to_string()],
            data_file: "app_data.json".to_string(),
        }
    }

    fn load_data(&self) -> HashMap<String, serde_json::Value> {
        if let Ok(contents) = fs::read_to_string(&self.data_file) {
            if let Ok(data) = serde_json::from_str(&contents) {
                data
            } else {
                HashMap::new()
            }
        } else {
            HashMap::new()
        }
    }

    fn save_data(&self, data: &HashMap<String, serde_json::Value>) {
        if let Ok(json) = serde_json::to_string_pretty(data) {
            let _ = fs::write(&self.data_file, json);
        }
    }

    fn run_feature(&self, feature_name: &str) {
        println!("Menjalankan fitur: {}", feature_name);
        // Implementasi fitur di sini
    }

    fn main_menu(&self) {
        loop {
            println!("\n=== {} ===", self.title);
            println!("Fitur tersedia:");
            for (i, feature) in self.features.iter().enumerate() {
                println!("{}. {}", i + 1, feature);
            }
            println!("0. Keluar");
            let mut input = String::new();
            std::io::stdin().read_line(&mut input).unwrap();
            let choice: usize = match input.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
            if choice == 0 {
                break;
            }
            if choice > 0 && choice <= self.features.len() {
                self.run_feature(&self.features[choice - 1]);
            } else {
                println!("Pilihan tidak valid.");
            }
        }
    }
}

fn main() {
    let app = EksperimenRitmeCompanionApp::new();
    app.main_menu();
}
