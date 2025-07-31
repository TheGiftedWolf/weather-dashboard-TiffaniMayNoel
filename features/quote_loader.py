
import pandas as pd
import random
import os

def load_random_quote(csv_path="data/Combined_Quote.csv"):
    if not os.path.exists(csv_path):
        return "Have a great day!"

    try:
        df = pd.read_csv(csv_path)
        if 'Quote' in df.columns:
            return random.choice(df['Quote'].dropna().tolist())
        else:
            return "No 'quote' column found in CSV."
    except Exception as e:
        return f"Error loading quote: {e}"
