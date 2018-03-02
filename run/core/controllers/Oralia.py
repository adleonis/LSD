#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Oralia',__name__,url_prefix='/Oralia')


@controller.route('/', methods=['GET'])
def lookup(name='Oralia'):
    return render_template('Oralia.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Oralia loves '+word
    return render_template('Oralia.html', name=name)

