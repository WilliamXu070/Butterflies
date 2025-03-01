import requests
from bs4 import BeautifulSoup

# Replace with the actual auction URL
url = "https://www.32auctions.com/organizations/117970/auctions/176290"

# Simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Page fetched successfully")
    soup = BeautifulSoup(response.text, "html.parser")
    # Example: Find all auction items
    items = soup.find_all("a", class_="col-lg-3 col-md-4 col-6 item")  # Update with actual class
    print(f"Found {len(items)} items", items)
    for item in items:
        #print(f"Item: {item}\n")
        title = None
        price = None

        try:
            title = item.find("h5", class_="text-truncate-2 narrow").text.strip()  # Update class
            price = item.find("span", class_="currency-amount").text.strip()  # Update class
        except:
            price = "Price not found"
        print(title, price)
else:
    print("Failed to fetch page:", response.status_code)
