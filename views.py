import random, string
from flask import render_template, request, g, abort, redirect, url_for
from flippo import app
from model import Flip, random_word


def new_ident():
    return random_word(100)


@app.before_request
def set_identity():
    g.ident = request.cookies.get('ident', new_ident())


@app.after_request
def set_identity_cookie(response):
    response.set_cookie('ident', g.ident)
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/lets-flip')
def lets_flip():
    new = Flip.make_new(2)
    return redirect(url_for('flip', code=new.code))


@app.route('/flip/<string:code>')
def flip(code):
    loaded = Flip.load(code)
    loaded.add_visit(g.ident)
    return render_template('flip.html', flip=loaded)
