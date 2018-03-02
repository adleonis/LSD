#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Rosendo',__name__,url_prefix='/Rosendo')


@controller.route('/', methods=['GET'])
def lookup(name='Rosendo'):
    return render_template('Rosendo.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Rosendo loves '+word
    return render_template('Rosendo.html', name=name)

