"""
    API flask que retorna dados em formato JSON
"""

# from flask_ngrok import run_with_ngrok
from flask import Flask
from flask import jsonify
# import random as rk

app = Flask(__name__) #the name of the application package
# run_with_ngrok(app)

d = [
      {'number': 1, 'name': 'Mahesh', 'age': 25, 'country': 'India'},
      {'number': 2, 'name': 'Alex', 'age': 26, 'country': 'UK'},
      {'number': 3, 'name': 'David', 'age': 27, 'country': 'USA'},
      {'number': 4, 'name': 'John', 'age': 28, 'country': 'Canada'},
      {'number': 5, 'name': 'Chris', 'age': 29, 'country': 'France'},
      ]

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
    '''
    The entire line below must be written in a single line.
    '''
    return "<marquee><h3>PARA CHECAR INPUT ADICIONE '/input' AO FINAL DA URL.</h3></marquee>"

@app.route("/input")
def input():
    return jsonify(d)

app.run(debug=True)
