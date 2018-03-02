#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Hattie',__name__,url_prefix='/Hattie')


@controller.route('/', methods=['GET'])
def lookup(name='Hattie'):
    return render_template('Hattie.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Hattie loves '+word
    return render_template('Hattie.html', name=name)

