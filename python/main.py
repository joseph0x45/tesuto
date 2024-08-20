from http.server import SimpleHTTPRequestHandler, HTTPServer
from lib import (
    run_suite, respond, get_query_param,
    get_suite_run_reports
)


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == '/health':
            respond(self, 200)
            return
        if path.startswith('/run'):
            suite = get_query_param(path, "suite")
            if suite is None:
                respond(self, 400)
                self.wfile.write(b'{"error":"No suite name provided"}')
                return
            run_suite(suite)
            respond(self, 200)
            return
        if path.startswith('/report'):
            suite = get_query_param(path, "suite")
            if suite is None:
                respond(self, 400)
                self.wfile.write(b'{"error":"No suite name provided"}')
                return
            get_suite_run_reports(suite)
            respond(self, 200)
            return
        self.send_error(404, "Not Found")


if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    print("Serving on port 8080...")
    httpd.serve_forever()
