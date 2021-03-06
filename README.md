## 收集含关键词的新浪微博数据

**利用微博高级搜索功能，按关键字搜集一定时间范围内的微博。**详见[博客](http://blog.csdn.net/jiange_zh/article/details/47361555)

1. 大体思路：构造URL，爬取网页，然后解析网页中的微博信息。
> 登陆新浪微博，进入高级搜索，输入关键字“广电禁令”，选择”实时“，时间为“2015-08-07-0:2015-08-08-0”，地区为“广东-广州”，之后发送请求会发现地址栏变为如下:
>	http://s.weibo.com/weibo/%25E4%25B8%25AD%25E5%25B1%25B1%25E5%25A4%25A7%25E5%25AD%25A6&region=custom:44:1&typeall=1&suball=1&timescope=custom:2015-08-07-0:2015-08-08-0&Refer=g
> > + 固定地址部分：http://s.weibo.com/weibo/
> > + 关键字二次UTF-8编码：%25E4%25B8%25AD%25E5%25B1%25B1%25E5%25A4%25A7%25E5%25AD%25A6
> > + 搜索地区：region=custom:44:1
> > + 搜索时间范围：timescope=custom:2015-08-07-0:2015-08-08-0
> > + 可忽略项：Refer=g
> > + 某次请求的页数：page=1
> *另外，高级搜索最多返回50页微博，那么时间间隔设置最小为宜。所以该类设置为搜集一定时间段内最多50页微博*

2. 依赖包：lxml(解析网页)、rsa(模拟登陆)、xlrd（操作excel）、xlutils（excel读写）

3. 导出结果到excel：

由于导出结果到excel的库不够完善，每次导出的数据无法直接追加到excel末尾。

因此我采取的方法是：

在excel的（0,0）格存放当前已存放的总行数，下次再次打开的时候，新建一个excel表，将旧的数据复制到新的表中，再根据总行数向后追加新的数据。

