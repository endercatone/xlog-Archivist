import json
import re
import requests
import os

def fetch_article_data(url):
    feed_url = url.rstrip("/") + "/feed?format=json"
    response = requests.get(feed_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_article_data(title, data, directory):
    filename = f"{title}.json"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def extract_article_info(article):
    article_info = {}
    article_info["url"] = article["url"]
    article_info["title"] = article["title"]
    article_info["created_at"] = article["date_published"]

    # 清除 content_html 字段中的 HTML 标签和无用字符
    content_html = article["content_html"]
    cleaned_content = re.sub("<.*?>", "", content_html)  # 删除 HTML 标签
    cleaned_content = re.sub(r"\s+", " ", cleaned_content)  # 删除多余的空白字符
    cleaned_content = cleaned_content.replace("Copy", "")  # 移除 " Copy " 字符(代码块的copy键)
    article_info["content"] = cleaned_content.strip()

    return article_info

# 用户输入博客的 URL
blog_url = input("请输入博客的 URL：")

# 获取博客的 JSON 数据
json_data = fetch_article_data(blog_url)

# 创建保存文章的目录
save_directory = "articles"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

if json_data:
    for article in json_data["items"]:
        article_info = extract_article_info(article)
        title = article_info["title"]
        save_article_data(title, article_info, save_directory)
    print("文章数据保存成功！")
else:
    print("无法获取博客数据，请检查博客的 URL 是否正确。")
