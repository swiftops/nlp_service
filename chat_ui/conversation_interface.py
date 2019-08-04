"""Starts web server, sets URL and renders CUI."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inbox_page():
    """Page to set rasa core URL."""
    return render_template('index.html')


@app.route('/cui')
def static_page():
    """Actual page rendering CUI."""
    return render_template('cui.html')


if __name__ == '__main__':
    app.run(port=8080)
