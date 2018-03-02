#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Roberto',__name__,url_prefix='/Roberto')


@controller.route('/', methods=['GET'])
def lookup(name='Roberto'):
    return render_template('Roberto.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Roberto loves '+word
    return render_template('Roberto.html', name=name)

