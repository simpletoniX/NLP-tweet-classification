import pandas as pd
import re

df = pd.read_csv("/Users/tonix/PycharmProjects/pythonProject/Cyberbulling/cyberbullying_tweets.csv")

# >>> Feature engineering

# Templates
template1 = re.compile(r"#\w+")
template2 = re.compile(r"@\w+")

# Create new df columns
df['username'] = ""
df['tag'] = ""

# Add new 2 columns and cleaning of text
for index, tweet in enumerate(df['tweet_text']):

    # For tags
    matches1 = len(template1.findall(tweet))
    df.at[index, 'tag'] = matches1

    cleaned_tweet = df.at[index, 'tweet_text'] = template1.sub("", tweet)  # Delete tags

    # For usernames
    matches2 = len(template2.findall(tweet))
    df.at[index, 'username'] = matches2

    df.at[index, 'tweet_text'] = template2.sub("", cleaned_tweet)  # Delete usernames

df.to_csv('cyberbullying_tweets2.csv', index=False)


