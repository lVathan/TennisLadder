import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development keys'
USERNAME = 'nathan'
PASSWORD = 'yipee'

app = Flask(__name__)
app.config.from_object(__name__)


