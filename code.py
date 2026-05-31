df=pd.read_csv('sentiment_dataset_mining.csv')
df.head()
import pandas as pd
import re
from textblob import TextBlob
def clean_text(text):
    if not isinstance(text, str):
        return text

    # Fix extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Correct minor spelling errors using TextBlob
    text = str(TextBlob(text).correct())
    return text

def correct_label(text, label):
    if not isinstance(text, str) or text is None:
        return label

    # Determine sentiment polarity
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Load the noisy dataset
df_noisy = pd.read_csv("sentimentdataset_noisy.csv")

# Clean text and correct labels
df_noisy["Text"] = df_noisy["Text"].apply(clean_text)
df_noisy["Sentiment"] = df_noisy.apply(lambda row: correct_label(row["Text"], row["Sentiment"]), axis=1)

# Save the cleaned dataset
clean_file_path = "sentimentdataset_cleaned.csv"
df_noisy.to_csv(clean_file_path, index=False)

print("Cleaning complete. File saved at:", clean_file_path)
