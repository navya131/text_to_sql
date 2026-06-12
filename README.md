# 🚀 AI Text-to-SQL Query Generator

An AI-powered web application that converts natural language prompts into SQL queries using Python and Flask.

Users can enter simple English commands such as:

> Show all employees

and instantly get the corresponding SQL query.

---

## 📌 Features

✅ Convert English text into SQL queries

✅ User-friendly Flask web interface

✅ Supports common SQL operations

✅ Prompt search history

✅ Clean and responsive UI

✅ Beginner-friendly project structure

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Regular Expressions (Regex)
- Jinja2 Templates

---

## 📂 Project Structure

```text
text_to_sql/
│
├── app.py
├── sql_generator.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/text_to_sql.git
```

### 2. Navigate to Project

```bash
cd text_to_sql
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python app.py
```

### 5. Open Browser

```text
http://127.0.0.1:5000
```

---

## 💡 Supported Prompts

### Show All Employees

Input:

```text
Show all employees
```

Output:

```sql
SELECT * FROM employees;
```

---

### Count Employees

Input:

```text
Count employees
```

Output:

```sql
SELECT COUNT(*) FROM employees;
```

---

### Salary Greater Than

Input:

```text
Show employees with salary greater than 50000
```

Output:

```sql
SELECT * FROM employees WHERE salary > 50000;
```

---

### Salary Less Than

Input:

```text
Show employees with salary less than 30000
```

Output:

```sql
SELECT * FROM employees WHERE salary < 30000;
```

---

### Department Filter

Input:

```text
Show employees in sales
```

Output:

```sql
SELECT * FROM employees WHERE department='sales';
```

---

### Highest Salary

Input:

```text
Employee with highest salary
```

Output:

```sql
SELECT * FROM employees ORDER BY salary DESC LIMIT 1;
```

---

## 📸 Application Screenshots

Add screenshots here after uploading them to your repository.

```markdown
![Home Page](screenshots/home.png)

![Generated Query](screenshots/output.png)
```

---

## 🔮 Future Enhancements

- NLP-based query understanding
- Dynamic table detection
- MySQL Integration
- PostgreSQL Support
- SQLite Database Connectivity
- Voice-to-SQL Conversion
- Query Execution Engine
- Machine Learning-Based Query Prediction
- Export Results to CSV/Excel

---

## 🎯 Learning Outcomes

This project demonstrates:

- Flask Web Development
- Python Backend Programming
- SQL Query Generation
- Form Handling
- Frontend Integration
- Git & GitHub Project Management

---

