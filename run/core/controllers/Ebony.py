#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Ebony',__name__,url_prefix='/Ebony')


@controller.route('/', methods=['GET'])
def lookup(name='Ebony'):
    return render_template('Ebony.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Ebony loves '+word
    return render_template('Ebony.html', name=name)

