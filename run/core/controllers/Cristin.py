#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Cristin',__name__,url_prefix='/Cristin')


@controller.route('/', methods=['GET'])
def lookup(name='Cristin'):
    return render_template('Cristin.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Cristin loves '+word
    return render_template('Cristin.html', name=name)

