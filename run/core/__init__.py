#!usr/bin/env/ python3

from flask import Flask, render_template

from core.controllers.index import controller as index
from core.controllers.Kellye import controller as Kellye
from core.controllers.Delmer import controller as Delmer
from core.controllers.Kenneth import controller as Kenneth
from core.controllers.Maegan import controller as Maegan
from core.controllers.Consuelo import controller as Consuelo
from core.controllers.Norma import controller as Norma
from core.controllers.Ernie import controller as Ernie
from core.controllers.Ebony import controller as Ebony
from core.controllers.Tena import controller as Tena
from core.controllers.Sandi import controller as Sandi
from core.controllers.Lilli import controller as Lilli
from core.controllers.Cora import controller as Cora
from core.controllers.Collette import controller as Collette
from core.controllers.Rogelio import controller as Rogelio
from core.controllers.Roberto import controller as Roberto
from core.controllers.Angeline import controller as Angeline
from core.controllers.Andria import controller as Andria
from core.controllers.Madeleine import controller as Madeleine
from core.controllers.Boris import controller as Boris
from core.controllers.Roni import controller as Roni
from core.controllers.Trula import controller as Trula
from core.controllers.Isadora import controller as Isadora
from core.controllers.Buddy import controller as Buddy
from core.controllers.Delma import controller as Delma
from core.controllers.Jeanette import controller as Jeanette
from core.controllers.Shawnee import controller as Shawnee
from core.controllers.Grisel import controller as Grisel
from core.controllers.Randal import controller as Randal
from core.controllers.Danna import controller as Danna
from core.controllers.Caryl import controller as Caryl
from core.controllers.Allyn import controller as Allyn
from core.controllers.Bruno import controller as Bruno
from core.controllers.Moises import controller as Moises
from core.controllers.Hattie import controller as Hattie
from core.controllers.Janice import controller as Janice
from core.controllers.Clarisa import controller as Clarisa
from core.controllers.Cristin import controller as Cristin
from core.controllers.Kacie import controller as Kacie
from core.controllers.Wally import controller as Wally
from core.controllers.Evon import controller as Evon
from core.controllers.Krishna import controller as Krishna
from core.controllers.Wai import controller as Wai
from core.controllers.Bret import controller as Bret
from core.controllers.Billye import controller as Billye
from core.controllers.Sunday import controller as Sunday
from core.controllers.Rosendo import controller as Rosendo
from core.controllers.Willy import controller as Willy
from core.controllers.Ulrike import controller as Ulrike
from core.controllers.Oralia import controller as Oralia

omnibus = Flask(__name__)
omnibus.register_blueprint(index)
omnibus.register_blueprint(Kellye)
omnibus.register_blueprint(Delmer)
omnibus.register_blueprint(Kenneth)
omnibus.register_blueprint(Maegan)
omnibus.register_blueprint(Consuelo)
omnibus.register_blueprint(Norma)
omnibus.register_blueprint(Ernie)
omnibus.register_blueprint(Ebony)
omnibus.register_blueprint(Tena)
omnibus.register_blueprint(Sandi)
omnibus.register_blueprint(Lilli)
omnibus.register_blueprint(Cora)
omnibus.register_blueprint(Collette)
omnibus.register_blueprint(Rogelio)
omnibus.register_blueprint(Roberto)
omnibus.register_blueprint(Angeline)
omnibus.register_blueprint(Andria)
omnibus.register_blueprint(Madeleine)
omnibus.register_blueprint(Boris)
omnibus.register_blueprint(Roni)
omnibus.register_blueprint(Trula)
omnibus.register_blueprint(Isadora)
omnibus.register_blueprint(Buddy)
omnibus.register_blueprint(Delma)
omnibus.register_blueprint(Jeanette)
omnibus.register_blueprint(Shawnee)
omnibus.register_blueprint(Grisel)
omnibus.register_blueprint(Randal)
omnibus.register_blueprint(Danna)
omnibus.register_blueprint(Caryl)
omnibus.register_blueprint(Allyn)
omnibus.register_blueprint(Bruno)
omnibus.register_blueprint(Moises)
omnibus.register_blueprint(Hattie)
omnibus.register_blueprint(Janice)
omnibus.register_blueprint(Clarisa)
omnibus.register_blueprint(Cristin)
omnibus.register_blueprint(Kacie)
omnibus.register_blueprint(Wally)
omnibus.register_blueprint(Evon)
omnibus.register_blueprint(Krishna)
omnibus.register_blueprint(Wai)
omnibus.register_blueprint(Bret)
omnibus.register_blueprint(Billye)
omnibus.register_blueprint(Sunday)
omnibus.register_blueprint(Rosendo)
omnibus.register_blueprint(Willy)
omnibus.register_blueprint(Ulrike)
omnibus.register_blueprint(Oralia)


#@omnibus.route('/',methods=['GET'])
#def homepage():
#    return render_template('index.html')
