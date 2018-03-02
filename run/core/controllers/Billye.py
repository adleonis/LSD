#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Billye',__name__,url_prefix='/Billye')


@controller.route('/', methods=['GET'])
def lookup(name='Billye'):
    return render_template('Billye.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Billye loves '+word
    return render_template('Billye.html', name=name)

