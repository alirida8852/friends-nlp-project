# 🎬 FriendsSpeak AI – NLP Mini Project

## 📌 Overview

FriendsSpeak AI is a Natural Language Processing (NLP) based web application that transforms user input into dialogue styled like characters from the TV show *Friends*.

The system analyzes input text and generates character-specific responses using rule-based NLP techniques and pattern matching.

---

## 🚀 Features

* 🎭 Character-based dialogue generation (Ross, Rachel, Monica, Chandler, Joey, Phoebe)
* 💬 Iconic phrase detection (e.g., "My eyes! My eyes!")
* 🧠 Rule-based NLP transformation
* 🌐 Interactive web interface
* 🖼️ Character image popup on response
* ⚡ Fast API backend

---

## 🧠 NLP Concepts Used

* Text preprocessing (lowercasing, trimming)
* Pattern matching
* Rule-based response generation
* Keyword detection
* Template-based text transformation

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** FastAPI (Python)
* **NLP Approach:** Rule-based system

---

## 📂 Project Structure

```
project/
│
├── backend/
│   ├── main.py
│   ├── translator.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── assets/
│
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 2. Run backend

```bash
uvicorn main:app --reload
```

### 3. Open frontend

Open `index.html` in browser

---

## 🎯 Example

**Input:**

```
my eyes my eyes
```

**Output:**

```
MY EYES! MY EYES!
(Character: Phoebe)
```

---

## 📌 Future Improvements

* Use ML model instead of rule-based system
* Add voice output
* Add more datasets for better accuracy
* Deploy as a web app

---

## 👩‍💻 Author

Rida – NLP Mini Project
Inchara
Tejesiswini
