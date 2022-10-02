import snscrape.modules.twitter as sntwitter
import pandas as pd
from tabulate import tabulate

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('uu pse lang:id').get_items()):
    if i > 500:
        break
    attributes_container.append([tweet.date,tweet.user.username,tweet.content])
# Creating a dataframe from the tweets list above
print(attributes_container)
tweets_df = pd.DataFrame(attributes_container, columns=["Tanggal Tweet", "Username", "Tweet"])
tweets_df.to_csv("twitter_raw.csv")