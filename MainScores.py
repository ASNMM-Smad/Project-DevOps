
from flask import Flask

app = Flask(__name__)

@app.route('/')
def score_server(score, status_code):
    app.run()
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

'''if __name__ == '__main__':
    app.run()
'''
