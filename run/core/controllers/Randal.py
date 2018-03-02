#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Randal',__name__,url_prefix='/Randal')


@controller.route('/', methods=['GET'])
def lookup(name='Randal'):
    return render_template('Randal.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Randal loves '+word
    return render_template('Randal.html', name=name)

