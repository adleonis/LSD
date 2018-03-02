#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Tena',__name__,url_prefix='/Tena')


@controller.route('/', methods=['GET'])
def lookup(name='Tena'):
    return render_template('Tena.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Tena loves '+word
    return render_template('Tena.html', name=name)

