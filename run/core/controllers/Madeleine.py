#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Madeleine',__name__,url_prefix='/Madeleine')


@controller.route('/', methods=['GET'])
def lookup(name='Madeleine'):
    return render_template('Madeleine.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Madeleine loves '+word
    return render_template('Madeleine.html', name=name)

