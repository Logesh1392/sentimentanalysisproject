🤖 AI Echo - Sentiment Analysis Project

AI Echo is a sentiment analysis project that predicts customer review sentiments (Positive, Negative, Neutral) using Machine Learning models.
The project includes data preprocessing, model training, and a Streamlit web app for deployment.

📂 Project Structure
.
├── 01_data_cleaning_eda.ipynb   # Data cleaning & exploratory data analysis
├── 02_model_training.ipynb      # Model training & evaluation
├── 03_streamlit.py              # Streamlit app for deployment
├── cleaned_reviews.csv          # Cleaned dataset (CSV format)
├── cleaned_reviews.pkl          # Preprocessed dataset (Pickle format)
├── tfidf_vectorizer.pkl         # Saved TF-IDF vectorizer
├── best_random_model.pkl        # Trained Random Forest model
└── README.md                    # Project documentation

🚀 Workflow
1️⃣ Data Cleaning & EDA

Run 01_data_cleaning_eda.ipynb

Steps include:

Text preprocessing (stopword removal, tokenization, etc.)

Data visualization

Sentiment distribution check

2️⃣ Model Training

Run 02_model_training.ipynb

Models compared: Naive Bayes, SVM, Random Forest, LSTM, RNN

Best performing model: Random Forest

Save trained model as best_random_model.pkl

Save vectorizer as tfidf_vectorizer.pkl

3️⃣ Deployment

Run 03_streamlit.py

Features:

Predict sentiment for a single review

Upload CSV file for bulk predictions

Download predictions as a CSV

🔧 Installation & Setup
1️⃣ Clone or Download Repository
git clone https://github.com/yourusername/ai-echo.git
cd ai-echo

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows

3️⃣ Install Dependencies

Create a requirements.txt with:

streamlit
pandas
scikit-learn
matplotlib
seaborn
nltk


Install using:

pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run 03_streamlit.py

📊 Example Usage
Single Review

Input:

"I loved this car rental service, it was smooth and easy!"


Output:

Positive

Bulk Review

Upload a CSV with column review

Get predictions + download as CSV

👨‍💻 Author

AI Echo Team
Built with ❤️ using Python, Streamlit, and Machine Learning
