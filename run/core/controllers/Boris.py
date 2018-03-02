#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Boris',__name__,url_prefix='/Boris')


@controller.route('/', methods=['GET'])
def lookup(name='Boris'):
    return render_template('Boris.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Boris loves '+word
    return render_template('Boris.html', name=name)

