# 📦 Training Recommender System

A lightweight recommendation system that matches users with suitable training courses based on their profile (language level, education, experience, preferences, etc).

---

## 🔧 Project Structure

```
training-recommender/
├── db
  ├── insert_courses.sql         # SQL file with 100 training course entries
  ├── db_reader.py           # Script to connect and fetch courses from PostgreSQL
├── scoring
  ├── rule_score_function.py          # Main scoring logic to compute recommendation scores
├── course_ranker.py         # Example script to run recommendation based on user input
├── requirements.txt           # Python dependencies
└── README.md                  # Project description and usage
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Gold-pig/training-recommender.git
cd training-recommender
```

### 2. Set Up PostgreSQL
```bash
# Create the database (in psql shell):
CREATE DATABASE courses_db3;

# Import sample data:
psql -d courses_db3 -f insert_courses.sql
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Recommender Example
```bash
python run_recommender.py
```

This script will load user profile, fetch courses from the DB, score each course, and output the top recommendations.

---

## 📊 Features
- ✅ Rule-based weighted scoring system
- ✅ Multi-field user input support (language, experience, mobility...)
- ✅ PostgreSQL data backend
- ✅ Modular design for reuse in web apps / APIs

---

## 🔐 Authentication for Git Push (optional)
If you encountered GitHub push errors, consider using [SSH authentication](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) or generate a [Personal Access Token (PAT)](https://github.com/settings/tokens) to use in place of your GitHub password.

---

## 🧠 Future Work
- Add embedding-based or ML-based ranking (BERT, LightGBM)
- Web UI for real-time matching
- Dockerization & deployment templates

---

Maintained by **guofy15775100131@gmail.com** — Feel free to fork & contribute!
