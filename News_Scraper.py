# Name : Subham Kothari
# Date : 07-08-2025
# News_Scraper.py


import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve content. Status Code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []

        # Try to find common headline tags
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            text = tag.get_text(strip=True)
            if text and len(text) > 10:  # avoiding very short or empty texts to make headline better
                headlines.append(text)

        return headlines

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_to_file(headlines, filename="headlines.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for idx, headline in enumerate(headlines, 1):
                file.write(f"{idx}. {headline}\n")
        print(f"Saved {len(headlines)} headlines to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    url = "https://www.bbc.com/news"  # I can change this to any public news website
    print(f"Fetching headlines from {url}...")
    headlines = fetch_headlines(url)
    
    if headlines:
        save_to_file(headlines)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
