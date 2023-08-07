from website import create_app
from gevent.pywsgi import WSGIServer

app = create_app()

if __name__ == '__main__':
    # app.run(debug=False)
    # Production using wsgi server
    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()
    
