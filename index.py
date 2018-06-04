# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
from src.data import article_list

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    title_list = [art['title'] for art in article_list]
    return render_template('news.html', titles=title_list)


@app.route('/n-detail/<name>')
def detail(name):
    title_list = [art['title'] for art in article_list]
    for art in article_list:
        wrong_art = {
            'title': "没有这篇文章"
        }
        if name == art['title']:
            return render_template('n-detail.html', article=art)

    return render_template('n-detail.html', article=wrong_art)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
