#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Wally',__name__,url_prefix='/Wally')


@controller.route('/', methods=['GET'])
def lookup(name='Wally'):
    return render_template('Wally.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Wally loves '+word
    return render_template('Wally.html', name=name)

