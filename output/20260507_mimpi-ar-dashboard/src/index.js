// Mimpi AR Dashboard
// Aplikasi lengkap dengan fitur: Fitur dasar aplikasi, Pengaturan pengguna, Dashboard sederhana

class MimpiARDashboardApp {
    constructor() {
        this.title = "Mimpi AR Dashboard";
        this.themes = ['Komunikasi', 'Mimpi', 'AR'];
        this.features = ['Fitur dasar aplikasi', 'Pengaturan pengguna', 'Dashboard sederhana'];
        this.dataFile = "app_data.json";
    }

    loadData() {
        try {
            const data = localStorage.getItem(this.dataFile);
            return data ? JSON.parse(data) : {};
        } catch (e) {
            return {};
        }
    }

    saveData(data) {
        localStorage.setItem(this.dataFile, JSON.stringify(data));
    }

    runFeature(featureName) {
        console.log(`Menjalankan fitur: ${featureName}`);
        // Implementasi fitur di sini
    }

    mainMenu() {
        while (true) {
            console.log(`\n=== ${this.title} ===`);
            console.log("Fitur tersedia:");
            this.features.forEach((feature, i) => {
                console.log(`${i + 1}. ${feature}`);
            });
            console.log("0. Keluar");
            const choice = prompt("Pilih fitur: ");
            if (choice === "0") break;
            const idx = parseInt(choice) - 1;
            if (idx >= 0 && idx < this.features.length) {
                this.runFeature(this.features[idx]);
            } else {
                console.log("Pilihan tidak valid.");
            }
        }
    }
}

const app = new MimpiARDashboardApp();
app.main_menu();
