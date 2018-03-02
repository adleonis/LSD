#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Jeanette',__name__,url_prefix='/Jeanette')


@controller.route('/', methods=['GET'])
def lookup(name='Jeanette'):
    return render_template('Jeanette.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Jeanette loves '+word
    return render_template('Jeanette.html', name=name)

