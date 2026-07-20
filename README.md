# 💰 FinSight

FinSight is a personal finance management web application built using **Flask** and **MySQL**. It helps users organize their finances by tracking income, expenses, budgets, investments, and financial goals from a single dashboard.

Along with basic financial management, FinSight provides visual analytics, spending insights, budget recommendations, trend analysis, and a financial health score to help users understand their financial habits and make better decisions.

---

## Features

### 🔐 Authentication
- User Registration
- Secure Login & Logout
- Session Management

### 💵 Income Management
- Add income records
- Update and delete income
- View complete income history

### 💸 Expense Management
- Add daily expenses
- Categorize expenses
- Edit and delete expense records
- View expense history

### 📊 Budget Management
- Create budgets
- Track budget utilization
- Monitor overspending

### 📈 Investment Management
- Add investments
- Track investment portfolio
- Monitor investment performance

### 🎯 Financial Goals
- Create financial goals
- Track goal progress
- View completed goals

### 📉 Analytics
- Financial Overview
- Spending Analysis
- Budget Recommendations
- Trends & Predictions
- Financial Health Score

---

# Tech Stack

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

---

# Project Structure

```
FinSight/
│
├── database/
│
├── models/
│
├── routes/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── uploads/
│
├── utils/
│
├── app.py
├── config.py
├── extensions.py
├── market_service.py
├── requirements.txt
└── README.md
```

---

# Installation

### Clone the repository

```bash
git clone https://github.com/vennelamake/FinSight.git
```

```bash
cd FinSight
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows

```bash
.venv\Scripts\activate
```

### Configure the database

Update your MySQL configuration in `config.py`.

Create the database.

Run the project.

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# Project Modules

- Dashboard
- Income Management
- Expense Management
- Budget Management
- Investment Management
- Financial Goals
- Analytics Dashboard
- Spending Analysis
- Budget Recommendations
- Trends & Predictions
- Financial Health Score


# Author

**MAKE SRI VIJAYA VENNELA RAJESWARI**

B.Tech – Computer Science Engineering

---

## License

This project was developed for learning and educational purposes.