# 🎓 Placement Management System

A Flask-based web application that helps students prepare for campus placements by providing resume ATS analysis, placement prediction using Machine Learning, company recommendations, and interview preparation.

---

## 🚀 Features

- 🔐 User Authentication (Register & Login)
- 📄 Resume Upload (PDF)
- 📊 ATS Resume Analysis
- 🤖 Placement Prediction using Machine Learning
- 🏢 Company Recommendation based on profile
- 💼 Interview Preparation Module
- 🗄 SQL Server Database Integration
- 📈 Dashboard with placement statistics

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- Scikit-learn
- NumPy
- Joblib

### Database
- Microsoft SQL Server
- PyODBC

---

## 📂 Project Structure

```
Placement-Management-System/
│
├── app.py
├── requirements.txt
├── models/
├── templates/
├── static/
├── utils/
├── database/
├── data/
└── uploads/
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/7123-chirag/Placement-Management-System.git
cd Placement-Management-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a file:

```
database/db_connection.py
```

Configure your SQL Server connection.

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🗃 Database

The SQL schema is included in:

```
placementss databases.sql
```

Import it into Microsoft SQL Server before running the project.

---



## 📌 Future Improvements

- Email verification
- Password reset
- Resume history
- Admin dashboard
- Cloud deployment
- AI-based resume suggestions

---

## 👨‍💻 Author

**Chirag Khanna**

GitHub:
https://github.com/7123-chirag
