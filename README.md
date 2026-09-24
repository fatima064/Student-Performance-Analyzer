# 🎓 Student Performance Analyzer
# LIVE SITE :- http://127.0.0.1:5000


A beginner-friendly web-based application built using Python, Flask, Pandas, SQL, and SQLite to analyze and visualize student academic performance.

The application reads student data, stores it in a SQLite database, performs SQL-based queries and analysis, calculates student averages, categorizes performance, and presents the results through an interactive web dashboard.

---

## 📌 Project Overview

The Student Performance Analyzer was developed to demonstrate how Python, SQL, database management, and web technologies can work together in a simple real-world application.

The application allows users to:

- View student academic records
- Search for individual students
- Calculate average marks
- Categorize student performance
- Identify the top-performing student
- Filter students based on passing criteria
- View class-level statistics
- Visualize student averages using a bar chart

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Flask | Web application backend |
| Pandas | Data manipulation and analysis |
| SQLite | Database storage |
| SQL | Data retrieval and filtering |
| HTML | Web page structure |
| CSS | Dashboard styling |
| Chart.js | Performance visualization |

---

## ✨ Features

### 📊 Dashboard

The dashboard displays:

- Total number of students
- Class average
- Top-performing student
- Complete student performance table

### 🔎 Student Search

Users can search for a student by name.

The application uses a parameterized SQL query to retrieve the student's record from the SQLite database.

### 🧮 Performance Calculation

The application calculates the average of:

- Python
- SQL
- DBMS

Based on the average, students are categorized as:

- Excellent
- Good
- Average
- Needs Improvement

### 🏆 Top Student

The application uses SQL sorting to identify the student with the highest average marks.

### ✅ Passed Students

Students with an average score of 40 or above can be identified using a SQL filtering condition.

### 📈 Performance Visualization

A bar chart displays the average marks of each student using Chart.js.
[Screenshot 2026-09-24 131737.png]

---

## 🗂️ Project Structure

```text
Student-Performance-Analyzer/
│
├── app.py
├── main.py
├── students.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
