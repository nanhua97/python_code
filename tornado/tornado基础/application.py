#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
from tornado.options import options,define
from tornado.web import url,RequestHandler

define("port",default=8000,type=int,help="run server on the given port")

class IndexHandler(RequestHandler):
    def get(self):
        python_url = self.reverse_url("python_url") #反向解析
        self.write('<a href="%s">to_python</a>'%python_url)

class RickHandler(RequestHandler):
    def initialize(self,morty):
        self.morty = morty
    def get(self):
        self.write(self.morty)

if __name__ == "__main__":
    options.parse_command_line()
    app = t_web.Application([
            (r'/',IndexHandler),
            (r'/cpp',RickHandler,{"morty":"C-137"}),
            url(r'/python',RickHandler,{"morty":"cool_morty"},name="python_url"),
        ],debug=True)
    httpServer=t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()
