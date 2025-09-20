from flask import Flask, render_template    


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/glossario')
def glossario():
    return render_template('glossario.html')

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

app.run()