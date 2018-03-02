#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Janice',__name__,url_prefix='/Janice')


@controller.route('/', methods=['GET'])
def lookup(name='Janice'):
    return render_template('Janice.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Janice loves '+word
    return render_template('Janice.html', name=name)

