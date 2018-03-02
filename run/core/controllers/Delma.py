#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Delma',__name__,url_prefix='/Delma')


@controller.route('/', methods=['GET'])
def lookup(name='Delma'):
    return render_template('Delma.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Delma loves '+word
    return render_template('Delma.html', name=name)

