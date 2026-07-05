# 🩺 HealthAI – Intelligent Web-Based Personalized Healthcare Recommendation and Analytics Platform

HealthAI is a dynamic web-based healthcare platform that combines **Internet Programming technologies** with **Machine Learning** to deliver personalized healthcare services. The application enables patients to predict diseases based on symptoms, receive customized treatment recommendations, book specialist appointments, generate downloadable healthcare reports, and interact with an AI-powered healthcare assistant. Doctors can efficiently monitor patients, analyze healthcare data, and support informed clinical decision-making through an interactive analytics dashboard.

---

# 📖 Project Overview

Traditional healthcare systems often rely on manual record management and generalized treatment approaches, leading to delayed diagnoses and fragmented healthcare services. HealthAI addresses these challenges by providing a centralized healthcare platform that integrates patient management, disease prediction, appointment scheduling, and healthcare analytics into a single intelligent web application.

The system is developed using **HTML, CSS, JavaScript, Bootstrap, Flask, SQLite, and Machine Learning**, following a **three-tier architecture** to ensure scalability, maintainability, and efficient healthcare data management.

---

# ✨ Features

## 👤 User Management
- Secure Patient & Doctor Registration
- Login Authentication
- Role-Based Access Control
- Session Management

## 🏥 Patient Services
- Symptom-Based Disease Prediction
- Personalized Treatment Recommendations
- Diet & Lifestyle Suggestions
- Severity & Risk Analysis
- AI Healthcare Chatbot
- Specialist Appointment Booking
- Downloadable Healthcare Reports (PDF)

## 👨‍⚕️ Doctor Dashboard
- Patient Record Management
- Healthcare Analytics Dashboard
- Disease Distribution Insights
- Patient Monitoring
- Report Management

## 📊 Healthcare Analytics
- Disease Prediction
- Risk Assessment
- Healthcare Statistics
- Personalized Recommendations

---

# 💻 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome

### Backend
- Python
- Flask
- Jinja2 Template Engine

### Database
- SQLite

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Report Generation
- ReportLab

---

# 📂 Project Structure

```
HealthAI
│
├── static
│   ├── css
│   ├── js
│   └── images
│
├── templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── patient_dashboard.html
│   ├── doctor_dashboard.html
│   ├── appointments.html
│   ├── reports.html
│   └── chatbot.html
│
├── datasets
│   ├── Training.csv
│   ├── Testing.csv
│   ├── Symptom-severity.csv
│   ├── Symptom-description.csv
│   └── Symptom-precaution.csv
│
├── models
│   └── disease_prediction_model.pkl
│
├── app.py
├── healthcare.db
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/HealthAI.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd HealthAI
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

> Screenshots of the following pages are uploaded for reference.

- 🏠 Landing Page
  <img width="937" height="436" alt="Screenshot 2026-06-24 230305" src="https://github.com/user-attachments/assets/de08c9d2-1317-4283-8faf-e0931dc332b9" />

- 🔐 Login Page
  <img width="955" height="428" alt="Screenshot 2026-06-24 230325" src="https://github.com/user-attachments/assets/594094e5-55c5-4240-8d07-051f15e856b5" />

- 📝 Registration Page
  <img width="935" height="425" alt="Screenshot 2026-07-05 201447" src="https://github.com/user-attachments/assets/3e10992f-f293-4c73-b3dd-eef7ebca2820" />

- 👤 Patient Dashboard
  <img width="946" height="434" alt="Screenshot 2026-06-24 230437" src="https://github.com/user-attachments/assets/f8993e10-1dde-4019-85ba-264037f05da8" />

- 👨‍⚕️ Doctor Dashboard
  <img width="932" height="436" alt="Screenshot 2026-06-24 230346" src="https://github.com/user-attachments/assets/fe6f589b-4c6a-4693-a72b-483e13fb6726" />
  <img width="929" height="419" alt="Screenshot 2026-06-24 230410" src="https://github.com/user-attachments/assets/53129e34-c692-4329-8433-29cdfb5beca1" />

- 🤖 Disease Prediction Interface
  <img width="933" height="418" alt="Screenshot 2026-06-24 230535" src="https://github.com/user-attachments/assets/478c5b0d-acb2-48ff-acfb-ed088c733f55" />
  <img width="761" height="422" alt="Screenshot 2026-06-24 230657" src="https://github.com/user-attachments/assets/0d646cb1-1187-412d-a07c-64000ee0a7ab" />
- 📅 Appointment Booking
  <img width="876" height="442" alt="Screenshot 2026-06-24 230756" src="https://github.com/user-attachments/assets/e21c99f8-9f2b-48c4-abf3-4dd0a9d0ae9f" />
  <img width="933" height="401" alt="Screenshot 2026-06-24 230811" src="https://github.com/user-attachments/assets/8966865d-12cf-41d8-93ef-ea043ad54639" />
- 💬 AI Chatbot
  <img width="305" height="353" alt="Screenshot 2026-06-24 230731" src="https://github.com/user-attachments/assets/3b2dcbb2-4471-43ca-b0db-1bdb39d4e374" />
- 📄 Healthcare Report
  <img width="916" height="423" alt="Screenshot 2026-06-24 230458" src="https://github.com/user-attachments/assets/5fe67769-b576-42fd-b90c-84d43310893f" />
<img width="232" height="278" alt="Screenshot 2026-07-05 202621" src="https://github.com/user-attachments/assets/5f7094e0-35e4-46f5-b6d9-bea06eb1a162" />
- 📊 Analytics Dashboard
  <img width="932" height="436" alt="Screenshot 2026-06-24 230346" src="https://github.com/user-attachments/assets/661b1c36-e4eb-4b2c-a0ad-695b81e437b9" />
  <img width="946" height="434" alt="Screenshot 2026-06-24 230437" src="https://github.com/user-attachments/assets/26ea7fc1-a7e2-43e0-8f1a-1d59d7d9cc02" />



---

# 🚀 Future Enhancements

- Integration with Electronic Health Records (EHR)
- Deep Learning Models for Improved Disease Prediction
- Voice-Based Virtual Healthcare Assistant
- Mobile Application Development
- Multi-Language Support
- Real-Time Notification & Alert System
- Integration with Hospital Information Systems (HIS)

---

# 👩‍💻 Author

**Adhiti Sivakumar**

Bachelor of Engineering (Computer Science and Engineering)

HealthAI was developed as an academic capstone project to demonstrate the integration of **Internet Programming**, **Machine Learning**, and **Healthcare Analytics** in building an intelligent, scalable, and user-centric healthcare management platform.

---

## ⭐ If you found this project useful, consider giving it a Star!

```
⭐ Star this repository if you like the project!
```
