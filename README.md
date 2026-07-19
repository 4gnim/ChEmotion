<div align="center">
  <h1>🧠 ChEmotion - MLOps & Containerization Showcase</h1>
</div>

**ChEmotion** is an AI-powered stress emotion detector utilizing OCR and Machine Learning.
While this repository contains both the Flutter frontend and the Flask backend, **this project serves primarily as a showcase for MLOps (Machine Learning Operations) and advanced DevOps containerization techniques.**

## DevOps Architecture & Containerization Strategy

Deploying AI applications involves more than just running a Python script. It requires managing OS-level dependencies alongside heavy mathematical libraries. To ensure seamless scalability and deployment, the backend is fully containerized.

1. **Infrastructure as Code (Docker):** The custom `Dockerfile` handles the installation of Debian-based OS packages (specifically `tesseract-ocr` and language packs), sets up the Python environment, resolves TensorFlow/Keras dependencies, and exposes the REST API.
2. **Continuous Deployment (CI/CD):** Utilizing GitHub Actions, any changes pushed to the `backend/` directory automatically trigger a build pipeline that compiles the Docker image and pushes it to Docker Hub.
3. **Decoupled Architecture:** The Flutter mobile application acts strictly as a presentation layer, while the containerized ML API securely handles the heavy computational logic (OCR extraction & LSTM prediction).

## Tech Stack

- **MLOps & DevOps:** Docker, GitHub Actions
- **Backend API:** Flask (Python)
- **Machine Learning:** TensorFlow/Keras (LSTM Model)
- **OCR Engine:** Tesseract OCR (Linux OS-level integration)
- **Frontend:** Flutter, Dart

## How to Run the AI Backend (Docker)

You do not need to manually install Python, TensorFlow, or Tesseract OCR on your local machine. Simply pull the containerized environment:

```bash
# Pull the latest image from Docker Hub
docker pull dad4d/chemotion-backend:latest

# Run the container on port 5000
docker run -d -p 5000:5000 dad4d/chemotion-backend:latest
```
