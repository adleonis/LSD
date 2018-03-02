#!/usr/bin/env python3

from flask import Blueprint, render_template

controller = Blueprint('index',__name__,url_prefix='/')

@controller.route('/', methods=['GET'])
def lookup():
    name = []
    name.append('Kellye')
    name.append('Delmer')
    name.append('Kenneth')
    name.append('Maegan')
    name.append('Consuelo')
    name.append('Norma')
    name.append('Ernie')
    name.append('Ebony')
    name.append('Tena')
    name.append('Sandi')
    name.append('Lilli')
    name.append('Cora')
    name.append('Collette')
    name.append('Rogelio')
    name.append('Roberto')
    name.append('Angeline')
    name.append('Andria')
    name.append('Madeleine')
    name.append('Boris')
    name.append('Roni')
    name.append('Trula')
    name.append('Isadora')
    name.append('Buddy')
    name.append('Delma')
    name.append('Jeanette')
    name.append('Shawnee')
    name.append('Grisel')
    name.append('Randal')
    name.append('Danna')
    name.append('Caryl')
    name.append('Allyn')
    name.append('Bruno')
    name.append('Moises')
    name.append('Hattie')
    name.append('Janice')
    name.append('Clarisa')
    name.append('Cristin')
    name.append('Kacie')
    name.append('Wally')
    name.append('Evon')
    name.append('Krishna')
    name.append('Wai')
    name.append('Bret')
    name.append('Billye')
    name.append('Sunday')
    name.append('Rosendo')
    name.append('Willy')
    name.append('Ulrike')
    name.append('Oralia')
    return render_template('index.html', name=name)