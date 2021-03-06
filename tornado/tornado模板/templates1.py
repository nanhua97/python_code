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

class IndexHandler(RequestHandler):
    def get(self):
        house_info={
                "price":398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5.4,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
                }
        self.render("index.html",**house_info)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = t_web.Application(
        [
            #本质是目录拼接
            (r'^/$', IndexHandler),
            (r'^/view/(.*)$', StaticFileHandler,{"path":os.path.join(current_path,"statics/html")}),
        ],
        debug=True,
        #本目录下的statics目录,jingtai文件路径
        static_path=os.path.join(current_path, "statics"),
        #本目录下的templates目录，模板文件路径
        template_path=os.path.join(current_path, "templates"),
    )
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

