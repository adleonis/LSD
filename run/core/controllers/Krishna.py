#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('Krishna',__name__,url_prefix='/Krishna')


@controller.route('/', methods=['GET'])
def lookup(name='Krishna'):
    return render_template('Krishna.html', name=name)


@controller.route('/<string:word>', methods=['GET'])
def lookup2(word):
    name='Krishna loves '+word
    return render_template('Krishna.html', name=name)

