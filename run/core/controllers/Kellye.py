#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Kellye',__name__,url_prefix='/Kellye')


@controller.route('/', methods=['GET'])
def lookup(name='Kellye'):
    return render_template('Kellye.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Kellye loves '+word
    return render_template('Kellye.html', name=name)

