import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        val1 = self.get_argument('name')
        val2 = self.get_argument('company')
        val3 = self.get_argument('department')
        val4 = self.get_argument('email')
        val5 = self.get_argument('phone')
        self.render("result.html",name=val1, company=val2, department=val3, email=val4, phone=val5)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/sousin", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()