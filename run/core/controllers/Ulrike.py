#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Ulrike',__name__,url_prefix='/Ulrike')


@controller.route('/', methods=['GET'])
def lookup(name='Ulrike'):
    return render_template('Ulrike.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Ulrike loves '+word
    return render_template('Ulrike.html', name=name)

