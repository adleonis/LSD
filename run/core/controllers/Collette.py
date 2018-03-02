#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Collette',__name__,url_prefix='/Collette')


@controller.route('/', methods=['GET'])
def lookup(name='Collette'):
    return render_template('Collette.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Collette loves '+word
    return render_template('Collette.html', name=name)

