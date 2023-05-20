import os
import threading
from fetcher import fetch_article_data
from saver import save_article_data
from extractor import extract_article_info

# 用户输入博客的 URL
blog_url = input("请输入博客的 URL：")

# 获取博客的 JSON 数据
json_data = fetch_article_data(blog_url)

# 创建保存文章的目录
save_directory = "articles"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# 定义保存文章的函数
def save_article(article):
    article_info = extract_article_info(article)
    title = article_info["title"]
    save_article_data(title, article_info, save_directory)
    print(f"文章保存成功：{title}")

if json_data:
    threads = []
    for article in json_data["items"]:
        thread = threading.Thread(target=save_article, args=(article,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有文章保存成功！")
else:
    print("无法获取博客数据，请检查博客的 URL 是否正确。")
