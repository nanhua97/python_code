#coding:utf8
import tornado.web
from tornado.web import RequestHandler
import torndb

class Application(tornado.web.Application):
    handlers=[
        (r'/',IndexHandler),
        (r'^/get$',GetHandler),
        (r'^/quert$',QueryHandler),
        ]
    settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),'templates'),
            static_path=os.path.join(os.path.dirname(__file__),'statics'),
            debug=True,
        )
    super(Application,self).__init__(handlers,**settings)
    self.db = torndb.Connection(
            host='127.0.0.1',
            database='tornado',
            user='root',
            password='1121'
        )
class IndexHandler(RequestHandler):
    def post(self):
        title = self.get_argument("title")
        position = self.get_argument("position")
        price = self.get_argument("price")
        score = self.get_argument("score")
        comments = self.get_argument("comments")
        try:
            self.application.db.execute("insert into house(title,position,price,score,comments) VALUES(%s,%s,%s,%s,%s)",title,position,price,score,comments)
        except Exception as e:
            self.write("DB error:%s"%e)
        else:
            self.write("OK %d" % ret)
class GetHandler(RequestHandler):
    def get(self):
        hid=self.get_argument("id")
        ret = self.application.db.get("select title,position,price,score,comments from house where id=%s",hid)
        self.render("index1.html",houses=[ret])
class QueryHandler(RequestHandler):
    def get(self):
        ret = self.application.db.query("select title,position,price,score,comments from house limit 10")
        self.render("index1.html",houses=[ret])
if __name__ == "__main__":
    app = Application()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
