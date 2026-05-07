// Kesehatan Paralel Portal
// Aplikasi lengkap dengan fitur: Pelacakan kesehatan harian

use std::collections::HashMap;
use std::fs;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct KesehatanParalelPortalApp {
    title: String,
    themes: Vec<String>,
    features: Vec<String>,
    data_file: String,
}

impl KesehatanParalelPortalApp {
    fn new() -> Self {
        Self {
            title: "Kesehatan Paralel Portal".to_string(),
            themes: vec!["Kesehatan".to_string(), "Komedi".to_string(), "Paralel".to_string()],
            features: vec!["Pelacakan kesehatan harian".to_string()],
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
    let app = KesehatanParalelPortalApp::new();
    app.main_menu();
}
