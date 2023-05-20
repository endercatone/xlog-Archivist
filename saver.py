import json
import os

def save_article_data(title, data, directory):
    filename = f"{title}.json"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_article_url(title, url, directory):
    filename = "url.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "a") as file:
        file.write(f"{title}: {url}\n")
