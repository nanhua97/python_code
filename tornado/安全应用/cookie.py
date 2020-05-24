#coding:utf8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.web import RequestHandler,url
from tornado.options import define,options
import time

define("port",default=8000,type=int,help="this is the port")

class IndexHandler(RequestHandler):
    def get(self):
        '''
        self.set_cookie("Rick","BAIDU")
        self.set_cookie("Morty","C-137",path="/new",expires=time.strptime("2019-2-28 10:48:00","%Y-%m-%d %H:%M:%S"))
        self.set_cookie("lo","lby",expires_days=10)
        #使用time.mktime将本地时间转换为UTV标准时间
        self.set_cookie("R_lv","lby",expires=time.mktime(time.strptime("2019-2-28 10:48:00","%Y-%m-%d %H:%M:%S")))
        '''
        #self.set_header("Set-Cookie","n5=v5; expires=Fri, 11 Nov 2016 15:59:59 GMT; Path=/")
        lo = self.get_cookie("lo")
        self.write("<p>"+lo+"</p>")
        self.clear_cookie("Rick")
        '''
        self.clear_cookie(name,path='/',domain=None)
        删除名为name并同时匹配domain和path的cookie
        self.clear_all_cookies(path='/',domain=None)
        删除同时匹配domain和path的所有cookie
        '''
        self.write("OK")
class BaiduHandler(RequestHandler):
    def get(self):
        self.write("OK BAIDU")
if __name__ == "__main__":
    app = tornado.web.Application([
            (r'/',IndexHandler),
            (r'^/baidu$',BaiduHandler),
        ],debug=True)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(options.port)
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()
