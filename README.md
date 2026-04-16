# 📄 PDF to Audio Converter (DevOps Project)

A **cloud-ready PDF to Audio Converter** that transforms PDF documents into speech using Python, Docker, Kubernetes, and CI/CD automation.

---

## 🚀 Features

* 📄 Upload PDF files via web UI
* 🔊 Convert text to speech (MP3)
* 🎧 Play and download audio
* 🌍 Multi-language support
* ⚡ Adjustable speech speed
* 🎨 Modern Streamlit UI
* 🐳 Dockerized application
* ☸️ Kubernetes deployment
* ⚙️ CI/CD with GitHub Actions

---

## 🛠️ Tech Stack

* **Frontend & Backend:** Python + Streamlit
* **Libraries:** PyPDF2, gTTS
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **CI/CD:** GitHub Actions
* **Registry:** Docker Hub

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
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md
```

---

## ⚙️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t pdf2audio .
```

### Run Container

```bash
docker run -p 8501:8501 pdf2audio
```

---

## ☸️ Kubernetes Deployment

### Apply Deployment

```bash
kubectl apply -f deployment.yml
```

### Apply Service

```bash
kubectl apply -f service.yml
```

### Access App

```
http://localhost:30080
```

---

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions to automate:

* 🔄 Build Docker image on every push
* 📦 Push image to Docker Hub

### Workflow File

```
.github/workflows/deploy.yml
```

---

## 🔁 Local Continuous Deployment (CD)

Since Kubernetes is running locally, deployment is handled using a simple script.

### Create `deploy.bat`

```bat
docker pull mohammadkasim/pdf2audio:latest
kubectl rollout restart deployment pdf2audio-deployment
```

### Run Deployment

```bash
deploy.bat
```

---

## 🔄 DevOps Workflow

```
Code → GitHub Push → CI (Build + Push Image) → Local CD → Kubernetes Deployment
```

---

## 🔥 DevOps Highlights

* Docker image optimization
* Kubernetes Deployment & Service
* NodePort exposure
* CI pipeline with GitHub Actions
* Local CD automation
* Real-world debugging & fixes

---

## 📌 Future Enhancements

* ☁️ Deploy on AWS (EKS)
* 🔄 Full CI/CD with cloud Kubernetes
* 📊 Monitoring (Prometheus + Grafana)
* 🔐 Authentication system
* 🎙️ AI-based voice generation

---

## 👨‍💻 Author

**Mohammad Kasim**
GitHub: https://github.com/Kasim2908

---

## ⭐ Contribute

Feel free to fork, improve, and submit pull requests!

---

## 📜 License

This project is open-source and available under the MIT License.
