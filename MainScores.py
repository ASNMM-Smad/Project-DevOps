from flask import Flask
import utils
import threading

app = Flask(__name__)

@app.route('/')
def score_server(status_code=0):
    with open(utils.SCORES_FILE_NAME, 'r+') as reading:
        score = reading.read()
    if status_code == 0:
        return f'''<html>
        <head>
            <title>Scores Game</title>
        </head>
        
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>'''

    else:
        return f'''<html>
        <head>
            <title>Scores Game</title>
        </head>

        <body>
            <h1><div id="score" style="color:red">{status_code}</div></h1>
        </body>
        </html>'''


def run_app():
    app.run(host='127.0.0.1', port=5000)

def wait_for_calling():
    first_thread = threading.Thread(target=run_app)
    first_thread.start()

