#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Sandi',__name__,url_prefix='/Sandi')


@controller.route('/', methods=['GET'])
def lookup(name='Sandi'):
    return render_template('Sandi.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Sandi loves '+word
    return render_template('Sandi.html', name=name)

