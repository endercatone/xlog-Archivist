import os
import threading
import configparser
from fetcher import fetch_article_data
from saver import save_article_data
from extractor import extract_article_info

# 创建配置文件对象
config = configparser.ConfigParser()

# 检查是否是第一次使用
if not os.path.exists('config.ini'):
    # 第一次使用，要求用户输入博客的 URL
    blog_url = input("请输入博客的 URL：")

    # 创建配置文件
    config['Blog'] = {'URL': blog_url}

    # 保存配置文件
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    # 读取配置文件
    config.read('config.ini')

    # 获取博客的 URL
    blog_url = config.get('Blog', 'URL')
    print("已从配置文件中读取URL:",blog_url)

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

    print("所有文章保存完毕！")
else:
    print("无法获取博客数据。")
