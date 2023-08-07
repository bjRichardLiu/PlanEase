from website import create_app
from gevent.pywsgi import WSGIServer

app = create_app()

if __name__ == '__main__':
    # app.run(debug=False)
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    
