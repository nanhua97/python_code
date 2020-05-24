#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http

class IndexHandler(t_web.RequestHandler):
    def get(self):
        self.write('Hello httpServerBind')

if __name__ == "__main__":
    app = t_web.Application([
            (r"/",IndexHandler),
        ])
    #app.listen(8000)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(8000)
    #httpServer.bind(8000)
    #httpServer.start(3)
    t_io.IOLoop.current().start()
