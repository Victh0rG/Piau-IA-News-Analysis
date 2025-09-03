from src.data_collection import collect_news
from src.data_cleaning import clean_data
from src.sentiment_analysis import analyze_sentiments

if __name__ == "__main__":
    csv_raw = collect_news()
    csv_clean = clean_data(csv_raw)
    analyze_sentiments(csv_clean)