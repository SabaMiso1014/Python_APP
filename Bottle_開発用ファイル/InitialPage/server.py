from Bottle_開発用ファイル.InitialPage.server import Bottle, run

app = Bottle()

@app.route('/')
def hello():
    return "Hello World!"

run(app, host='localhost', port=8080)