#coding:utf8
import json
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.options as t_opt
import tornado.httpserver as t_http
from tornado.web import RequestHandler,url,StaticFileHandler
from tornado.options import options,define
import os

define("port",default="8000",type=int,help="this is port")
'''
class IndexHandler(RequestHandler):
    def initialize(self,path,default_filename):
        self.path=path
        self.filename=filename
        print(self.path)
        print(self.filename)
    def get(self):
        current_file = self.path+"/"+self.filename
        with open(current_file,'r') as f:
            self.write(f.read())
'''
if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = t_web.Application(
        [
            #(r'/',IndexHandler,{"path":os.path.join(current_path,"static/html"),"default_filename":"index.html"}),
            (r"^/()$",StaticFileHandler,{"path":os.path.join(current_path,"statics/html"),"default_filename":"index.html"}),
            (r"^/view/(.*)$",StaticFileHandler,{"path":os.path.join(current_path,"statics/html")}),
        ],
        debug=True,
        static_path = os.path.join(current_path,"statics"),
        template_path=os.path.join(current_path, "templates"),
        )

    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

