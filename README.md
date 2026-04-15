# 📄 PDF to Audio Converter (DevOps Project)

A cloud-ready **PDF to Audio Converter** that transforms PDF documents into speech using Python, containerization, and Kubernetes.

---

## 🚀 Features

* 📄 Upload PDF files
* 🔊 Convert text to speech (MP3)
* 🌐 Web interface using Streamlit
* 🐳 Dockerized application
* ☸️ Kubernetes deployment ready
* ⚙️ DevOps pipeline compatible

---

## 🛠️ Tech Stack

* **Backend:** Python
* **Framework:** Streamlit
* **Libraries:** PyPDF2, gTTS
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **CI/CD:** GitHub Actions (planned)

---

## 📁 Project Structure

```
pdf2audio/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yml
├── service.yml
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/Kasim2908/pdf2audio.git
cd pdf2audio
```

---

### 2️⃣ Run Locally

```
pip install -r requirements.txt
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🐳 Docker Setup

### Build Image

```
docker build -t pdf2audio .
```

### Run Container

```
docker run -p 8501:8501 pdf2audio
```

---

## ☸️ Kubernetes Deployment

### Apply Deployment

```
kubectl apply -f deployment.yml
```

### Apply Service

```
kubectl apply -f service.yml
```

---

## 🌐 Access Application

```
http://<NodeIP>:30007
```

---

## 🔥 DevOps Highlights

* Containerized using Docker
* Lightweight image optimization
* Kubernetes deployment with scaling
* Service exposure using NodePort
* Ready for CI/CD automation

---

## 📌 Future Enhancements

* 🔁 CI/CD pipeline using GitHub Actions
* ☁️ Cloud deployment (AWS/GCP)
* 🎙️ Advanced AI voices
* 🌍 Multi-language support
* 📊 Monitoring with Prometheus & Grafana

---

## 👨‍💻 Author

**Mohammad Kasim**

GitHub: https://github.com/Kasim2908

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.
