#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Evon',__name__,url_prefix='/Evon')


@controller.route('/', methods=['GET'])
def lookup(name='Evon'):
    return render_template('Evon.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Evon loves '+word
    return render_template('Evon.html', name=name)

