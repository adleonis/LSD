#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Sunday',__name__,url_prefix='/Sunday')


@controller.route('/', methods=['GET'])
def lookup(name='Sunday'):
    return render_template('Sunday.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Sunday loves '+word
    return render_template('Sunday.html', name=name)

