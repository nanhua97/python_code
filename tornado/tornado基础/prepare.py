#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.web import RequestHandler,url
from tornado.options import options,define
import json

define("port",default=8000,type=int,help="this is the port")
class IndexHandler(RequestHandler):
    def prepare(self):
        if self.request.headers.get("Content-Type").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None
    def post(self):
        if self.json_dict:
            for key,value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key,value))
    def put(self):
        if self.json_dict:
            for key,value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key,value))
if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",IndexHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

