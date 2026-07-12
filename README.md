**Care AI** is a next-generation medical assistant that bridges the gap between **Modern Medicine** and **Ayurvedic Wisdom**. It utilizes Generative AI, Computer Vision, and classical Machine Learning to provide holistic health assessments, diet planning, and drug safety analysis.



## 🚀 Key Features

### 🧠 Dual-Engine Intelligence
* **Hybrid Diagnosis:** Combines a custom-trained ML model (`model.pkl`) with Google's Gemini LLM for high-accuracy symptom analysis.
* **Holistic Advice:** Every diagnosis includes both **Allopathic (Medical)** treatment and **Ayurvedic (Herbal)** remedies.

### 👁️ Medical Vision (AI Scan)
* Upload images of **Skin Rashes**, **X-Rays**, **Lab Reports**, or **Medicine Labels**.
* The AI analyzes visual data to identify conditions or explain report metrics in simple language.

### 🩺 Comprehensive Tools
* **🥗 Smart Diet Planner:** Generates personalized 7-day meal plans based on cuisine (South/North Indian), condition (Diabetes/BP), and age.
* **🛡️ Drug Interaction Checker:** Analyzes chemical compatibility between two medicines to prevent harmful side effects.
* **📍 Nearby Care:** GPS-enabled locator for Doctors, Clinics, and Pharmacies using OpenStreetMap.
* **📊 Smart Vitals:** Simulates and analyzes vital signs (SpO2, Heart Rate, BP) to detect emergencies.

### 🌐 Platform Capabilities
* **Multilingual:** Full UI and Chat translation for **10+ Indian Languages** (Hindi, Kannada, Tamil, etc.).
* **Voice-Enabled:** Speech-to-Text input and Text-to-Speech response for accessibility.
* **PDF Reports:** Generates professional, downloadable medical reports.

---

## 📂 Project Architecture

