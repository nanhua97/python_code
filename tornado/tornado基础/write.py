#coding:utf8
import json
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.options as t_opt
from tornado.web import RequestHandler,url
from tornado.options import options,define

class IndexHandler(RequestHandler):
    def get(self):
        """
        self.write("hello Rick")
        self.write("hello Morty")
        self.write("hello Rick&Morty")
        """
        stu={
            "name":"Morty",
            "age":15,
            "gender":1,
        }
        #self.write(stu)
        #write方法会将json格式的数据自动转化为json
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("Content-Type","Application/json;charset:UTF-8")

if __name__ == "__main__":
    app = t_web.Application([
            (r'/',IndexHandler),
        ],debug=True)
    app.listen(8000)
    t_io.IOLoop.current().start()

