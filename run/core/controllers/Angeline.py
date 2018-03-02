#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Angeline',__name__,url_prefix='/Angeline')


@controller.route('/', methods=['GET'])
def lookup(name='Angeline'):
    return render_template('Angeline.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Angeline loves '+word
    return render_template('Angeline.html', name=name)

