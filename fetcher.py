import requests

def fetch_article_data(url):
    feed_url = url.rstrip("/") + "/feed?format=json"
    response = requests.get(feed_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
