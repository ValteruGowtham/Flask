from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

# Route for /hello
@app.route("/hello")
def hello():
    return "<h1>Hello, Flask!</h1>"

# Route with a dynamic parameter <name>
@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello {name}!</h1>"

# Route with two dynamic integer parameters
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

# Route that handles query parameters (?greeting=...&name=...)
@app.route('/handle_param')
def handle_param():
    if 'greeting' in request.args and 'name' in request.args:
        greeting = request.args['greeting']
        name = request.args['name']
        return f"{greeting} {name}!"
    else:
        return "Missing parameters!"

# Route that handles both GET and POST methods
@app.route('/handle_methods', methods=['GET', 'POST'])
def handle_methods():
    if request.method == 'POST':
        return "This is a POST request!"
    elif request.method == 'GET':
        return "This is a GET request!"     
    else:
        return "U won't see msg"

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)