#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Maegan',__name__,url_prefix='/Maegan')


@controller.route('/', methods=['GET'])
def lookup(name='Maegan'):
    return render_template('Maegan.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Maegan loves '+word
    return render_template('Maegan.html', name=name)

