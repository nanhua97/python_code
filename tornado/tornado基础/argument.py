#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.web import RequestHandler
from tornado.options import options,define

define("port",default=8000,type=int,help="this is the port")

class IndexHandler(RequestHandler):
    '''
    def post(self):
        query_arg = self.get_query_argument("a")
        query_args = self.get_query_arguments("a")
        body_arg = self.get_body_argument("a")
        body_args = self.get_body_arguments("a",strip=False)
        arg = self.get_arguments("a")
        args = self.get_arguments("a")
        default_arg = self.get_argument("b","Ricka")
        default_args = self.get_arguments("b")

        try:
            missing_arg = self.get_argument("c")
        except MissingArgumentError as e:
            missing_arg = "cached the MissingArguentError!"
            print(e)
        missing_args = self.get_arguments("c")
        rep = "query_arg:%s<br/>" % query_arg
        rep += "query_args:%s<br/>" % query_args
        rep += "body_arg:%s<br/>"  % body_arg
        rep += "body_args:%s<br/>" % body_args
        rep += "arg:%s<br/>"  % arg
        rep += "args:%s<br/>" % args
        rep += "default_arg:%s<br/>" % default_arg
        rep += "default_args:%s<br/>" % default_args
        rep += "missing_arg:%s<br/>" % missing_arg
        rep += "missing_args:%s<br/>" % missing_args
        self.write(rep)
    '''
    def post(self):
        #获取网址里的参数
        #query_arg = self.get_query_argument('r')
        #query_args = self.get_query_arguments('r')
        #获取body里的参数
        #body_arg = self.get_body_arguments('r')
        #body_args = self.get_body_arguments('r')
        #获取所有参数
        #arg = self.get_argument('r')
        args = self.get_arguments('r')
        #self.write(str(query_args))
        #self.write(str(body_args))
        self.write(str(args))


if __name__ == "__main__":
    t_opt.parse_command_line()
    app = t_web.Application([
            (r"/",IndexHandler),
        ],debug=True)
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(options.port)
    t_io.IOLoop.current().start()

