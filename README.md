# 📚 Student Score Predictor

An AI-powered web app that predicts a student's expected exam score based on various academic, behavioral, and environmental factors. Built with **Streamlit**, **scikit-learn**, and **Regression Models**.

---

## 🚀 Demo
🎯 [Student Score Predictor](https://pathwaypredict.streamlit.app/)

---

## 🧠 Features
- Predicts student exam scores using multiple inputs:
  - Hours Studied
  - Attendance
  - Sleep Hours
  - Previous Scores
  - Tutoring Sessions
  - Motivation Level
  - Parental Involvement
  - Peer Influence
- Uses polynomial feature transformation for improved accuracy
- Simple, interactive Streamlit interface

---

## 🛠 Tech Stack

| Tool | Description |
|------|-------------|
| Python | Core programming language |
| Streamlit | For building the web interface |
| scikit-learn | Machine learning library |
| pandas, numpy | Data manipulation and preprocessing |
| pickle | For saving and loading ML models |

---

## 📈 How it Works

1. User enters values through the web interface.
2. Input is transformed using a polynomial feature transformer.
3. Trained model predicts the exam score.
4. Predicted score is displayed interactively.

---

## 🧪 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/Kaifi1199/Student-Score-Predictor.git
```

```bash
cd Student-Score-Prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 📄 License

This project is for educational purposes.

---
