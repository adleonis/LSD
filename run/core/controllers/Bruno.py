#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Bruno',__name__,url_prefix='/Bruno')


@controller.route('/', methods=['GET'])
def lookup(name='Bruno'):
    return render_template('Bruno.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Bruno loves '+word
    return render_template('Bruno.html', name=name)

