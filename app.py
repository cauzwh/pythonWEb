#!/usr/bin/python
#-*-coding:utf-8-*-

import web # web包

urls = (
  '/', 'index'
)

app = web.application(urls, globals()) # web的application方法，建新的app

class index:
    def GET(self):
        greeting = "Hello World" # 字符串
        return greeting

if __name__ == "__main__":
    app.run()
