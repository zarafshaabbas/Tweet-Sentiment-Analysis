import pandas as pd
from textblob import TextBlob

# Load tweets
df = pd.read_csv("tweets.csv")

# Sentiment analysis function
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply to tweets
df['Sentiment'] = df['tweet'].apply(get_sentiment)

# Output
print(df)
df.to_csv("labeled_tweets.csv", index=False)
print("\nSaved labeled tweets to 'labeled_tweets.csv'")
