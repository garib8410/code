from textblob import TextBlob

# Sample text
text = "The movie was very interesting and amazing"

# Create TextBlob object
analysis = TextBlob(text)

# Print text
print("Text:", text)

# Print polarity
print("Sentiment Polarity:", analysis.sentiment.polarity)

# Determine sentiment
if analysis.sentiment.polarity > 0:
    print("Sentiment: Positive")
elif analysis.sentiment.polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")