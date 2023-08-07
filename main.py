from website import create_app
from gevent.pywsgi import WSGIServer

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    # Production using wsgi server
    app.run(port=5000)
    
