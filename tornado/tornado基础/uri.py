#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.web import RequestHandler,url
from tornado.options import options,define

define("port",default=8000,type=int,help="this is the port")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello rick")
        #City_url = self.reverse_url("City")
        #self.write('<a href="%s">City</a>'%City_url)
        self.write(self.request.uri)
class SubjectCityHandler(RequestHandler):
    def get(self,subject,city):
        self.write("subject:%s<br/>city:%s"%(subject,city))
        self.write(self.request.uri)

class SubjectDateHandler(RequestHandler):
    def get(self,date,subject):
        self.write("Date:%s<br/>Subject:%s"%(date,subject))
        self.write(self.request.uri)

if __name__ ==  "__main__":
    t_opt.parse_command_line()
    app=t_web.Application([
            url(r"/",IndexHandler),
            url(r"/sub-city/(.+)/([a-z]+)",SubjectCityHandler,name="City"),
            url(r"/sub-date/(?P<subject>.+)/(?P<date>\d+)",SubjectDateHandler,name="Date"),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()


