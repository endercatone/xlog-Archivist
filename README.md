# xlog-Archivist

xlog-Archivist 是[xLog-ArticleURLCrawler](https://github.com/endercatone/xLog-ArticleURLCrawler)的改进版本，它不仅可以爬取URL，还能爬取内容、创作日期等信息并以json格式分别将每篇文章保存到对应的json文件中。

![image-20230520231829638](https://article.biliimg.com/bfs/article/7575458a96d694222abadd0abbde30fb22fafeb2.png)

制作这个程序的目的是为了更方便地将xlog博客上的文章添加到知识库中。

> [在博客上嵌入可以读取文章的ChatGPT](https://endercat.xlog.app/zai-bo-ke-shang-qian-ru-ke-yi-du-qu-wen-zhang-de-chatgpt) 

*本程序使用ChatGPT协助编写*



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
   文章保存成功：在xLog上与ChatGPT对话文章保存成功：在博客上嵌入可以读取文章的ChatGPT
   文章保存成功：免费给Telegram机器人接入GPT-4
   文章保存成功：通过CSS修改文字文章保存成功：Chirper - AI的社区，禁止人类进入文章保存成功：在博客上使用黑条字文章保存成功：使用Python脚本检测OpenAi额度和模型文章保存成功：分享一些OpenAi API KEY
   文章保存成功：更简单地为Arch linux或其衍生系统更换更快的镜像源文章保存成功：免费领取二级域名,使用ClouDNS!
   所有文章保存完毕！
   ```

4. 在`articles`目录找到文章的json文件



## 许可证

该项目使用 MIT 许可证。详细信息请参阅 LICENSE 文件。