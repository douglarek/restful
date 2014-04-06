# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

from .tasks.views import mod as tasks

app.register_blueprint(tasks)
