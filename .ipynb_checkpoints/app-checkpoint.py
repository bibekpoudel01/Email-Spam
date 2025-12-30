import pickle
import streamlit as st

# Load trained model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Load labels (optional, fallback to default)
labels = {0: "ham", 1: "spam"}
try:
    with open("labels.pkl", "rb") as f:
        labels = pickle.load(f)
except:
    pass


text_input = st.text_area("Enter email text:")


if text_input:
    X = tfidf.transform([text_input])
    prob = model.predict_proba(X)[:, 1][0]
    pred_label = "spam" if prob >= threshold else "ham"
    st.write("Prediction:", pred_label)
    st.write("Probability of spam:", round(prob, 4))
