# 🏠 AI Property Price Predictor

A simple Machine Learning web application that predicts property prices based on input features like property size.

---

## 🚀 Project Overview

This project is a beginner-friendly AI/ML application that demonstrates how to integrate a Machine Learning model with a web interface.

Users can input the size of a property, and the system predicts the estimated price using a trained Linear Regression model.

---

## 🧠 How It Works

1. A dataset containing property sizes and prices is used to train a model
2. A Linear Regression algorithm learns the relationship between size and price
3. The trained model is saved using `pickle`
4. A web interface allows users to input property size
5. The backend processes the input and returns the predicted price

---

## 🛠️ Tech Stack

* Python
* Flask (Backend)
* HTML & CSS (Frontend)
* Scikit-learn (Machine Learning)
* Pandas (Data Handling)

---

## 📂 Project Structure

```
AI-Property-Price-Predictor/
│
├── app.py
├── model.pkl
├── model.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Property-Price-Predictor.git
cd AI-Property-Price-Predictor
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Run the application

```bash
python3 app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 Features

* User-friendly input form
* Real-time price prediction
* Simple and clean UI
* Machine Learning integration with Flask

---

## 🔮 Future Improvements

* Add more features (location, BHK, amenities)
* Improve model accuracy with larger dataset
* Better UI/UX design
* Deploy the app online
* Add database support

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📌 Author

**Prayash Das**

---

## ⭐ Acknowledgements

* Built as a beginner AI/ML project
* Inspired by real-world property prediction systems

---
