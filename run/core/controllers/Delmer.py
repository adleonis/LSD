#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Delmer',__name__,url_prefix='/Delmer')


@controller.route('/', methods=['GET'])
def lookup(name='Delmer'):
    return render_template('Delmer.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Delmer loves '+word
    return render_template('Delmer.html', name=name)

