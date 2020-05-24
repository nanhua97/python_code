#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.web import RequestHandler
from tornado.options import options,define

define("port",default=8000,type=int,help="this is the port")
#自定义错误页面
class IndexHandler(RequestHandler):
    def get(self):
        err_code = self.get_argument("code", None) 
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        print(err_code)
        print(err_title)
        print(err_content)
        if err_code:
            self.send_error(int(err_code),title=err_title,content=err_content)
        else:
            self.write("23")
    def write_error(self,status_code,**kwargs):
        self.write(kwargs["title"])
        self.write(kwargs["content"])




if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",IndexHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

