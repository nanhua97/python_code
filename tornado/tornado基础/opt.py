#coding:utf8
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
'''
from tornado.options import options,parse_command_line
options.logging = None
parse_command_line()
'''
t_opt.define("port",default=8000,type=int,help="this is the port")
t_opt.define("rick",default=[],type=str,multiple=True,help='a b c d')

class IndexHandler(t_web.RequestHandler):
    def get(self):
        self.write("Hello options")
if __name__ == "__main__":
    #t_opt.parse_command_line()
    t_opt.parse_config_file("./config")
    print(t_opt.options.rick)

    app = t_web.Application([
            (r'/',IndexHandler),
        ])
    httpServer = t_http.HTTPServer(app)
    httpServer.listen(t_opt.options.port)
    t_io.IOLoop.current().start()
    #运行   python opt.py --port==9000 --rick=a,b,c,d
