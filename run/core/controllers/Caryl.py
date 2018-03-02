#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Caryl',__name__,url_prefix='/Caryl')


@controller.route('/', methods=['GET'])
def lookup(name='Caryl'):
    return render_template('Caryl.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Caryl loves '+word
    return render_template('Caryl.html', name=name)

