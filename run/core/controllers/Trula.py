#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Trula',__name__,url_prefix='/Trula')


@controller.route('/', methods=['GET'])
def lookup(name='Trula'):
    return render_template('Trula.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Trula loves '+word
    return render_template('Trula.html', name=name)

