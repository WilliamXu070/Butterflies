import requests
from bs4 import BeautifulSoup
import json
# Replace with the actual auction URL
url = "https://www.32auctions.com/organizations/117970/auctions/176290"

# Simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

data = []

if response.status_code == 200:
    print("Page fetched successfully")
    soup = BeautifulSoup(response.text, "html.parser")
    # Example: Find all auction items
    items = soup.find_all("a", class_="col-lg-3 col-md-4 col-6 item")  # Update with actual class
    print(f"Found {len(items)} items")
    for item in items:
        title = None
        price = None
        path = None
        link = None
        try:
            title = item.find("h5", class_="text-truncate-2 narrow").text.strip()  # Update class
            price = item.find("span", class_="currency-amount").text.strip()  # Update class
            path = item.find("img", alt=title)["src"]  # Update class
            link = item["href"]
            print(f"Title: {title}\nPrice: {price}\nLink: {link}\n")
        except:
            price = "Attributes not found"
        print(title, price, link)
        data.append({
            "id": len(data) + 1,
            "title": title,
            "price": price,
            "path": path,
            "link": link
            #"path": "https://32auctions.com" + item["href"]  # Update with actual attribute
        })
else:
    print("Failed to fetch page:", response.status_code)

with open('api/gallery.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)