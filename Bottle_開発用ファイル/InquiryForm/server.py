from bottle import Bottle, run, template

app = Bottle()

@app.route('/otoiawase')
def hello():
    return template('index.tpl')

@app.route('/soushin')
def hello():
    return template('result.tpl')

run(app, host='localhost', port=8080, debug=True)