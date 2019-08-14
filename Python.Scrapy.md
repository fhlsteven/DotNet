# scrapy爬虫框架

## 一. Scrapy入门 [**from**](https://woodenrobot.me/2017/01/01/scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%E6%95%99%E7%A8%8B%EF%BC%88%E4%B8%80%EF%BC%89-Scrapy%E5%85%A5%E9%97%A8/])

### Scrapy简介

>Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。</br>
其最初是为了 页面抓取 (更确切来说, 网络抓取 )所设计的， 也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。

### 架构概览

![scrapy_architecture](img/python.scrapy/scrapy_architecture.png)

### 各组件作用

#### Scrapy Engine

>引擎负责控制数据流在系统中所有组件中流动，并在相应动作发生时触发事件。 详细内容查看下面的数据流(Data Flow)部分。

此组件相当于爬虫的“大脑”，是整个爬虫的调度中心。

#### 调度器(Scheduler)

>调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎。

初始的爬取URL和后续在页面中获取的待爬取的URL将放入调度器中，等待爬取。同时调度器会自动去除重复的URL（如果特定的URL不需要去重也可以通过设置实现，如post请求的URL）

#### 下载器(Downloader)

>下载器负责获取页面数据并提供给引擎，而后提供给spider。

#### Spiders

>Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。 每个spider负责处理一个特定(或一些)网站。

#### Item Pipeline

>Item Pipeline负责处理被spider提取出来的item。典型的处理有清理、 验证及持久化(例如存取到数据库中)。

当页面被爬虫解析所需的数据存入Item后，将被发送到项目管道(Pipeline)，并经过几个特定的次序处理数据，最后存入本地文件或存入数据库。

#### 下载器中间件(Downloader middlewares)

>下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。

通过设置下载器中间件可以实现爬虫自动更换user-agent、IP等功能。

#### Spider中间件(Spider middlewares)

>Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出(items及requests)。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。

#### 数据流(Data flow)

>1. 引擎打开一个网站(open a domain)，找到处理该网站的Spider并向该spider请求第一个要爬取的URL(s)。
>2. 引擎从Spider中获取到第一个要爬取的URL并在调度器(Scheduler)以Request调度。
>3. 引擎向调度器请求下一个要爬取的URL。
>4. 调度器返回下一个要爬取的URL给引擎，引擎将URL通过下载中间件(请求(request)方向)转发给下载器(Downloader)。
>5. 一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(返回(response)方向)发送给引擎。
>6. 引擎从下载器中接收到Response并通过Spider中间件(输入方向)发送给Spider处理。
>7. Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。
>8. 引擎将(Spider返回的)爬取到的Item给Item Pipeline，将(Spider返回的)Request给调度器。
>9. (从第二步)重复直到调度器中没有更多地request，引擎关闭该网站。

### **建立Scrapy爬虫项目流程**

1. 安装Python

    学习Python的书
    1. [Automate the Boring Stuff With Python](https://automatetheboringstuff.com/)
    2. [How To Think Like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/)
    3. [Learn Python 3 The Hard Way](https://learnpythonthehardway.org/python3/)

2. 安装[scrapy](https://scrapy.org/)
   > 看文档是最好的学习方式

   * [scrapy官方文档](https://docs.scrapy.org/en/latest/)
   * [scrapy中文文档](https://scrapy-chs.readthedocs.io/zh_CN/latest/)

``` bash
    pip install scrapy
```

在开始爬取之前，首先要创建一个新的Scrapy项目.

进入你打算存储代码的目录中，运行下列命令:

``` bash
    scrapy startproject scrapyspider
```

该命令将会创建包含下列内容的`scrapyspider`目录

``` folder
scrapyspider/
    scrapy.cfg
    scrapyspider/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
```

这些文件分别是:

* scrapy.cfg: 项目的配置文件。
* scrapyspider/: 该项目的python模块。之后您将在此加入代码。
* scrapyspider/items.py: 项目中的item文件。
* scrapyspider/pipelines.py: 项目中的pipelines文件。
* scrapyspider/settings.py: 项目的设置文件。
* scrapyspider/spiders/: 放置spider代码的目录。

### 编写第一个爬虫(Spider)

Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类。

其包含了一个用于下载的初始URL，如何跟进网页中的链接以及如何分析页面中的内容， 提取生成 item 的方法。

为了创建一个Spider，必须继承`scrapy.Spider`类， 且定义以下三个属性:

>* `name`: 用于区别Spider。该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
>* `start_urls`: 包含了Spider在启动时进行爬取的url列表。因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
>* `parse()` 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的`Response`对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的`Request`对象。

以下为我们的第一个Spider代码，保存在`scrapyspider/spiders`目录下的`mapBD_spider.py`文件中:

``` python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mapBD"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

### 运行爬虫程序

打开`cmd`到项目文件夹的最顶层,在`cmd`输入一下命令

``` cmd
    scrapy crawl mapBD
```

然后就能看到一大堆的消息,（多的文件自己看吧）

```log
... (omitted for brevity)
2019-08-14 18:13:30 [scrapy.core.engine] INFO: Spider opened
2019-08-14 18:13:30 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2019-08-14 18:13:30 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2019-08-14 18:13:31 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2019-08-14 18:13:31 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2019-08-14 18:13:31 [mapBD] DEBUG: Saved file quotes-2.html
2019-08-14 18:13:32 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2019-08-14 18:13:32 [mapBD] DEBUG: Saved file quotes-1.html
2019-08-14 18:13:32 [scrapy.core.engine] INFO: Closing spider (finished)
...
```

----

## 相关文章

[python爬虫框架——Scrapy架构原理介绍](
https://blog.csdn.net/u013332124/article/details/80645690)
