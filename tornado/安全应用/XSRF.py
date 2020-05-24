#coding:utf8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.web import RequestHandler,url
from tornado.options import options,define

define("port",default=8000,type=int,help="this is port")
'''
#127.0.0.1:8000
class IndexHandler(RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie)+1 if cookie else 1
        self.set_secure_cookie("count",str(count))
        self.write(
                '<html><head><title>Cookie计数器</title></head>'
                '<body><h1>您已访问本页%d次。</h1>' % count +
                '</body></html>'    
            )
'''
#127.0.0.1:9000 因把图片的连接指向了127.0.0.1:8000 所以自动启用了cookie
class IndexHandler(RequestHandler):
    def get(self):
        self.write(
                '<html><head><title>被攻击的网站</title></head>'
                '<body><h1>此网站的图片链接被修改了</h1>'
                '<img alt="这应该是图片" src="http://127.0.0.1:8000/?f=9000/">'
                '</body></html>'    
            )
if __name__ == "__main__":
    app = tornado.web.Application([
            (r'/',IndexHandler),
        ])
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