```text
📦 AI_Medicine
│
├── 📂 data                  # Dataset storage for training local models
│   └── training_data.csv    # CSV containing symptom-disease mapping
│
├── 📂 model                 # Machine Learning artifacts
│   └── model.pkl            # Serialized Random Forest/Naive Bayes model
│
├── 📂 static                # Frontend assets (CSS, JS, Images)
│   ├── 📂 images
│   │   └── download.jpeg    # Default assets/placeholders
│   ├── script.js            # Core frontend logic (Fetch API, UI DOM manipulation)
│   └── style.css            # Custom styling + Tailwind utilities
│
├── 📂 templates             # Jinja2 HTML Templates
│   ├── base.html            # Master layout (Navbar, Footer, Translation Logic)
│   ├── landing.html         # Login / Registration Page
│   ├── home.html            # Main Dashboard & Symptom Checker
│   ├── chat.html            # Dual-Pane AI Chatbot Interface
│   ├── vision.html          # Image Upload & Analysis Interface
│   ├── diet.html            # 7-Day Diet Planner Interface
│   ├── safety.html          # Drug Interaction Checker Interface
│   ├── maps.html            # GPS Doctor Locator
│   └── history.html         # User Medical Records & Database View
│
├── .env                     # Environment Variables (API Keys - Hidden)
├── app.py                   # Main Flask Server Entry Point
├── medical_engine.py        # Core Logic: Emergency detection, Vitals analysis, Herbal DB
├── train_model.py           # Script to retrain the local ML model using training_data.csv
├── create_db.py             # Database initialization script (SQLite/MySQL tables)
├── check_models.py          # Utility to verify model integrity
├── check_tables.py          # Utility to verify database schema
├── test_db.py               # Unit tests for database connectivity
├── test_key.py              # Unit test for Google Gemini API connectivity
└── users.db                 # Local SQLite Database (Users, History, Appointments)



Sure! Here is your **polished, professional, GitHub-ready README** — perfectly formatted, clean typography, consistent emojis, color-balanced badges, improved spacing, and better hierarchy.

---

# 🏥 **Care AI – Intelligent Health & Wellness Suite**

![Version](https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge\&logo=flask)
![AI](https://img.shields.io/badge/AI-Gemini%202.0-orange?style=for-the-badge\&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Care AI** is a next-generation digital medical assistant that blends
> **Modern Healthcare**, **Ayurvedic Wisdom**, and **AI-powered Diagnostics**
> into a single intelligent wellness ecosystem.

---

## 🚀 **Key Features**

### 🧠 **Dual-Engine Health Intelligence**

* Hybrid symptom diagnosis using:

  * ✔️ **Custom Local ML Model (`model.pkl`)**
  * ✔️ **Google Gemini 2.0 LLM**
* Provides both **Allopathic** & **Ayurvedic** treatment recommendations.

---

### 👁️ **AI Medical Vision**

Upload images of:

* Skin diseases
* X-rays
* Lab reports
* Medicine labels

➡️ Care AI explains, detects, summarizes, and interprets visual medical data.

---

### 🩺 **Complete Medical Toolkit**

#### 🥗 Smart Diet Planner

Creates tailored **7-day meal plans** based on:

* Age
* Symptoms
* Cuisine (North/South)
* Medical conditions (Diabetes, BP)

#### 🛡️ Drug Interaction Checker

Detects **harmful chemical conflicts** between two medicines.

#### 📍 Nearby Health Locator

GPS + OpenStreetMap to find:

* Hospitals
* Doctors
* Clinics
* Pharmacies

#### 📊 Smart Vitals

Simulates & analyzes:

* SpO₂
* BP
* Heart Rate
* Temperature

Automatically detects emergencies.

---

### 🌐 **Platform Features**

* 🌏 **Multilingual** (10+ Indian languages)
* 🎤 **Voice Input + Voice Output**
* 📄 **Downloadable AI-generated PDF reports**
* 🧭 **Fully Responsive UI (TailwindCSS)**

---

## 📂 **Project Architecture**

```
📦 backend
│
├── 📂 data                  # Training datasets
│   └── training_data.csv
│
├── 📂 model                 # ML artifacts
│   └── model.pkl
│
├── 📂 static                # Frontend assets
│   ├── 📂 images
│   │   └── download.jpeg
│   ├── script.js
│   └── style.css
│
├── 📂 templates             # HTML UI (Jinja2)
│   ├── base.html
│   ├── landing.html
│   ├── home.html
│   ├── chat.html
│   ├── vision.html
│   ├── diet.html
│   ├── safety.html
│   ├── maps.html
│   └── history.html
│
├── .env                     # API keys + DB config
├── app.py                   # Main Flask backend
├── medical_engine.py        # Vitals, emergency detection, herbal DB
├── train_model.py           # Retrain ML model
├── create_db.py             # Database initializer
├── check_models.py          # Model verification
├── check_tables.py          # DB schema verification
├── test_db.py               # DB connectivity test
├── test_key.py              # Gemini API test
└── users.db                 # SQLite database
```

---

# ⚡ **Installation & Setup**

### **1️⃣ Get Repository**


### **2️⃣ Create Virtual Environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```bash
pip install flask flask-cors google-generativeai scikit-learn pandas python-dotenv fpdf pillow mysql-connector-python
```

### **4️⃣ Configure Environment**

Create `.env`:

```
GEMINI_API_KEY=your_google_api_key_here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=careai_db
USE_LOCAL_MODEL=true
```

### **5️⃣ Initialize Model & Database**

```bash
python train_model.py
python create_db.py
```

### **6️⃣ Run the Server**

```bash
python app.py
```

Open:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

# 📖 **Module Documentation**

## 🧠 `medical_engine.py`

Contains all internal health logic:

### **✔ detect_emergency(text)**

Finds risky patterns such as *chest pain, suicide, heart attack*.

### **✔ analyze_vitals(vitals_dict)**

Detects abnormal BP, HR, SpO₂ & flags emergencies.

### **✔ get_herbal_remedy(symptom)**

Fast remedy lookup using Ayurvedic dataset.

---

## ⚙️ `app.py` — Core API Routes

| Route            | Purpose                                 |
| ---------------- | --------------------------------------- |
| `/recommend`     | Symptom → Local ML → Gemini → Treatment |
| `/chat`          | Text + Image chatbot                    |
| `/generate_diet` | Produces structured 7-day diet plan     |
| `/analyze_image` | Vision AI endpoint                      |
| `/history`       | Pull user medical history               |

---

# 🛡️ **Safety & Disclaimer**

* Care AI is **not** a replacement for a doctor.
* Emergency terms instantly trigger a **hard-coded alert response**.
* Always consult a certified healthcare professional before acting on AI advice.
"# Care-AI" 
