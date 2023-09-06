import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/')
def index():
    return 'HelloWorld!'

if __name__ == '__main__':
    app.run()