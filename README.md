# 🧠 ChEmotion: Chat Emotion Detector

**ChEmotion** adalah aplikasi berbasis Flutter yang mendeteksi emosi stres dari screenshot percakapan (chat) menggunakan OCR dan model Machine Learning.

---

## 🚀 Fitur Utama

- 📸 Unggah screenshot percakapan dari galeri
- 🔍 Ekstraksi teks menggunakan OCR (Tesseract)
- 🧠 Deteksi stres dari teks dengan model LSTM
- 📊 Menampilkan label `stres / tidak stres` dengan confidence score

---

## 🏗️ Arsitektur Teknologi

```mermaid
graph TD
A[Flutter App] --> B[Upload Screenshot]
B --> C[Flask API]
C --> D[Tesseract OCR]
D --> E[Preprocessing + Tokenizer]
E --> F[Model LSTM (.h5)]
F --> G[Label & Confidence]
G --> H[Return JSON to Flutter]
```

---

## 🧰 Teknologi yang Digunakan

| Komponen     | Teknologi                      |
| ------------ | ------------------------------ |
| Frontend     | Flutter, Dart                  |
| Backend      | Flask (Python)                 |
| OCR          | Tesseract OCR                  |
| ML Model     | TensorFlow/Keras (LSTM)        |
| Format Model | `.h5` model + `.pkl` tokenizer |

---

## 📁 Struktur Folder

```
ChEmotion/
├── mobile_app/        # Source code Flutter
├── backend/            # Source code Flask API + Model
│   ├── model_lstm_stress.h5
│   ├── tokenizer_stress.pkl
│   └── ...
└── README.md
```

---

## 🔧 Cara Menjalankan

### Backend (Flask + OCR + Model)

1. Masuk ke folder `backend/`
2. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
3. Pastikan Tesseract OCR sudah terinstal:
   - Linux: `sudo apt install tesseract-ocr`
   - Windows: Download dari [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
4. Jalankan Flask server:
   ```bash
   python app.py
   ```

### Flutter App

1. Masuk ke folder `mobile_app/stress_detection/`
2. Jalankan:
   ```bash
   flutter pub get
   flutter run
   ```

> 📱 Ganti `http://10.0.2.2:5000` dengan IP lokal jika menggunakan perangkat fisik.

---

## 📜 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan eksperimen. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

## 🤝 Kontribusi

Kontribusi terbuka untuk:

- Menambahkan deteksi emosi selain stres
- Meningkatkan hasil OCR atau model NLP
- Integrasi ke platform lainnya (web, desktop)

---

## 🙋 Tentang Pembuat

Dibuat oleh Agni Musadad

---
