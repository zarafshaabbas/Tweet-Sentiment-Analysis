# Tweet-Sentiment-Analysis

*COMPANY*: CODEC TECHNOLOGIES

*NAME*: ZARAFSHA ABBAS MOLLA

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 1 MONTH

*GUIDE NAME*: VAISHALI SHRIVASTAVA

# Tweet Sentiment Analysis

This project is focused on analyzing the sentiment of tweets using Natural Language Processing (NLP). The goal is to classify tweets into one of three categories: positive, negative, or neutral, based on their textual content. It is designed as a beginner-friendly project using Python and the NLTK library.

## Project Overview

The script reads a CSV file containing tweets, processes each tweet to clean the text, and then applies sentiment analysis to determine the mood expressed in each tweet. The result is saved into a new CSV file with a sentiment label added.

## Features

* Reads tweets from a CSV file (tweets.csv)
* Applies basic text preprocessing
* Performs sentiment analysis using NLTK’s SentimentIntensityAnalyzer
* Outputs a labeled dataset with sentiment classification
* Helps in understanding how to work with text data in Python

## Tools and Technologies Used

* Python (3.x)
* pandas for data manipulation
* nltk for sentiment analysis

## How It Works

1. The program loads tweet data from a file named tweets.csv.
2. Each tweet is passed through a sentiment analysis function.
3. The sentiment (positive, negative, or neutral) is calculated based on the compound score from the VADER sentiment analyzer.
4. A new column named “sentiment” is added to the dataset.
5. The processed data is saved into labeled\_tweets.csv for later use or visualization.

## Input Format

The input file must be named tweets.csv and should contain a column named tweet. Each row in this column should contain one tweet.

Example:

* I am feeling great today!
* This is a bad service.
* The movie was okay, nothing special.

## Output

A new file is created (labeled\_tweets.csv) that contains the original tweet along with a new column named sentiment. This column contains values like positive, negative, or neutral based on the analysis.

## Notes

* Make sure the tweets are properly quoted in the CSV file to avoid parsing issues.
* If the file structure is incorrect or malformed, the script may raise a parser error.
* You can easily modify the script to read from different input formats or columns.
