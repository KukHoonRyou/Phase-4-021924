#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug
# 1a. Set Up Imports
from flask import Flask, request, jsonify, make_response 


# 1b. Create instance of Flask
app = Flask(__name__)

# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555

# 2. Create a / route that returns Hello World
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
# 2a. Run the server with `flask run --debug` to check if its in the browser

#3. Create a path /longest-movies
# 3a. Import jsonify, make_response
# 3b. Use the `route` decorator
@app.route('/longest-movies')
def get_longest_movies():
     # 3c. Jsonify and return a response
    prod = {
        "title": "example",
        "genre": "example",
        "length": 3
    }
    return make_response(jsonify(prod), 200)

# https://www.adamsmith.haus/python/docs/flask.jsonify
# 🛑 you may see on internet - jsonify automatically puts application/json mimetype ... arguments are same as dict constructor
# https://www.adamsmith.haus/python/docs/flask.make_response
# 🛑 make_response is for the default views and setting headers in those views

# 🛑 for responses:
# return...doesn't turn the reponse into an object
# jsonify...creates a response object and autmomatically sets correct headers for JSON
# json.dumps...converts Python object into JSON-formatted string
# make_response...helpful mostly for flask views and needing to include headers with those views
# can also make a response object directly resp=Response()

# 4. Create a dynamic route
# 4a. Use the route decorator
@app.route('/productions/<string:title>')
# 🛑 First run in browser and view the title as response just to show that its working
def production(title):
    production_response = {
        "title": title,
        "genere": title,
        "length": 3
    }

    # 4b. Return result as JSON
    return make_response(
        jsonify(production_response),
        200
    )

# 5. View the path and host with request context
# 5a. Import 'request'
# 🛑 this is a LocalProxy object from werkzeug
# 5b. Create route `context` 
@app.route('/context')
def context():
    # 5c. use ipdb
    # import ipdb; 
    # ipdb.set_trace()
    return f'<h1>Path{request.path} Host:{request.host}</h1>'


# 6. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    current_user={"user_id":1, "username":"rose"}
    print(current_user)


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)