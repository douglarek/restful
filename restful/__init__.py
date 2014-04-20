# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

from .tasks.views import mod as tasks
from .home.views import mod as homepage

app.register_blueprint(tasks)
app.register_blueprint(homepage)
