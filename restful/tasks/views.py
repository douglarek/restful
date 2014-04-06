# -*- coding: utf-8 -*-

from functools import wraps

from flask import abort, Blueprint, jsonify, make_response, request
from flask.ext.restful import Api, fields, marshal, Resource, reqparse

mod = Blueprint('tasks', __name__, url_prefix='/todo/api/tasks')
api = Api(mod)

tasks = [{
            'id': 1,
            'title': u'Buy Books',
            'description': u'Amazon, 360buy, Dangdang',
            'done': False},
        {
            'id': 2,
            'title': u'Learn Haskell',
            'description': u'Need to find a good Haskell tutorial on the web',
            'done': False}]

task_fields = {
        'id': fields.Integer, # id should be included, since fields.Url uses it.
        'title': fields.String,
        'description': fields.String,
        'done': fields.Boolean,
        'uri': fields.Url('tasks.single', absolute=True)}

check_auth = lambda user, passwd: user == 'admin' and passwd == 'admin'

def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            abort(401)
        return func(*args, **kwargs)
    return decorated


class TaskListAPI(Resource):

    def __init__(self):
        super(TaskListAPI, self).__init__()
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('title', type=str, required=True, help='No task title provided', location='json')
        self.parse.add_argument('description', type=str, default="", location='json')

    def get(self):
        return jsonify(tasks=[marshal(t, task_fields) for t in tasks])

    @requires_auth
    def post(self):
        args = self.parse.parse_args()
        task = {
                'id': tasks and tasks[-1]['id'] + 1 or 1,
                'title': args['title'],
                'description': args['description'],
                'done': False}
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201


class TaskAPI(Resource):

    def __init__(self):
        super(TaskAPI, self).__init__()
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('title', type=str, location='json')
        self.parse.add_argument('description', type=str, location='json')
        self.parse.add_argument('done', type=bool, location='json')

    def get(self, id):
        task = [t for t in tasks if t['id'] == id]
        if not task:
            abort(404)
        return jsonify(task=marshal(task[0], task_fields))

    @requires_auth
    def put(self, id):
        task = [t for t in tasks if t['id'] == id]
        if not task:
            abort(404)
        args = self.parse.parse_args()
        task = task[0]
        for k in args:
            if args[k] is not None:
                task[k] = args[k]
        return jsonify(task=marshal(task, task_fields))

    @requires_auth
    def delete(self, id):
        task = [t for t in tasks if t['id'] == id]
        if not task:
            abort(404)
        tasks.remove(task[0])
        return jsonify(result='True')


api.add_resource(TaskListAPI, '/', endpoint = 'list')
api.add_resource(TaskAPI, '/<int:id>', endpoint = 'single')
