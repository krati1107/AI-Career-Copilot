# 🚀 AI Career Copilot

### 🔥 Full Stack Project (Python + Flask + SQL)

---

## 📌 Overview

AI Career Copilot is a web application that recommends career paths based on user skills using Python and Flask.

---

## 🧠 Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS

---

## ✨ Features

* Skill-based career recommendation
* Simple and interactive UI
* Stores prediction history in database
* Fast backend using Flask

---

## ⚙️ How It Works

1. User enters skills
2. Flask processes input
3. Python model analyzes skills
4. Career is predicted
5. Data stored in SQLite

---

## 🧠 Core Logic

```python
def recommend_career(skills):
    skills = [s.strip().lower() for s in skills]

    data_skills = {"python", "sql", "excel"}
    web_skills = {"html", "css", "javascript"}

    if len(set(skills) & data_skills) > len(set(skills) & web_skills):
        return "Data Analyst"
    else:
        return "Web Developer"
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/AI-Career-Copilot.git
cd AI-Career-Copilot
pip install flask
python app.py
```

Open in browser:
http://127.0.0.1:5000/

---


## 🌟 Future Improvements

* Add Machine Learning model
* Add dashboard
* Deploy online

---
