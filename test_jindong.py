import re
import docx
from pyquery import PyQuery as pq
doc = pq('https://item.jd.com/44675757996.html',headers={'User-Agent': 'Mozilla/5.0 '
                                                                '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                                                '(KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'},encoding='gbk')
test_comment = [i.text() for i in doc.items('#comment-item comment-column J-comment-column')]
# 因为京东的评论是以加载的方式呈现的，所以直接爬取静态网页是爬不下来的，测试到此结束
