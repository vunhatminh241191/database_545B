from flask import Flask
from flask.ext.mysqldb import MySQL
from flask.ext.httpauth import HTTPBasicAuth
import MySQLdb

app = Flask(__name__)
auth = HTTPBasicAuth()
db = MySQLdb.connect("localhost", "minhvu", "", "FinalProject")
SECRET_KEY = 'you-will-never-guess'

from . import pages