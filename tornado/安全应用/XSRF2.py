#coding:utf8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.web import RequestHandler,StaticFileHandler,url
from tornado.options import options,define
import os

define("port",default="8000",type=int,help="this is the port")

class XSRFTokenHandler(RequestHandler):
    def get(self):
        self.xsrf_token
        self.write("OK")
        print(self.request.headers["Cookie"])

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
            (r"/",XSRFTokenHandler),
            (r"^/view/()$",StaticFileHandler,{"path":os.path.join(current_path,"statics/html"),"default_filename":"index.html"})
        ],
        debug=True,
        static_path = os.path.join(current_path,"statics"),
        template_path = os.path.join(current_path,"templates")
        )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
