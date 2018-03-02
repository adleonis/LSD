#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Rogelio',__name__,url_prefix='/Rogelio')


@controller.route('/', methods=['GET'])
def lookup(name='Rogelio'):
    return render_template('Rogelio.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Rogelio loves '+word
    return render_template('Rogelio.html', name=name)

