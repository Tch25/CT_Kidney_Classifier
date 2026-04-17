# 🩻 Kidney CT Scan Analyzer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ctkidneyclassifier.streamlit.app/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-orange.svg)](https://tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://docker.com/)

> AI-powered detection of kidney cysts, tumors, and stones from CT scans.

## 🎯 Live Demo

**[👉 Click here to try the app!](https://ctkidneyclassifier.streamlit.app/)**

Upload a CT scan and get instant predictions with AI-generated clinical reports.

## 📊 Model Performance (Validation Set)

| Metric | Score |
|--------|-------|
| **Accuracy** | 98.0% |
| **Macro Avg Precision** | 97% |
| **Macro Avg Recall** | 98% |
| **Macro Avg F1-Score** | 98% |

### Per-class Performance

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Cyst | 0.99 | 1.00 | 0.99 | 555 |
| Normal | 0.99 | 0.97 | 0.98 | 759 |
| Stone | 0.98 | 0.96 | 0.97 | 206 |
| Tumor | 0.94 | 0.99 | 0.96 | 342 |

### Stone Class Performance (Most Critical)

| Metric | Score |
|--------|-------|
| **Precision** | 97.5% |
| **Recall** | 95.6% |
| **F1-Score** | 96.6% |

> ✅ The model finds most stones (95.6% recall) with few false alarms (97.5% precision).

## 🏗️ Architecture
```
User Uploads CT Scan
        ↓
Streamlit Frontend (Streamlit Cloud)
        ↓
FastAPI Backend (Google Cloud Run)
        ↓
TensorFlow CNN Model
        ↓
Prediction + AI Report (Groq LLM)
        ↓
Results Displayed to User
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Model** | Custom CNN (TensorFlow/Keras) |
| **Backend** | FastAPI + Docker |
| **Frontend** | Streamlit |
| **Deployment** | Google Cloud Run + Streamlit Cloud |
| **LLM Report** | Groq API (Llama 3.3) |
| **Container** | Docker + docker-compose |

## 📁 Project Structure
```
CT_Kidney_Classifier/
├── backend/
│ ├── main.py # FastAPI endpoints
│ ├── model.py # Model loading & prediction
│ ├── report.py # AI report generation
│ └── requirements.txt
├── frontend/
│ ├── app.py # Streamlit UI
│ ├── Dockerfile
│ └── requirements.txt
├── model/
│ └── custom_cnn_kidney_model.h5
├── tests/
│ ├── test_backend.py # API tests
│ ├── test_model.py
│ └── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt # Root requirements (reference only)
└── README.md
```
## 🚀 Local Development

### Prerequisites
- Python 3.10
- Docker (optional)

### Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
### Docker
```
docker-compose up --build
```
## 🔗 Live URLs

| Service | URL |
|---------|-----|
| **Streamlit App** | [https://ctkidneyclassifier.streamlit.app/](https://ctkidneyclassifier.streamlit.app/) |
| **API Documentation** | [https://ct-kidney-classifier-709689790245.europe-west1.run.app/docs](https://ct-kidney-classifier-709689790245.europe-west1.run.app/docs) |

## 👥 Authors

- [Valeria Montejo](https://github.com/VMontejo)
- [Milka Tch](https://github.com/Tch25)

## 📄 License

MIT
