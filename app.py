from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the dataset
dataframe = pd.read_csv("./dataset/news.csv")

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    dataframe["text"], dataframe["label"], test_size=0.2, random_state=42
)

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Fit and transform TF-IDF vectorizer on training data
tfidf_train = tfidf_vectorizer.fit_transform(x_train)

# Initialize and train PassiveAggressiveClassifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)


@app.route("/detect", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        article = data.get("article")

        # Preprocess the input article using the loaded vectorizer
        article_tfidf = tfidf_vectorizer.transform([article])

        # Make prediction
        pred = pac.predict(article_tfidf)
        # print(pred)
        # print(pred[0])

        # Map prediction to human-readable label
        result = "Fake" if pred[0] == "FAKE" else "Real"

        print(result)

    except Exception as e:
        print(str(e))
        result = "Something went wrong"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
