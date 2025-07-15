import requests
import time
import random
from textblob import TextBlob

ETHERSCAN_API_KEY = "38PP8S4UZSDD3TWAM65GNSIJACTBRZNA2T"
ADDRESS = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Пример адреса

def get_transaction_comments(address, api_key, max_txs=10):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Etherscan API error")

    txs = response.json().get("result", [])
    comments = []
    for tx in txs[:max_txs]:
        fake_comment = random.choice([
            "Great project!", "This looks like a rug pull", "Holding strong!",
            "Scam detected", "Just bought more", "Too risky", "To the moon!"
        ])
        comments.append(fake_comment)
    return comments

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def main():
    print("🔍 Fetching transaction comments...")
    comments = get_transaction_comments(ADDRESS, ETHERSCAN_API_KEY)

    print("🧠 Analyzing mood...")
    for i, comment in enumerate(comments, 1):
        sentiment = analyze_sentiment(comment)
        print(f"{i}. \"{comment}\" → Sentiment: {sentiment}")
        time.sleep(1)

if __name__ == "__main__":
    main()

