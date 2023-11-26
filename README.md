# Wallstreet-Sentiment-Analyzer
Python & Django project to get r/wallstreetbets comments, analyize sentiment, and display bull/bear results

## Part 1 - Get r/wallstreetbets Comments
- Use reddit bot to download the most recent comments from the r/wallstreetbets subreddit
- Filter out garbage posts that might negatively affect results
## Part 2 - Get Aggregate Sentiment of Downloaded Comments
- Use NLTK (Natural Language Toolkit) library to get the positive/negative rating of each comment
- Get aggregate NLTK rating of all comments downloaded
## Part 3 - Display Bull/Bear Results in Browser Using Django Framework
- Create a simple webpage that displays the percentage of how bullish, or bearish the sentiment is. Percentage should be a value from 0% (bearish) to 100% (bullish)
- Add options to view day sentiment, week (7 days) sentiment, month (30 days) sentiment
- Refresh results every 5 seconds while the program is running
## Part 4 - Connect Django Website to a Server & Domain
- Deploy to AWS server and pick a domain name


# Set Up
## To Active venv
- Navigate to root directory
- Run: wallstreet-sentiment-analyzer-env\Scripts\activate.bat
## Install Django If First Time
- py -m pip install Django
## Verify Installation
- django-admin --version
## Navigate to App Directory
- cd into wallstreet_sentiment_analyzer
## Run Server on localhost
- py manage.py runserver
## Django Tutorial
- For more information, visit https://www.w3schools.com/django/index.php
## install nltk
- py -3 -m pip install nltk
## Sentiment Tutorial
- https://www.datacamp.com/tutorial/text-analytics-beginners-nltk