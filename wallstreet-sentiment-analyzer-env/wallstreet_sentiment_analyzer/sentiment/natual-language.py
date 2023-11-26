# potentially need to run this line if first time
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


def get_sentiment(text):
    sid = SIA()
    sentiment_score = sid.polarity_scores(text)

    return sentiment_score


sentence = "my stocks were down today"
result = get_sentiment(sentence)
print(f"The sentiment of the sentence is: {result}")
