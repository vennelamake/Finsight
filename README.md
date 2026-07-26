# 💰 FinSight – Smart Personal Finance Management System

FinSight is a comprehensive personal finance management web application developed using **Flask**, **Python**, and **MySQL**. It helps users efficiently manage their finances by tracking income, expenses, budgets, investments, financial goals, and savings from a single dashboard.

The application also provides intelligent financial insights through spending analysis, budget recommendations, financial health evaluation, trend analysis, OCR-based bank statement import, CSV transaction import, and investment portfolio monitoring, enabling users to make informed financial decisions.

---

# ✨ Features

## 🔐 User Authentication
- Secure user registration and login
- Session management using Flask-Login
- Password hashing for enhanced security

## 💰 Income Management
- Add, edit, and delete income records
- View complete income history
- Categorize different income sources

## 💸 Expense Management
- Record daily expenses
- Categorize expenses
- Edit and delete expense records
- View complete expense history

## 📊 Budget Management
- Create monthly budgets
- Track budget utilization
- Monitor overspending
- Budget recommendations

## 🎯 Financial Goals
- Create financial goals
- Track savings progress
- Monitor completed goals

## 📈 Investment Portfolio
- Add investment details
- Record investment transactions
- Track portfolio performance

## 📉 Analytics Dashboard
- Financial Overview
- Income vs Expense Analysis
- Category-wise Spending Analysis
- Monthly Expense Trends
- Budget Utilization
- Financial Health Score

## 🧠 Smart Financial Insights
- Spending pattern analysis
- Savings suggestions
- Budget recommendations
- Financial health evaluation
- Personalized insights

## 📂 Transaction Import
- Import transactions using CSV files
- OCR-based bank statement image import
- Preview transactions before saving

## 🔔 Notifications
- Budget alerts
- Savings reminders
- Goal notifications
- Financial health alerts

---

# 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2
- Font Awesome

### Backend
- Python
- Flask

### Database
- MySQL
- SQLAlchemy ORM

### Authentication
- Flask-Login

### Additional Libraries
- EasyOCR
- OpenCV
- Pandas
- Matplotlib

---

# 📁 Project Structure

```text
FinSight/
│
├── database/
├── models/
├── routes/
├── services/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── uploads/
├── utils/
├── app.py
├── config.py
├── extensions.py
├── market_service.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/vennelamake/FinSight.git
```

Move into the project folder

```bash
cd FinSight
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Configure your MySQL database in **config.py**.

Run the application

```bash
python app.py
```

Open your browser and visit

```text
http://127.0.0.1:5000
```

---

# 📊 Project Modules

- Dashboard
- User Authentication
- Income Management
- Expense Management
- Budget Management
- Financial Goals
- Investment Portfolio
- Financial Analytics
- Spending Analysis
- Budget Recommendations
- Financial Health Score
- Notifications
- CSV Transaction Import
- OCR Bank Statement Import

---

# 🔮 Future Enhancements

- Mobile Application
- Cloud Deployment
- AI-powered Financial Assistant
- Bill Payment Reminders
- Multi-bank Integration
- Expense Prediction using Machine Learning
- Family Finance Management

---

# 👩‍💻 Author

**MAKE SRI VIJAYA RAJESWARI**

B.Tech – Computer Science Engineering

---

# 📄 License

This project is developed for educational and learning purposes.