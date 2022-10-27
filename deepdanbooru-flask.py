from gevent.pywsgi import WSGIServer
from ddbr_onnx import app

http_server = WSGIServer(("", 12421), app)
http_server.serve_forever()