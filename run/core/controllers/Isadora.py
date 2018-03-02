#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Isadora',__name__,url_prefix='/Isadora')


@controller.route('/', methods=['GET'])
def lookup(name='Isadora'):
    return render_template('Isadora.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Isadora loves '+word
    return render_template('Isadora.html', name=name)

