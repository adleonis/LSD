#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Lilli',__name__,url_prefix='/Lilli')


@controller.route('/', methods=['GET'])
def lookup(name='Lilli'):
    return render_template('Lilli.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Lilli loves '+word
    return render_template('Lilli.html', name=name)

