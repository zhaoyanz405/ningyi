# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
from src.data import article_list

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    title_list = [ art['title'] for art in article_list]
    return render_template('news.html', titles=title_list)

@app.route('/n-detail')
def detail():
    return render_template('n-detail.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
