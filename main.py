from website import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    # Production using wsgi server
    app.run(host='0.0.0.0:$PORT',port=5000)
    
