from google_play_scraper import reviews, Sort
import pandas as pd

result, _ = reviews(
    'com.getmimo',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=4000
)

df = pd.DataFrame(result)

df = df[['userName', 'score', 'content']]
df.dropna(inplace=True)

df.to_csv('mimo_reviews.csv', index=False)

print("Scraping selesai! Data tersimpan dalam mimo_reviews.csv")