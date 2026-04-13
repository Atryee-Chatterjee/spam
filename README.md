# SpamNix - AI-Powered Spam Detection System

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Now-blue)](https://spam-ubh0.onrender.com/)

🎓 **Project Highlight**: SpamNix is a web-based spam detection platform developed during my internship at Travarsa Private Limited. This intelligent system combines machine learning and web technologies to detect and filter spam messages effectively, ensuring safer platforms for users.

**Project Objective**: To build a responsive and intelligent spam detection system that accurately identifies spam messages using multiple ML models, while offering a smooth, user-friendly interface.

## 🚀 Features

- 📊 **Spam Probability Visualization** with interactive Chart.js
- 🤖 **Multiple ML Models** for robust predictions:
  - Naive Bayes – for quick and lightweight classification
  - Logistic Regression – for higher accuracy
  - Random Forest – for reliable predictions
- 🌐 **Responsive, modern UI** for seamless interaction
- 🔌 **API integration** to make predictions in real-time
- ☁ **Cloud deployment** ready for production

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, Chart.js
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn, NLTK
- **Deployment**: Render

## 🔍 How the Message Detection Works

1. **Input Processing**: Users paste or type messages into the web interface
2. **Text Preprocessing**: Messages are cleaned using NLTK (removing stopwords, punctuation, lowercasing)
3. **Feature Extraction**: TF-IDF vectorization transforms text into numerical features
4. **Model Prediction**: Multiple ML models analyze the features simultaneously
5. **Result Aggregation**: Results from all models are combined to show predictions and spam risk percentage
6. **Visualization**: Interactive charts display the analysis results

## 🤖 ML Models Used

The system employs three different machine learning algorithms for comprehensive spam detection:

- **Naive Bayes**: Probabilistic classifier based on Bayes' theorem - fast and effective for text classification
- **Logistic Regression**: Statistical model for binary classification - provides high accuracy
- **Random Forest**: Ensemble learning method using multiple decision trees - offers robust and reliable predictions

All models are trained on preprocessed text data and work together to minimize false positives and maximize detection accuracy.

## 📊 Kaggle Dataset

The models are trained on a comprehensive spam dataset sourced from Kaggle, containing thousands of labeled messages categorized as spam or not-spam. The dataset includes diverse examples of SMS and email messages, ensuring the models can handle various types of spam patterns.

## 🌐 Live Demo

**Experience SpamNix in action**: [https://spam-ubh0.onrender.com/](https://spam-ubh0.onrender.com/)

* GitHub: https://github.com/Atryee-Chatterjee
* LinkedIn: www.linkedin.com/in/atryee-chatterjee

---

**Developed during internship at Travarsa Private Limited** | **Made with ❤️ using Flask and Machine Learning**</content>
