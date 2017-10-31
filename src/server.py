import tornado.ioloop
import tornado.web
import json
import main_process as mp
import tools
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        res=mp.process(param)
        self.write(json.dumps(res))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(8899)
    tornado.ioloop.IOLoop.current().start()