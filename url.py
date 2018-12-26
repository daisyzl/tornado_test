#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:设置网站的目录结构

# import sys
#
# sys.setdefaultencoding("utf-8")

from handlers import IndexHandler

url = [
    (r'/', IndexHandler),

]
#url指向一个列表,在列表中列出所有目录和对应的处理类

