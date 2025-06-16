from flask import Flask, jsonify, request, render_template

app = Flask(name)

@app.route('/')
def home():
    return '<h1>Welcome to Flask!</h1>'

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello, {name}!')

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(received=data), 201

if name == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)