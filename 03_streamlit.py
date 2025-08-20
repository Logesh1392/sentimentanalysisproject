import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Pre-trained Model & Vectorizer
# -------------------------------
with open("best_random_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# -------------------------------
# Streamlit App UI
# -------------------------------
st.set_page_config(page_title="AI Echo - Sentiment Analyzer", layout="wide")
st.title("🤖 AI Echo: Sentiment Analysis App")
st.write("Upload your reviews and analyze sentiment using the best Random Forest model.")

# -------------------------------
# Text Input Prediction
# -------------------------------
st.subheader("🔹 Predict Sentiment for a Single Review")
user_input = st.text_area("Enter a review:", "")

if st.button("Predict Sentiment"):
    if user_input.strip():
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        st.success(f"Predicted Sentiment: **{prediction}**")
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# -------------------------------
# CSV File Upload Prediction
# -------------------------------
st.subheader("📂 Upload CSV for Bulk Prediction")
uploaded_file = st.file_uploader("Upload a CSV file with a 'review' column", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        if "review" not in df.columns:
            st.error("❌ The CSV must contain a 'review' column.")
        else:
            X_input = vectorizer.transform(df["review"].astype(str))
            predictions = model.predict(X_input)
            df["Predicted_Sentiment"] = predictions

            st.success("✅ Predictions complete!")
            st.dataframe(df.head(20))

            # Download option
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Predictions",
                data=csv,
                file_name="predicted_reviews.csv",
                mime="text/csv",
            )
    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
