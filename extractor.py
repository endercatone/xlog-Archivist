import re
import requests

def extract_article_info(article):
    article_info = {}
    article_info["title"] = article["title"]
    article_info["created_at"] = article["date_published"]

    # 发送请求并获取响应
    response = requests.get(article["url"], allow_redirects=False)

    # 提取重定向后的URL
    if "Location" in response.headers:
        final_url = response.headers["Location"]
    else:
        final_url = article["url"]

    article_info["url"] = final_url

    # 清除 content_html 字段中的 HTML 标签和无用字符
    content_html = article["content_html"]
    cleaned_content = re.sub("<.*?>", "", content_html)  # 删除 HTML 标签
    cleaned_content = re.sub(r"\s+", " ", cleaned_content)  # 删除多余的空白字符
    cleaned_content = cleaned_content.replace("Copy", "")  # 移除 " Copy " 字符(代码块的copy键)
    article_info["content"] = cleaned_content.strip()

    return article_info
