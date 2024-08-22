import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class BashRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the content length from the headers
        content_length = int(self.headers['Content-Length'])
        # Read the body of the request
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Start the process in the background
        try:
            subprocess.Popen(post_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable='/bin/bash')

            # Send a response back immediately without waiting for the process to complete
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Process started.")
        except Exception as e:
            # Handle any errors
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Error starting process: {e}".encode('utf-8'))

    def do_GET(self):
        self.send_response(405)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Use POST to start bash commands.")

def run(server_class=HTTPServer, handler_class=BashRequestHandler, port=38866):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
