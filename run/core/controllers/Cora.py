#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Cora',__name__,url_prefix='/Cora')


@controller.route('/', methods=['GET'])
def lookup(name='Cora'):
    return render_template('Cora.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Cora loves '+word
    return render_template('Cora.html', name=name)

