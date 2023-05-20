# xlog-Archivist

xlog-Archivist 是[xLog-ArticleURLCrawler](https://github.com/endercatone/xLog-ArticleURLCrawler)的改进版本，它不仅可以爬取URL，还能爬取内容、创作日期等信息并以json格式分别将每篇文章保存到对应的json文件中。

![image-20230520231829638](https://article.biliimg.com/bfs/article/7575458a96d694222abadd0abbde30fb22fafeb2.png)

制作这个程序的目的是为了更方便地将xlog博客上的文章添加到知识库中。

> [在博客上嵌入可以读取文章的ChatGPT](https://endercat.xlog.app/zai-bo-ke-shang-qian-ru-ke-yi-du-qu-wen-zhang-de-chatgpt) 



# 使用方法



1. 克隆库到本地

   ```shell
   git clone https://github.com/endercatone/xlog-Archivist.git
   ```

2. 安装依赖

   ```shell
   pip install requests
   ```

3. 运行程序

   ```shell
   python main.py
   ```

   示例:

   ```text
   请输入博客的 URL：https://endercat.xlog.app
   文章数据保存成功！
   ```

4. 在`articles`目录找到文章的json文件



## 许可证

该项目使用 MIT 许可证。详细信息请参阅 LICENSE 文件。