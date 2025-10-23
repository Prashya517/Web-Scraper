
import requests
from bs4 import BeautifulSoup
import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    page = 1
    print("🔍 Scraping quotes... Please wait.\n")

    while True:
        url = f"http://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            writer.writerow([text, author, ", ".join(tags)])

        print(f"✅ Page {page} scraped successfully.")
        page += 1

print("\n🎉 All quotes scraped successfully! Data saved to 'quotes.csv'")
