#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Kenneth',__name__,url_prefix='/Kenneth')


@controller.route('/', methods=['GET'])
def lookup(name='Kenneth'):
    return render_template('Kenneth.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Kenneth loves '+word
    return render_template('Kenneth.html', name=name)

