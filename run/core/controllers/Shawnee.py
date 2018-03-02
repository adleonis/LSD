#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Shawnee',__name__,url_prefix='/Shawnee')


@controller.route('/', methods=['GET'])
def lookup(name='Shawnee'):
    return render_template('Shawnee.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Shawnee loves '+word
    return render_template('Shawnee.html', name=name)

