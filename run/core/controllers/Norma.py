#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Norma',__name__,url_prefix='/Norma')


@controller.route('/', methods=['GET'])
def lookup(name='Norma'):
    return render_template('Norma.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Norma loves '+word
    return render_template('Norma.html', name=name)

