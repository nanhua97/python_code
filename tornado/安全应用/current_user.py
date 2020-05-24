#coding:utf8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.web import RequestHandler,StaticFileHandler,url
from tornado.options import options,define
import os

define("port",default="8000",type=int,help="this is the port")

class ProfileHandler(RequestHandler):
    def get_current_user(self):
        user_name = self.get_argument("name",None)
        return user_name
    @tornado.web.authenticated
    def get(self):
        self.write("这是我的个人主页")

class LoginHandler(RequestHandler):
    def get(self):
        self.write("登陆页面")
        #next记录的是/login转过来之前的页面
        next = self.get_argument("next","/")
        self.redirect(next+"?name=logined")

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
            (r"/",ProfileHandler),
            (r"/login",LoginHandler),
        ],
        debug=True,
        login_url="/login",
        static_path = os.path.join(current_path,"statics"),
        template_path = os.path.join(current_path,"templates")
        )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
