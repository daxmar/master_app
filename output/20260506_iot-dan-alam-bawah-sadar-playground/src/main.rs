// IoT dan Alam bawah sadar Playground
// Aplikasi lengkap dengan fitur: Koneksi perangkat IoT

use std::collections::HashMap;
use std::fs;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct IoTdanAlambawahsadarPlaygroundApp {
    title: String,
    themes: Vec<String>,
    features: Vec<String>,
    data_file: String,
}

impl IoTdanAlambawahsadarPlaygroundApp {
    fn new() -> Self {
        Self {
            title: "IoT dan Alam bawah sadar Playground".to_string(),
            themes: vec!["IoT".to_string(), "Alam bawah sadar".to_string(), "Nostalgia".to_string()],
            features: vec!["Koneksi perangkat IoT".to_string()],
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
    let app = IoTdanAlambawahsadarPlaygroundApp::new();
    app.main_menu();
}
