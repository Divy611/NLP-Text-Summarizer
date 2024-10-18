import requests
# API Key: 3b09f8a8c5934cc48b1b5c39b76cc630

API_KEY = '3b09f8a8c5934cc48b1b5c39b76cc630'
url = f'https://newsapi.org/v2/top-headlines'

params = {
    'country': 'us',
    # 'category': 'business',
    'apiKey': API_KEY
}

# Send the GET request to NewsAPI
response = requests.get(url, params=params)

# Convert the response to JSON format
data = response.json()

# Print the news headlines
if data['status'] == 'ok':
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")
else:
    print(f"Error: {data['message']}")
