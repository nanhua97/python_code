#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.web import RequestHandler,url
from tornado.options import options,define
import json

'''
NO_ERROR
set_default_headers()
initialize()
prepare()
get()
on_finish()

ERROR
set_default_headers()
initialize()
prepare()
post()
set_default_hearders()
write_error()
on_finish()
'''

define("port",default=8000,type=int,help="this is the port")
class IndexHandler(RequestHandler):
    def initialize(self):
        print("this is function:initialize()")
    def prepare(self):
        print("this is function:prepare()")
    def set_default_headers(self):
        print("this is the function:set_default_header()")
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("Rick","C-137")
    def write_error(self,status_code,**kwargs):
        print("this is function:write_error()")
    def get(self):
        print("this is function:get()")
        self.set_header("Rick","summer")
    def post(self):
        print("this is function:post()")
        self.send_error(200)
    def on_finish(self):
        print("this is function:on_finish()")

if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",IndexHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

