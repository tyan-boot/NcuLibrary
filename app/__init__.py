from flask import Flask

app = Flask(__name__)

email_host = ''
email_user = ''
email_pwd = ''

from . import view
