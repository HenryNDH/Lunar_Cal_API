import http.server
import json
import datetime
from lunarcalendar import Converter, Solar

class LunarDateServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lunar':
            # Get current date
            current_date = datetime.datetime.now().date()

            # Calculate lunar date
            solar = Solar(current_date.year, current_date.month, current_date.day)
            lunar = Converter.Solar2Lunar(solar)
            lunar_day = lunar.day
            lunar_month = lunar.month

            # Prepare response
            response = {
                'Lunar_Day': lunar_day,
                'Lunar_Month': lunar_month
            }

            # Set response headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from all origins
            self.end_headers()

            # Send response
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404, "Not Found")

if __name__ == '__main__':
    server_address = ('', 2000)
    httpd = http.server.HTTPServer(server_address, LunarDateServer)
    print('Starting server...')
    httpd.serve_forever()
