#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Consuelo',__name__,url_prefix='/Consuelo')


@controller.route('/', methods=['GET'])
def lookup(name='Consuelo'):
    return render_template('Consuelo.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Consuelo loves '+word
    return render_template('Consuelo.html', name=name)

