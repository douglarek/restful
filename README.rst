RESTful
=======

A RESTful sample with Flask.

-  get todo list:

   ::

       > curl -i -H "Content-Type: application/json" http://restful-flask.herokuapp.com/todo/api/tasks/

       HTTP/1.1 200
       Content-Length: 432
       Via: HTTP/1.1 GWA
       Server: gunicorn/18.0
       Connection: keep-alive
       Date: Sun, 06 Apr 2014 06:46:25 GMT
       Content-Type: application/json

       {
         "tasks": [
           {
             "description": "Amazon, 360buy, Dangdang",
             "done": false,
             "id": 1,
             "title": "Buy Books",
             "uri": "http://restful-flask.herokuapp.com/todo/api/tasks/1"
       },
           {
             "description": "Need to find a good Haskell tutorial on the web",
             "done": false,
             "id": 2,
             "title": "Learn Haskell",
             "uri": "http://restful-flask.herokuapp.com/todo/api/tasks/2"
           }
         ]
       }

-  create a todo item:

   ::

       > curl -i -H "Content-Type: application/json" -X POST -d '{"title": "Learn Python", "description": "go Pythonic"}' http://restful-flask.herokuapp.com/todo/api/tasks/ -u admin:admin

       HTTP/1.1 201 CREATED
       Content-Type: application/json
       Date: Sun, 06 Apr 2014 06:49:30 GMT
       Server: gunicorn/18.0
       Content-Length: 151
       Connection: keep-alive

       {"task": {"done": false, "uri": "http://restful-flask.herokuapp.com/todo/api/tasks/3", "description": "go Pythonic",     "title": "Learn Python", "id": 3}}

-  lookup a single todo item:

   ::

       > curl -i -H "Content-Type: application/json" http://restful-flask.herokuapp.com/todo/api/tasks/1

       HTTP/1.1 200
       Content-Length: 189
       Via: HTTP/1.1 GWA
       Server: gunicorn/18.0
       Connection: keep-alive
       Date: Sun, 06 Apr 2014 06:50:48 GMT
       Content-Type: application/json

       {
         "task": {
         "description": "Amazon, 360buy, Dangdang",
         "done": false,
         "id": 1,
         "title": "Buy Books",
         "uri": "http://restful-flask.herokuapp.com/todo/api/tasks/1"
         }
       }

-  update a todo item:

   ::

       > curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "Learn Python", "description": "go Pythonic"}' http://restful-flask.herokuapp.com/todo/api/tasks/1 -u admin:admin

       HTTP/1.1 200 OK
       Content-Type: application/json
       Date: Sun, 06 Apr 2014 06:51:49 GMT
       Server: gunicorn/18.0
       Content-Length: 179
       Connection: keep-alive

       {
         "task": {
         "description": "go Pythonic",
         "done": false,
         "id": 1,
         "title": "Learn Python",
         "uri": "http://restful-flask.herokuapp.com/todo/api/tasks/1"
         }
       }

-  delete a todo item:

   ::

       > curl -i -H "Content-Type: application/json" -X DELETE  http://restful-flask.herokuapp.com/todo/api/tasks/1 -u    admin:admin

       HTTP/1.1 200 OK
       Content-Type: application/json
       Date: Sun, 06 Apr 2014 06:57:36 GMT
       Server: gunicorn/18.0
       Content-Length: 22
       Connection: keep-alive

       {
         "result": "True"
       }


