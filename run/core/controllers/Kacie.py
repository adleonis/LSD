#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Kacie',__name__,url_prefix='/Kacie')


@controller.route('/', methods=['GET'])
def lookup(name='Kacie'):
    return render_template('Kacie.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Kacie loves '+word
    return render_template('Kacie.html', name=name)

