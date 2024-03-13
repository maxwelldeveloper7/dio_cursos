"""
    API flask que retorna dados em formato JSON
"""

from flask import Flask
from flask import jsonify


app = Flask(__name__) 

d = [
      {'number': 1, 'name': 'Mahesh', 'age': 25, 'country': 'India'},
      {'number': 2, 'name': 'Alex', 'age': 26, 'country': 'UK'},
      {'number': 3, 'name': 'David', 'age': 27, 'country': 'USA'},
      {'number': 4, 'name': 'John', 'age': 28, 'country': 'Canada'},
      {'number': 5, 'name': 'Chris', 'age': 29, 'country': 'France'},
      ]

@app.route("/") 

def home():
    '''
        Retorno das informações em formato JSON
    '''
    return jsonify(d)

app.run(debug=True)
