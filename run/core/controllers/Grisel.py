#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Grisel',__name__,url_prefix='/Grisel')


@controller.route('/', methods=['GET'])
def lookup(name='Grisel'):
    return render_template('Grisel.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Grisel loves '+word
    return render_template('Grisel.html', name=name)

