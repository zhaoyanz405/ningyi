# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
