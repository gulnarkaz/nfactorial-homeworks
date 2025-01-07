import json
def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    protocol = environ['SERVER_PROTOCOL']
    
    if method == 'GET' and path == '/info':
        data = b'{"method": "GET", "url": "/info", "protocol": "HTTP/1.1"}'   
        status = "200 OK"
        response_headers = [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ]
    else:
        data = b"Not Found\n"
        status = "404 Not Found"
        response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])