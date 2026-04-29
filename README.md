# Friends Catchphrase Detection (NLP Project)

## Overview
This project is a Natural Language Processing (NLP) system that predicts which character from the TV show *Friends* is speaking based on a given dialogue input.

It uses machine learning techniques to classify text into multiple character classes such as Joey, Ross, Rachel, Chandler, Monica, and Phoebe.

---

## Problem Statement
Given a line of dialogue, the goal is to identify the most likely character who said it.

This is a **multi-class text classification problem**, where each class represents a character.

---

## Tech Stack
- Python
- scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer

---

## Approach

### 1. Data Preprocessing
- Removed punctuation and special characters  
- Converted text to lowercase  
- Tokenized dialogue lines  

### 2. Feature Engineering
- Used **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text into numerical features  

### 3. Model Training
- Applied machine learning algorithms such as:
  - Multinomial Naive Bayes *(recommended for text classification)*  
  - Logistic Regression *(optional improvement)*  

### 4. Prediction Pipeline
Input text → Preprocessing → TF-IDF → Model → Predicted Character  

---

## Results
- Accuracy: ~30%  

### Why accuracy is moderate:
- Characters use similar conversational language  
- Dataset may be limited or imbalanced  
- Catchphrases are not always unique  

---

## Example Predictions

| Input Dialogue        | Predicted Character |
|----------------------|--------------------|
| "How you doin?"      | Joey               |
| "We were on a break!"| Ross               |
| "Oh. My. God!"       | Janice             |

---

## Project Structure
│
├── data/
│ └── dialogues.csv
│
├── model/
│ └── trained_model.pkl
│
├── src/
│ ├── preprocessing.py
│ ├── train.py
│ └── predict.py
│
├── requirements.txt
└── README.md


---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/alirida8852/friends-nlp-project
cd friends-nlp-project

python src/predict.py

Future Improvements
Improve accuracy using deep learning (LSTM / BERT)
Increase dataset size
Build a web interface using FastAPI
Deploy as an API

Key Learnings
Practical implementation of NLP pipelines
Feature extraction using TF-IDF
Challenges in multi-class classification
Model evaluation and limitations