#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.options as t_opt
import tornado.httpserver as t_http
from tornado.web import RequestHandler,url
from tornado.options import options,define
import json
define("port",default=8000,type=int,help="this is port")

class BaseHandler(RequestHandler):
    def prepare(self):
        if self.request.headers.get("Content-Type").startswith("application/json"):
            self.dict_json = json.loads(self.request.body)
        else:
            self.dict_json = None
    def post(self):
        if self.dict_json:
            for k,v in self.dict_json.items():
                self.write("<h3>%s</h3><p>%s</p>" % (k,v))
    def get(self):
        err_code = self.get_argument("code",None)
        err_title = self.get_argument("title","")
        err_content = self.get_argument("content","")
        if err_code:
            self.write_error(int(err_code),title=err_title,content=err_content)
        else:
            self.write("ABC")
    def write_error(self,status_code,**kwargs):
        self.write(kwargs["title"])
        self.write(kwargs["content"])
if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",BaseHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

