# 🎭 FriendsSpeak AI – NLP-Based Dialogue Translator

## 📌 Project Overview

FriendsSpeak AI is a Natural Language Processing (NLP) web application that transforms user input into dialogue styled like characters from the popular TV show *Friends*.

The system takes a sentence as input, predicts which character (Ross, Rachel, Monica, Chandler, Joey, or Phoebe) is most likely to say it, and generates a response in that character’s unique tone and personality.

---

## 🚀 Key Features

* 🎭 Character Prediction (6 main Friends characters)
* 💬 Style-based Dialogue Generation
* 🧠 NLP-powered text classification
* ⚡ FastAPI backend for real-time processing
* 🌐 Interactive frontend UI
* 🎨 Character-specific catchphrases and expressions

---

## 🧠 NLP Methodology

This project follows a **hybrid NLP approach**:

### 1. Text Preprocessing

* Lowercasing
* Cleaning input text
* Basic normalization

### 2. Feature Extraction

* TF-IDF Vectorization to convert text into numerical form

### 3. Classification Model

* Machine Learning model predicts the most probable character

### 4. Response Generation

* Rule-based templates generate character-style dialogue
* Special keyword-based handling (e.g., “my eyes” → Phoebe)

---

## 🛠 Tech Stack

| Layer    | Technology               |
| -------- | ------------------------ |
| Frontend | HTML, CSS, JavaScript    |
| Backend  | FastAPI (Python)         |
| ML/NLP   | Scikit-learn             |
| Model    | TF-IDF + Classification  |
| Data     | Friends dialogue dataset |

---

## 📂 Project Structure

```bash
friends-nlp-project/
│
├── backend/
│   └── main.py              # FastAPI backend
│
├── frontend/
│   ├── index.html          # UI
│   └── assets/             # Character images
│
├── src/
│   ├── translator.py       # Response logic
│   ├── catchphrase.py      # Character phrases
│   └── utils.py            # Helpers
│
├── models/
│   ├── model.pkl           # Trained model
│   └── vectorizer.pkl      # TF-IDF vectorizer
│
├── notebooks/
│   └── eda_and_model.ipynb # Training & analysis
│
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/alirida8852/friends-nlp-project.git
cd friends-nlp-project
```

### 2. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Run Backend Server

```bash
cd backend
uvicorn main:app --reload
```

### 4. Run Frontend

Open:

```bash
frontend/index.html
```

in your browser.

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

## 📊 Dataset

The model is trained on dialogue transcripts from the *Friends* TV show.

Projects using similar datasets often focus on dialogue modeling and personality recognition ([Chris Payne Home][1]).

---

## ⚠️ Limitations

* Response generation is rule-based (not fully generative AI)
* Limited dataset size affects accuracy
* Does not understand deep context (sentence-level only)

---

## 🚀 Future Improvements

* Use deep learning (LSTM / Transformers)
* Add conversational memory (context awareness)
* Deploy as a live web app
* Improve dataset size and diversity

---

## 👩‍💻 Author

Rida
Tejeswini
Inchara
NLP Mini Project


