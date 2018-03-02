#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Allyn',__name__,url_prefix='/Allyn')


@controller.route('/', methods=['GET'])
def lookup(name='Allyn'):
    return render_template('Allyn.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Allyn loves '+word
    return render_template('Allyn.html', name=name)

