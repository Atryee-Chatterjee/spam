from flask import Flask, render_template, request, redirect, url_for
import pickle
import re
import nltk
from nltk.corpus import stopwords
import numpy as np

app = Flask(__name__)

# Load models and vectorizer
with open("spam_models.pkl", "rb") as f:
    models = pickle.load(f)

vectorizer = models["vectorizer"]
rf_model = models["random_forest"]
nb_model = models["naive_bayes"]
lr_model = models["logistic_regression"]

# Download stopwords if not already present
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)

def predict_all(message):
    cleaned_message = clean_text(message)
    vectorized_message = vectorizer.transform([cleaned_message])
    results = {
        "Naive Bayes": nb_model.predict(vectorized_message)[0],
        "Logistic Regression": lr_model.predict(vectorized_message)[0],
        "Random Forest": rf_model.predict(vectorized_message)[0]
    }
    return {k: ("Spam" if v == 1 else "Not Spam") for k, v in results.items()}


### All Routes ###

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Test Route
# @app.route("/test", methods=["GET", "POST"])
# def test():
#     prediction = None
#     if request.method == "POST":
#         message = request.form["message"]
#         prediction = predict_all(message)
#     return render_template("test.html", prediction=prediction)

# About Route
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Route
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Terms and Policy Route
@app.route("/termsAndPolicy")
def terms_and_policy():
    return render_template("termsAndPolicy.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    prediction = {}
    spam_risk = None
    model_accuracy = {
        "Naive Bayes": 0.92,   # replace with your real accuracy
        "Logistic Regression": 0.95,
        "Random Forest": 0.96
    }

    if request.method == "POST":
        message = request.form["message"]
        cleaned_message = message.lower()
        vectorized_message = vectorizer.transform([cleaned_message])

        results = {
            "Naive Bayes": nb_model.predict(vectorized_message)[0],
            "Logistic Regression": lr_model.predict(vectorized_message)[0],
            "Random Forest": rf_model.predict(vectorized_message)[0]
        }

        prediction = {k: ("Spam" if v == 1 else "Not Spam") for k, v in results.items()}

        # Average spam probability (risk percentage)
        spam_count = sum(1 for result in prediction.values() if result == "Spam")
        total_models = len(prediction)
        spam_risk = int((spam_count / total_models) * 100)

    return render_template("test.html", prediction=prediction, spam_risk=spam_risk, model_accuracy=model_accuracy)


if __name__ == "__main__":
    app.run(debug=True)