package main

import (
    "encoding/json"
    "fmt"
    "os"
)

// Data Horor Memory
// Aplikasi lengkap dengan fitur: Fitur dasar aplikasi, Pengaturan pengguna, Dashboard sederhana

type DataHororMemoryApp struct {
    Title    string
    Themes   []string
    Features []string
    DataFile string
}

func NewDataHororMemoryApp() *DataHororMemoryApp {
    return &DataHororMemoryApp{
        Title:    "Data Horor Memory",
        Themes:   []string{"Data", "Horor", "VR"},
        Features: []string{"Fitur dasar aplikasi", "Pengaturan pengguna", "Dashboard sederhana"},
        DataFile: "app_data.json",
    }
}

func (app *DataHororMemoryApp) LoadData() map[string]interface{} {
    data := make(map[string]interface{})
    if file, err := os.Open(app.DataFile); err == nil {
        defer file.Close()
        json.NewDecoder(file).Decode(&data)
    }
    return data
}

func (app *DataHororMemoryApp) SaveData(data map[string]interface{}) {
    if file, err := os.Create(app.DataFile); err == nil {
        defer file.Close()
        json.NewEncoder(file).Encode(data)
    }
}

func (app *DataHororMemoryApp) RunFeature(featureName string) {
    fmt.Printf("Menjalankan fitur: %s\n", featureName)
    // Implementasi fitur di sini
}

func (app *DataHororMemoryApp) MainMenu() {
    for {
        fmt.Printf("\n=== %s ===\n", app.Title)
        fmt.Println("Fitur tersedia:")
        for i, feature := range app.Features {
            fmt.Printf("%d. %s\n", i+1, feature)
        }
        fmt.Println("0. Keluar")
        var choice int
        fmt.Print("Pilih fitur: ")
        fmt.Scan(&choice)
        if choice == 0 {
            break
        }
        if choice > 0 && choice <= len(app.Features) {
            app.RunFeature(app.Features[choice-1])
        } else {
            fmt.Println("Pilihan tidak valid.")
        }
    }
}

func main() {
    app := NewDataHororMemoryApp()
    app.MainMenu()
}
