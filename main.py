from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def success():
    return "<h1>Hi</h1>"


if __name__ == '__main__':
    app.run(debug=True)
