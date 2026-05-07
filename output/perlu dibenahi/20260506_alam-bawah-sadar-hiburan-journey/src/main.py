# Alam bawah sadar Hiburan Journey
# Aplikasi lengkap dengan fitur: Fitur dasar aplikasi, Pengaturan pengguna, Dashboard sederhana

import json
import os

class AlambawahsadarHiburanJourneyApp:
    def __init__(self):
        self.title = "Alam bawah sadar Hiburan Journey"
        self.themes = ['Hiburan', 'Alam bawah sadar', 'Ritual']
        self.features = ['Fitur dasar aplikasi', 'Pengaturan pengguna', 'Dashboard sederhana']
        self.data_file = "app_data.json"

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def run_feature(self, feature_name):
        print(f"Menjalankan fitur: {feature_name}")
        # Implementasi fitur di sini

    def main_menu(self):
        while True:
            print(f"\n=== {self.title} ===")
            print("Fitur tersedia:")
            for i, feature in enumerate(self.features, 1):
                print(f"{i}. {feature}")
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
    app = AlambawahsadarHiburanJourneyApp()
    app.main_menu()
