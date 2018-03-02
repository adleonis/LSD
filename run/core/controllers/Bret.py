#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Bret',__name__,url_prefix='/Bret')


@controller.route('/', methods=['GET'])
def lookup(name='Bret'):
    return render_template('Bret.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Bret loves '+word
    return render_template('Bret.html', name=name)

