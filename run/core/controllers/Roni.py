#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Roni',__name__,url_prefix='/Roni')


@controller.route('/', methods=['GET'])
def lookup(name='Roni'):
    return render_template('Roni.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Roni loves '+word
    return render_template('Roni.html', name=name)

