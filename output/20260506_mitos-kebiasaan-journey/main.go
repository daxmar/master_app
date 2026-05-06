package main

import (
  "bufio"
  "encoding/json"
  "fmt"
  "os"
  "path/filepath"
  "strings"
  "time"
)

type Habit struct {
  Name           string   `json:"name"`
  Description    string   `json:"description"`
  CompletedDates []string `json:"completed_dates"`
}

type JourneyData struct {
  Title     string  `json:"title"`
  Themes    []string `json:"themes"`
  CreatedAt string  `json:"created_at"`
  Habits    []Habit `json:"habits"`
}

const storageFile = "habits.json"

var mythQuotes = []string{
  "Dalam cerita lama, setiap ritual kecil menjaga keseimbangan bumi. Hari ini, kebiasaanmu adalah ritual baru.",
  "Gunung, hutan, dan sungai berbisik: satu tindakan kecil bisa merawat alam lebih lama dari mitos terkuat.",
  "Kekuatan nyata ada pada konsistensi — seperti legenda, kebiasaan baik bertahan melewati musim.",
}

func main() {
  path := filepath.Join(getWorkingDir(), storageFile)
  data, err := loadJourneyData(path)
  if err != nil {
    fmt.Println("Gagal memuat data:", err)
    return
  }

  showHeader(data.Title)
  reader := bufio.NewReader(os.Stdin)

  for {
    fmt.Println("\nPilih aksi:")
    fmt.Println("1) Lihat kebiasaan hari ini")
    fmt.Println("2) Tandai kebiasaan selesai")
    fmt.Println("3) Tambah kebiasaan baru")
    fmt.Println("4) Baca petuah mitos")
    fmt.Println("5) Keluar")
    fmt.Print("Masukkan nomor: ")

    choice, _ := reader.ReadString('\n')
    choice = strings.TrimSpace(choice)

    switch choice {
    case "1":
      listHabits(data)
    case "2":
      markHabitCompleted(data, path, reader)
    case "3":
      addHabit(data, path, reader)
    case "4":
      showMythQuote()
    case "5":
      fmt.Println("Sampai jumpa! Tetap jaga kebiasaan kecilnya.")
      return
    default:
      fmt.Println("Pilihan tidak dikenal. Coba lagi.")
    }
  }
}

func getWorkingDir() string {
  dir, err := os.Getwd()
  if err != nil {
    return "."
  }
  return dir
}

func loadJourneyData(path string) (*JourneyData, error) {
  raw, err := os.ReadFile(path)
  if err != nil {
    if os.IsNotExist(err) {
      return createDefaultJourneyData(path)
    }
    return nil, err
  }

  var data JourneyData
  if err := json.Unmarshal(raw, &data); err != nil {
    return nil, err
  }
  return &data, nil
}

func createDefaultJourneyData(path string) (*JourneyData, error) {
  data := &JourneyData{
    Title:     "Mitos Kebiasaan Journey",
    Themes:    []string{"Kebiasaan", "Mitos", "Eko"},
    CreatedAt: time.Now().Format(time.RFC3339),
    Habits: []Habit{
      {Name: "Minum air yang cukup", Description: "Jaga ritme tubuh dan pelihara alam dengan kesadaran.", CompletedDates: []string{}},
      {Name: "Bawa tas kain", Description: "Hindari sampah plastik dan rawat mitos lingkungan sehari-hari.", CompletedDates: []string{}},
      {Name: "Tanam satu tanaman kecil", Description: "Buat bumi lebih hijau dengan tindakan kecil setiap hari.", CompletedDates: []string{}},
    },
  }
  if err := saveJourneyData(path, data); err != nil {
    return nil, err
  }
  return data, nil
}

func saveJourneyData(path string, data *JourneyData) error {
  raw, err := json.MarshalIndent(data, "", "  ")
  if err != nil {
    return err
  }
  return os.WriteFile(path, raw, 0o644)
}

func showHeader(title string) {
  fmt.Println("==========================================")
  fmt.Println("   ", title)
  fmt.Println("==========================================")
  fmt.Println("Sebuah aplikasi ritus kebiasaan yang menghubungkan mitos, kebiasaan, dan ekologi.")
}

func listHabits(data *JourneyData) {
  today := time.Now().Format("2006-01-02")
  fmt.Println("\nKebiasaan saat ini:")
  for index, habit := range data.Habits {
    status := "belum selesai"
    if contains(habit.CompletedDates, today) {
      status = "sudah selesai"
    }
    fmt.Printf("%d) %s — %s [%s]\n", index+1, habit.Name, habit.Description, status)
  }
}

func markHabitCompleted(data *JourneyData, path string, reader *bufio.Reader) {
  listHabits(data)
  fmt.Print("Masukkan nomor kebiasaan yang ingin ditandai selesai: ")
  input, _ := reader.ReadString('\n')
  input = strings.TrimSpace(input)
  index := parseIndex(input) - 1
  if index < 0 || index >= len(data.Habits) {
    fmt.Println("Nomor tidak valid.")
    return
  }

  today := time.Now().Format("2006-01-02")
  habit := &data.Habits[index]
  if contains(habit.CompletedDates, today) {
    fmt.Println("Kebiasaan ini sudah ditandai selesai hari ini.")
    return
  }

  habit.CompletedDates = append(habit.CompletedDates, today)
  if err := saveJourneyData(path, data); err != nil {
    fmt.Println("Gagal menyimpan data:", err)
    return
  }
  fmt.Printf("Berhasil! '%s' ditandai selesai untuk %s.\n", habit.Name, today)
}

func addHabit(data *JourneyData, path string, reader *bufio.Reader) {
  fmt.Print("Masukkan nama kebiasaan baru: ")
  name, _ := reader.ReadString('\n')
  name = strings.TrimSpace(name)
  if name == "" {
    fmt.Println("Nama kebiasaan tidak boleh kosong.")
    return
  }
  fmt.Print("Masukkan deskripsi singkat: ")
  description, _ := reader.ReadString('\n')
  description = strings.TrimSpace(description)
  if description == "" {
    description = "Ritual baru untuk menjaga keseimbangan harian."
  }

  data.Habits = append(data.Habits, Habit{Name: name, Description: description, CompletedDates: []string{}})
  if err := saveJourneyData(path, data); err != nil {
    fmt.Println("Gagal menyimpan data:", err)
    return
  }
  fmt.Println("Kebiasaan baru berhasil ditambahkan.")
}

func showMythQuote() {
  quote := mythQuotes[time.Now().UnixNano()%int64(len(mythQuotes))]
  fmt.Println("\nPetuah Mitos:")
  fmt.Println(quote)
}

func parseIndex(input string) int {
  var num int
  fmt.Sscan(input, &num)
  return num
}

func contains(list []string, value string) bool {
  for _, item := range list {
    if item == value {
      return true
    }
  }
  return false
}
