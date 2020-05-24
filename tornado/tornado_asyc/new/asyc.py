#coding:utf8
import tornado
import tornado.web
import tornado.ioloop as t_io
import tornado.options as t_opt
import tornado.httpserver as t_http
from tornado.web import RequestHandler,url
from tornado.options import options,define
import json
define("port",default=8000,type=int,help="this is port")

class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24")
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            if 1 == data["ret"]:
                self.write(u"国家：%s 省份: %s 城市: %s" % (data["country"], data["province"], data["city"]))
            else:
                self.write("查询IP信息错误")

"""
class IndexHandler(RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        #httpClient = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24",callback=self.on_response)
    def on_response(self,response):
        if response.error:
            self.send_error(500)
        else:
            data = json.load(response.body)
            if 1 == data["ret"]:
                self.write(u"国家：%s 省份: %s 城市: %s" % (data["country"], data["province"], data["city"]))
            else:
                self.write("查询IP信息错误")
        self.finish()
"""
if __name__ == "__main__":
    t_opt.parse_command_line()
    app = tornado.web.Application([
            (r"/",IndexHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

