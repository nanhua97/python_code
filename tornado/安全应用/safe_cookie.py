#coding:utf8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.web import RequestHandler


#base = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

class IndexHandler(RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1
        self.set_secure_cookie("count",str(count))
        self.xsrf_token
        self.write(
                '<html><head><title>Cookie计数器</title></head>'
                '<body><h1>您已访问本页%d次。</h1>' % count + 
                '</body></html>'
            )
    def post(self):
        print("This is post")
        print(self.request.headers["cookies"])
        self.write("HWLLO WORLD")
if __name__ == "__main__":
    settings = dict(
            cookie_secret = "SoQ810Z7QoqQ9e9QplNiSA7lWUb2O0hSnPeUQmM/T+o=",
            xsrf_cookies=True,
            debug=True
            )
    app = tornado.web.Application([
            (r"/",IndexHandler),
        ],**settings)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()

