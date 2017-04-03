import os
import datetime
from tornado import gen
from tornado.web import RequestHandler, Application, StaticFileHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop



class StatPageHandler(RequestHandler):
    '''Imports from tornado.web.RequestHandler, this class passes data for stats page to be displayed at  <proxy_address>/stats'''

    async def get(self):
        self.render(
            "templates/stats.html",
            uptime_seconds=self.application.uptime_seconds,
            bytes_transferred=self.application.bytes_transferred
        )

class MainHandler(RequestHandler):
    '''Imports from tornado.web.RequestHandler'''

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.client = AsyncHTTPClient()

    async def get(self):

        range_header = self.request.headers.get("Range", None)
        range_query = self.get_argument("range", None)

        if range_query and range_header and range_query != range_header:
            self.send_error(416)
        else:
            headers = self.request.headers

            if range_query:
                headers["Range"] = range_query

            request = HTTPRequest(url=self.request.uri, headers=headers, streaming_callback=self._streaming_callback)

            response = await gen.Task(self.client.fetch, request)

            for header_name, header_value in response.headers.get_all():
                self.add_header(header_name, header_value)

            self.finish()

    def _streaming_callback(self, chunk):

        self.write(chunk)
        self.application.bytes_transferred += len(chunk)
        self.flush()

class App(Application):

    '''Imports from tornado.web.Application'''

    def __init__(self):

        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
        }

        handlers = [
            (r"/stats", StatPageHandler),
            (r"/static/.*", StaticFileHandler, dict(path=settings['static_path'])),
            (r".*", MainHandler),
        ]

        self.bytes_transferred = 0
        self.start_time = datetime.datetime.now()

        super().__init__(handlers, **settings)

    @property
    def uptime_seconds(self):

        return (datetime.datetime.now() - self.start_time).seconds

def main():

    port = os.getenv("PROXY_PORT", 8080)
    address = os.getenv("PROXY_ADDRESS", "0.0.0.0")
    app = App()
    app.listen(port, address=address)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
