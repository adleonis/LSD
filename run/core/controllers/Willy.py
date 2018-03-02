#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Willy',__name__,url_prefix='/Willy')


@controller.route('/', methods=['GET'])
def lookup(name='Willy'):
    return render_template('Willy.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Willy loves '+word
    return render_template('Willy.html', name=name)

