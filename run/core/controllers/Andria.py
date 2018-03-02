#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Andria',__name__,url_prefix='/Andria')


@controller.route('/', methods=['GET'])
def lookup(name='Andria'):
    return render_template('Andria.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Andria loves '+word
    return render_template('Andria.html', name=name)

