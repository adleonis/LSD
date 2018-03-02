#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Moises',__name__,url_prefix='/Moises')


@controller.route('/', methods=['GET'])
def lookup(name='Moises'):
    return render_template('Moises.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Moises loves '+word
    return render_template('Moises.html', name=name)

