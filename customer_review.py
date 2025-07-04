import pandas as pd
import mysql.connector
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os  # ✅ to print and open file path

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Fetch data from the MySQL database
def fetch_data_from_sql():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aluchen123,',
        database='business'
    )
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM business.`dbo.customers`"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Try loading the data once
try:
    customer_reviews_df = fetch_data_from_sql()
    print("✅ Data loaded successfully.")
    print(customer_reviews_df.head())
except Exception as e:
    print("❌ Failed to load data:", e)
    exit()

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def calculate_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

def categorize_sentiment(score, rating):
    if score > 0.05:
        if rating >= 4:
            return 'Positive'
        elif rating == 3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <= 2:
            return 'Negative'
        elif rating == 3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'

def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Apply sentiment analysis
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Print results
print(customer_reviews_df.head())

# ✅ Save and show file location
output_file = 'fact_customer_reviews_.csv'
print("📁 Saving to:", os.path.abspath(output_file))
customer_reviews_df.to_csv(output_file, index=False)

# ✅ (Optional) Open the file automatically (Windows only)
try:
    os.startfile(output_file)
except Exception:
    pass  # Safe to ignore if not on Windows
