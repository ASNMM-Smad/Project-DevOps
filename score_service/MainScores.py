from flask import Flask
import utils

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

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)


'''
#import threading, logging
#from  .. tests.e2e import test_scores_service
#from multiprocessing import Process

def run_app():
    app.run(host='127.0.0.1', port=5000)
    #test_scores_service(current_score)

def wait_for_calling():
    first_thread = threading.Thread(target=run_app)
    first_thread.start()

def starting_service():
    app.run(host='127.0.0.1', port=5000)
'''
