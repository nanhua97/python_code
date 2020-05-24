#coding:utf8
import json
import tornado.web as t_web
import tornado.ioloop as t_io
import tornado.httpserver as t_http
import tornado.options as t_opt
from tornado.options import options,define

define("port",default=8000,type=int,help="this is port")

class IndexHandler(t_web.RequestHandler):
    def post(self):
        '''
        print(self.request.headers.get("Content-Type"))
        print(self.request.body)
        #JSON不识别单引号，会报错
        json_data = self.request.body.replace("'",'"')
        json_send = json.loads(json_data)
        self.write(str(json_send))
        '''
        '''
        print(type(self.request.files))
        print(self.request.files.keys())
        print(self.request.files["imgName"][0]["body"])

        '''
        files = self.request.files
        image_files = files.get('imgName')
        
        with open('./image','w+') as f:
            image = image_files[0]["body"]
            f.write(image)
        self.write("OK")
if __name__ == "__main__":
    t_opt.parse_command_line()
    app=t_web.Application([
            (r'/',IndexHandler),
        ],debug=True)
    app.listen(options.port)
    t_io.IOLoop.current().start()

