#coding:utf8
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import os
from tornado.web import RequestHandler,url,StaticFileHandler

class IndexHandler(RequestHandler):
    def get(self):
        self.render("index2.html")
    def post(self):
        print(self.request.headers["Cookie"])
        self.write("hello world")

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
            (r"/",IndexHandler),
        ],
        debug=True,
        static_path = os.path.join(current_path,"statics"),
        template_path = os.path.join(current_path,"templates"),
        )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
