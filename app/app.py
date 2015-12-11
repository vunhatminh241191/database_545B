from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
import MySQLdb

app = Flask(__name__)
auth = HTTPBasicAuth()
db = MySQLdb.connect("localhost", "root", "", "FinalProject")
SECRET_KEY = 'you-will-never-guess'

from . import pages