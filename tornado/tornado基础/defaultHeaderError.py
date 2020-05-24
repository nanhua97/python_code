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
    def set_default_headers(self):
        print("set_default_headers()")
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("Rick","C-137")
    def get(self):
        print("this is the get()")
        stu = {
            "name":"Morty",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("Rick","summer")
    def post(self):
        print("this is the post()")
        stu = {
            "name":"Morty",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)

"""
#标准状态码不需要写reason，非标准状态玛需要写reason，否则会报错
class Err404Handler(RequestHandler):
    def get(self):
        self.write("Hello Rick-404")
        self.set_status(404)
class Err489Handler(RequestHandler):
    def get(self):
        self.write("Hello Rick-489")
        self.set_status(489,"Morty Error")
class Err481Handler(RequestHandler):
    def get(self):
        self.write("Hello Rick-481")
        self.set_status(481)
#重定向
class LoginHandler(RequestHandler):
    def get(self):
        self.write('<form method="post"><input type="submit" value="登陆"></form>')
    def post(self):
        self.redirect("/")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("主页")
        self.send_error(404,content="404错误")
        #self.write("error")
        #send_error()后不要往缓冲区写东西
class IndexHandler(RequestHandler):
    def get(self):
        err_code = self.get_argument("code",None)
        err_title = self.get_argument("title","")
        err_content = self.get_argument("content","")
        if err_code:
            self.send_error(err_code,sss=123,content=err_content)
            print(err_title)
            print(err_content)
        else:
            self.write("主页")
    def write_error(self,status_code,**kwargs):
        self.write("<h1>出错了，程序员GG正在赶过来！</h1>")
#        self.write(kwargs["sss"])
#       self.write(kwargs["content"])
class IndexHandler(RequestHandler):
    def get(self):
        err_code = self.get_argument(u"code", None) # 注意返回的是unicode字符串，下同
        err_title = self.get_argument(u"title", "")
        err_content = self.get_argument(u"content", "")
        print(err_code)
        print(err_title)
        print(err_content)

        if err_code:
            self.send_error(int(err_code), title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        self.write("<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write("<p>错误名：%s</p>" % kwargs["title"])
        self.write("<p>错误详情：%s</p>" % kwargs["content"])
"""
if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",IndexHandler),
            #(r"/err404",Err404Handler),
            #(r"/err489",Err489Handler),
            #(r"/err481",Err481Handler),
            #(r"/login",LoginHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()
