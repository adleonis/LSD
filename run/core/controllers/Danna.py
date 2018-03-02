#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Danna',__name__,url_prefix='/Danna')


@controller.route('/', methods=['GET'])
def lookup(name='Danna'):
    return render_template('Danna.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Danna loves '+word
    return render_template('Danna.html', name=name)

