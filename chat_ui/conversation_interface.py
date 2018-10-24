from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/cui')
def static_page():
    return render_template('cui.html')


if __name__ == '__main__':
    app.run(port=8080)
