#-*-coding:utf8-*-
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('HELLO WORLD')


if __name__=='__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
