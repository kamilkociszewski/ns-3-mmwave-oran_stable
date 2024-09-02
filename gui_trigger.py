import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer


# Function to run startup commands
def run_startup_commands():
    commands = [
        'python3 sim_data_pusher.py',
        'python3 stop_ns3.py'
    ]

    for command in commands:
        # Start the command and wait for it to complete
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable='/bin/bash')
        stdout, stderr = process.communicate()

        # Check if the command started successfully
        if process.returncode != 0:
            print(f"Error: Failed to start '{command}'.\nError Message: {stderr.decode('utf-8')}")
            return False

    return True


# Define the request handler
class BashRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the content length from the headers
        content_length = int(self.headers['Content-Length'])
        # Read the body of the request
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Check if the process "scenario-zero-with_parallel_logging" is already running
        try:
            result = subprocess.run("pgrep -f scenario-zero-with_parallel_logging", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            pids = result.stdout.strip().split('\n')

            if pids and pids[0]:
                # If the process is found, return a 500 error response
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Error: Process 'scenario-zero-with_parallel_logging' is already running.")
                return

            # If the process is not found, start the new process
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
    # Run startup commands and check if they started correctly
    if not run_startup_commands():
        print("Error: One or more startup commands failed to start. Exiting.")
        return

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
