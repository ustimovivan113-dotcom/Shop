from http.server import HTTPServer, BaseHTTPRequestHandler
import os

# Путь к папке с шаблонами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # На ЛЮБОЙ запрос возвращаем contacts.html
        file_path = os.path.join(TEMPLATE_DIR, 'contacts.html')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))

        except FileNotFoundError:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>404 - File not found</h1>')


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()